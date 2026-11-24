# -*- coding: utf-8 -*-
"""
Collector for Google Gemini API.
Uses official Google Search Grounding for live real-time web retrieval.
"""

import os
from pathlib import Path
from typing import List, Dict, Any
from dotenv import load_dotenv

# Try loading from local .env or parent .env files
ENV_PATHS = [
    Path(__file__).resolve().parent / ".env",
    Path("d:/Qoder/vlog_planner_bot/.env"),
    Path("d:/Qoder/.env")
]
for p in ENV_PATHS:
    if p.exists():
        load_dotenv(p)
        break

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def run_gemini_prompts(prompts: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    """
    Executes prompts against Gemini with Google Search Grounding enabled.
    """
    if not GEMINI_API_KEY:
        print("[Gemini] ВНИМАНИЕ: GEMINI_API_KEY не задан в .env файле.")
        return []

    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=GEMINI_API_KEY)
        responses = []

        for p in prompts:
            prompt_id = p["id"]
            prompt_text = p["text"]
            print(f"[Gemini] Запуск аудита: {p.get('title', prompt_id)}...")

            try:
                # Enable Google Search grounding tool
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt_text,
                    config=types.GenerateContentConfig(
                        tools=[{"google_search": {}}],
                        temperature=0.2,
                    ),
                )
                text = response.text or ""
                responses.append({
                    "platform": "Gemini",
                    "prompt_id": prompt_id,
                    "response_text": text
                })
                print(f"[Gemini] Ответ получен ({len(text)} симв.)")
            except Exception as e:
                print(f"[Gemini] Ошибка при запросе {prompt_id}: {e}")

        return responses

    except ImportError:
        print("[Gemini] Библиотека google-genai не найдена. Пропуск.")
        return []
