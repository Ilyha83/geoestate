# -*- coding: utf-8 -*-
"""
Robust Browser Automation Collector using Playwright with Real Chrome.
Features:
- Resilient typing via keyboard.insert_text (handles Quill/ProseMirror/Angular rich text).
- Single browser session for all platforms (faster, no profile locking).
- Automatic login detection and friendly prompt if login/captcha is shown.
- Automatic debug screenshot capture on any error.
"""

import time
from pathlib import Path
from typing import List, Dict, Any
from playwright.sync_api import sync_playwright
from config import BROWSER_PROFILE_DIR, BASE_DIR

CHROME_CHANNEL = "chrome"
DEBUG_DIR = BASE_DIR / "debug"
DEBUG_DIR.mkdir(parents=True, exist_ok=True)


def setup_auth():
    """
    Launches Chrome in interactive mode with persistent profile.
    Allows user to log in to ChatGPT, Perplexity and Gemini.
    """
    print("\n" + "=" * 60)
    print(" НАСТРОЙКА АВТОРИЗАЦИИ В НЕЙРОСЕТЯХ")
    print(" Сейчас откроется Google Chrome с изолированным профилем.")
    print(" 1. Войдите в свой аккаунт на https://chatgpt.com")
    print(" 2. Войдите в свой аккаунт на https://www.perplexity.ai")
    print(" 3. Войдите в свой аккаунт на https://gemini.google.com")
    print(" 4. Когда закончите — вернитесь сюда и нажмите Enter.")
    print("=" * 60 + "\n")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(BROWSER_PROFILE_DIR),
            channel=CHROME_CHANNEL,
            headless=False,
            ignore_default_args=["--enable-automation"],
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox"
            ]
        )

        p1 = context.pages[0] if context.pages else context.new_page()
        p1.goto("https://chatgpt.com/")

        p2 = context.new_page()
        p2.goto("https://www.perplexity.ai/")

        p3 = context.new_page()
        p3.goto("https://gemini.google.com/app")

        input("\n>>> Нажмите ENTER в этой консоли ПОСЛЕ того, как успешно авторизуетесь на ВСЕХ сайтах: ")
        print("[Auth] Сохранение сессии и закрытие браузера...")
        context.close()
        print("[Auth] Профиль успешно сохранен в:", BROWSER_PROFILE_DIR)


def wait_and_type(page, selectors: List[str], text: str, platform_name: str, timeout_sec: int = 40) -> bool:
    """
    Finds input area, focuses it, and sends text via keyboard.insert_text.
    If login screen or Cloudflare is detected, prompts the user.
    """
    start_time = time.time()
    input_el = None
    notified_cf = False

    while time.time() - start_time < timeout_sec:
        # Check for Cloudflare Challenge
        page_content = page.content().lower()
        if ("cloudflare" in page_content or "challenge-running" in page_content or "turnstile" in page_content) and not notified_cf:
            print(f"\n[{platform_name}] ⚠️ ВНИМАНИЕ: Появилась проверка Cloudflare ('Подтвердите, что вы человек').")
            print(f"[{platform_name}] Пожалуйста, нажмите галочку в открывшемся окне браузера...")
            notified_cf = True

        for sel in selectors:
            try:
                locator = page.locator(sel)
                if locator.count() > 0 and locator.first.is_visible():
                    input_el = locator.first
                    break
            except Exception:
                pass

        if input_el:
            break
        time.sleep(1.5)

    if not input_el:
        ss_path = DEBUG_DIR / f"{platform_name.lower()}_timeout.png"
        page.screenshot(path=str(ss_path))
        print(f"[{platform_name}] Поле ввода не найдено. Скриншот сохранен: {ss_path}")
        return False

    try:
        input_el.click()
        time.sleep(0.5)
        # Use insert_text to bypass complex rich-text Quill/ProseMirror issues
        page.keyboard.insert_text(text)
        time.sleep(1)
        page.keyboard.press("Enter")
        return True
    except Exception as e:
        print(f"[{platform_name}] Ошибка ввода текста: {e}")
        return False


def run_all_browser_audits(prompts: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    """
    Runs all 3 platforms (Gemini, ChatGPT, Perplexity) inside ONE single Chrome session.
    """
    all_results = []
    print("\n[Browser Collector] Запуск единой браузерной сессии Chrome...")

    with sync_playwright() as p:
        try:
            context = p.chromium.launch_persistent_context(
                user_data_dir=str(BROWSER_PROFILE_DIR),
                channel=CHROME_CHANNEL,
                headless=False,
                ignore_default_args=["--enable-automation"],
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox"
                ]
            )
            page = context.pages[0] if context.pages else context.new_page()

            # ----------------------------------------------------
            # 1. Google Gemini
            # ----------------------------------------------------
            print("\n>>> [1/3] Опрос Google Gemini...")
            gemini_selectors = [
                'div.ql-editor[contenteditable="true"]',
                'div[contenteditable="true"]',
                'p[data-placeholder]',
                'textarea'
            ]
            for p_info in prompts:
                pid = p_info["id"]
                ptext = p_info["text"]
                print(f"[Gemini] Запрос: {p_info.get('title', pid)}...")

                page.goto("https://gemini.google.com/app", wait_until="domcontentloaded")
                time.sleep(3)

                success = wait_and_type(page, gemini_selectors, ptext, "Gemini")
                if not success:
                    continue

                print("[Gemini] Ожидание генерации ответа...")
                time.sleep(8)
                for _ in range(25):
                    time.sleep(2)
                    stop_btn = page.locator('button[aria-label*="Остановить"], button[aria-label*="Stop"]')
                    if stop_btn.count() == 0:
                        break

                time.sleep(3)
                containers = page.locator('message-content, .model-response-text, div[data-test-id="conversation-turn"]')
                text = containers.last.inner_text() if containers.count() > 0 else page.locator("main").inner_text()
                print(f"[Gemini] Ответ получен ({len(text)} симв.)")
                all_results.append({"platform": "Gemini", "prompt_id": pid, "response_text": text})
                time.sleep(2)

            # ----------------------------------------------------
            # 2. ChatGPT
            # ----------------------------------------------------
            print("\n>>> [2/3] Опрос ChatGPT...")
            chatgpt_selectors = [
                '#prompt-textarea',
                'div[contenteditable="true"]',
                'textarea'
            ]
            for p_info in prompts:
                pid = p_info["id"]
                ptext = p_info["text"]
                print(f"[ChatGPT] Запрос: {p_info.get('title', pid)}...")

                page.goto("https://chatgpt.com/?model=auto", wait_until="domcontentloaded")
                time.sleep(3)

                success = wait_and_type(page, chatgpt_selectors, ptext, "ChatGPT")
                if not success:
                    continue

                print("[ChatGPT] Ожидание генерации ответа...")
                time.sleep(6)
                for _ in range(35):
                    time.sleep(2)
                    stop_btn = page.locator('button[data-testid="stop-button"], button[aria-label="Stop streaming"]')
                    if stop_btn.count() == 0:
                        break

                time.sleep(3)
                articles = page.locator('article, div[data-message-author-role="assistant"]')
                text = articles.last.inner_text() if articles.count() > 0 else page.locator("main").inner_text()
                print(f"[ChatGPT] Ответ получен ({len(text)} симв.)")
                all_results.append({"platform": "ChatGPT", "prompt_id": pid, "response_text": text})
                time.sleep(2)

            # ----------------------------------------------------
            # 3. Perplexity AI
            # ----------------------------------------------------
            print("\n>>> [3/3] Опрос Perplexity...")
            perplexity_selectors = [
                'textarea[placeholder*="Ask"]',
                'textarea',
                'div[contenteditable="true"]'
            ]
            for p_info in prompts:
                pid = p_info["id"]
                ptext = p_info["text"]
                print(f"[Perplexity] Запрос: {p_info.get('title', pid)}...")

                page.goto("https://www.perplexity.ai/", wait_until="domcontentloaded")
                time.sleep(3)

                success = wait_and_type(page, perplexity_selectors, ptext, "Perplexity")
                if not success:
                    continue

                print("[Perplexity] Ожидание поиска и ответа...")
                time.sleep(8)
                for _ in range(25):
                    time.sleep(2)
                    stop_ind = page.locator('button[aria-label="Stop"], button[data-testid="stop-generating"]')
                    if stop_ind.count() == 0:
                        break

                time.sleep(3)
                containers = page.locator('.prose, div[dir="auto"], [data-testid="answer"]')
                text = containers.first.inner_text() if containers.count() > 0 else page.locator("main").inner_text()
                print(f"[Perplexity] Ответ получен ({len(text)} симв.)")
                all_results.append({"platform": "Perplexity", "prompt_id": pid, "response_text": text})
                time.sleep(2)

            context.close()
        except Exception as e:
            print(f"[Browser Collector] Ошибка выполнения: {e}")

    return all_results
