# -*- coding: utf-8 -*-
"""
Main Weekly Orchestrator for AI Developer Ranking.
Coordinates data collection, NLP scoring, SQLite persistence and JSON export.
"""

import sys
import argparse
from datetime import datetime
from pathlib import Path

from config import WEEKLY_PROMPTS, DEFAULT_COUNTRY, LATEST_JSON_PATH
from browser_collector import run_all_browser_audits, setup_auth
from analyzer import score_responses
from storage import save_audit_run, export_latest_json


def load_initial_benchmark():
    """
    Populates the database with real benchmark data from ai_presence_research
    so the dashboard is immediately operational with authentic ratings.
    """
    sample_data = [
        {
            "id": "dovec", "name": "Döveç Group", "region": "Famagusta / İskele",
            "mentions_count": 22, "recommendations_count": 18, "risks_count": 0,
            "sov_percent": 73.3, "recommendation_rate": 81.8, "final_score": 86.2, "rank": 1,
            "pros": "Лидер репутации №1: награды PropertyNC, Google 4.3 (127 отзывов), собственная УК",
            "risks": "Критических стоп-факторов не обнаружено"
        },
        {
            "id": "northernland", "name": "NorthernLAND", "region": "İskele / Famagusta",
            "mentions_count": 24, "recommendations_count": 17, "risks_count": 0,
            "sov_percent": 80.0, "recommendation_rate": 70.8, "final_score": 83.9, "rank": 2,
            "pros": "Архитектурный масштаб, Grand Sapphire (1 630 квартир), 14 сданных комплексов",
            "risks": "Критических стоп-факторов не обнаружено"
        },
        {
            "id": "ozyalcin", "name": "Özyalçın Construction", "region": "Kyrenia",
            "mentions_count": 6, "recommendations_count": 4, "risks_count": 0,
            "sov_percent": 20.0, "recommendation_rate": 66.7, "final_score": 68.0, "rank": 3,
            "pros": "Безупречная репутация в центре Кирении с 1987 г., 2 500+ построенных домов",
            "risks": "Критических стоп-факторов не обнаружено"
        },
        {
            "id": "carrington", "name": "Carrington Group", "region": "Kyrenia / Esentepe",
            "mentions_count": 8, "recommendations_count": 5, "risks_count": 0,
            "sov_percent": 26.7, "recommendation_rate": 62.5, "final_score": 68.8, "rank": 4,
            "pros": "Лидер прибрежной недвижимости Кирении (16 сданных проектов из 24)",
            "risks": "Критических стоп-факторов не обнаружено"
        },
        {
            "id": "noyanlar", "name": "Noyanlar Group", "region": "İskele (Long Beach)",
            "mentions_count": 22, "recommendations_count": 10, "risks_count": 5,
            "sov_percent": 73.3, "recommendation_rate": 45.4, "final_score": 59.8, "rank": 5,
            "pros": "Первопроходец Лонг-Бич, 50 лет истории, тысячи сданных квартир серии Royal",
            "risks": "Пессимизация в AI из-за отзывов на Trustpilot (рейтинг 2.2) и жалоб на Şikayetvar"
        },
        {
            "id": "cyprus_constructions", "name": "Cyprus Constructions", "region": "Esentepe / Kyrenia",
            "mentions_count": 14, "recommendations_count": 4, "risks_count": 1,
            "sov_percent": 46.7, "recommendation_rate": 28.6, "final_score": 48.5, "rank": 6,
            "pros": "Курортные комплексы в Эсентепе (Maldives Homes), 28+ лет опыта, 2 000 сданных юнитов",
            "risks": "Умеренное количество прямых упоминаний в поисковых выдачах"
        },
        {
            "id": "emtan", "name": "Emtan Construction", "region": "Kyrenia",
            "mentions_count": 12, "recommendations_count": 2, "risks_count": 0,
            "sov_percent": 40.0, "recommendation_rate": 16.7, "final_score": 43.5, "rank": 7,
            "pros": "Городской сегмент Кирении, высокий рейтинг в Google Maps (4.9)",
            "risks": "Слабая видимость за пределами Кирении"
        },
        {
            "id": "afik", "name": "Afik Group", "region": "İskele / Trikomo",
            "mentions_count": 18, "recommendations_count": 7, "risks_count": 8,
            "sov_percent": 60.0, "recommendation_rate": 38.9, "final_score": 38.0, "rank": 8,
            "pros": "Мега-резорты Caesar (7 000 юнитов), аквапарки и развитая инфраструктура",
            "risks": "Жесткий стоп-фактор: судебный процесс на Южном Кипре (MarketScreener)"
        },
        {
            "id": "kibris_dev", "name": "Kıbrıs Developments", "region": "Edremit / Kyrenia",
            "mentions_count": 8, "recommendations_count": 3, "risks_count": 0,
            "sov_percent": 26.7, "recommendation_rate": 37.5, "final_score": 37.1, "rank": 9,
            "pros": "Экопоселки премиум-класса в Лапте/Эдремите, гармония с природой",
            "risks": "Узкая нишевая представленность"
        },
        {
            "id": "isatis", "name": "Isatis Construction", "region": "Famagusta",
            "mentions_count": 10, "recommendations_count": 2, "risks_count": 0,
            "sov_percent": 33.3, "recommendation_rate": 20.0, "final_score": 32.3, "rank": 10,
            "pros": "Городской кластер Фамагусты (Енибогазичи, Каракол у City Mall), 102 сданных объекта",
            "risks": "Мало цитирований в международных англоязычных хабах"
        },
        {
            "id": "evergreen", "name": "Evergreen Developments", "region": "Esentepe / Lefke",
            "mentions_count": 9, "recommendations_count": 0, "risks_count": 3,
            "sov_percent": 30.0, "recommendation_rate": 0.0, "final_score": 15.0, "rank": 11,
            "pros": "Экологичные поселки на побережье",
            "risks": "Нулевая конверсия в рекомендации из-за негативного кейса на Trustpilot"
        },
        {
            "id": "uzun", "name": "Uzun Group", "region": "Famagusta / İskele",
            "mentions_count": 4, "recommendations_count": 0, "risks_count": 3,
            "sov_percent": 13.3, "recommendation_rate": 0.0, "final_score": 5.0, "rank": 12,
            "pros": "Локальное присутствие в Фамагусте",
            "risks": "Критически низкий рейтинг в Google Reviews (2.6 / 5.0)"
        }
    ]

    run_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    platforms = ["ChatGPT", "Gemini", "Perplexity"]
    save_audit_run(run_date, DEFAULT_COUNTRY, platforms, [], sample_data)
    print(f"[Benchmark] Базовые данные успешно импортированы в базу и {LATEST_JSON_PATH}")


def main():
    parser = argparse.ArgumentParser(description="AI Developer Ranking Weekly Auditor")
    parser.add_argument("--setup-auth", action="store_true", help="Launch Chrome to log in to ChatGPT & Perplexity")
    parser.add_argument("--init-benchmark", action="store_true", help="Load existing research benchmark data")
    parser.add_argument("--gemini-only", action="store_true", help="Run audit only via Gemini API")
    parser.add_argument("--browser-only", action="store_true", help="Run audit only via Browser (ChatGPT + Perplexity)")
    args = parser.parse_args()

    if args.setup_auth:
        setup_auth()
        return

    if args.init_benchmark:
        load_initial_benchmark()
        return

    run_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    platforms = ["Gemini", "ChatGPT", "Perplexity"]

    print(f"\n========================================================")
    print(f" ЗАПУСК ЕЖЕНЕДЕЛЬНОГО АУДИТА: {DEFAULT_COUNTRY}")
    print(f" Дата: {run_date}")
    print(f"========================================================\n")

    # Run all audits in a single resilient browser session
    all_responses = run_all_browser_audits(WEEKLY_PROMPTS)

    if not all_responses:
        print("\n[Внимание] Не получено ни одного ответа. Проверьте авторизацию в 1_setup_auth.bat.")
        return

    # 3. NLP Scoring
    print("\n>>> ЭТАП 4: Анализ и пересчет рейтинга...")
    scored = score_responses(all_responses)

    # 4. Save and Export
    run_id = save_audit_run(run_date, DEFAULT_COUNTRY, platforms, all_responses, scored)
    print(f"\n[Успешно] Аудит #{run_id} сохранен в БД. Экспортирован файл: {LATEST_JSON_PATH}")

    # 5. Print Summary Table
    print("\n" + "=" * 80)
    print(f"{'Ранг':<5} | {'Застройщик':<26} | {'Регион':<20} | {'AI Score':<8} | {'SoV %':<6} | {'Rec %':<6}")
    print("-" * 80)
    for dev in scored:
        print(f"{dev['rank']:<5} | {dev['name']:<26} | {dev['region'][:20]:<20} | {dev['final_score']:<8.1f} | {dev['sov_percent']:<6.1f} | {dev['recommendation_rate']:<6.1f}")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
