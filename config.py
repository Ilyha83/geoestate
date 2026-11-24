# -*- coding: utf-8 -*-
"""
Configuration for AI Developer Ranking System.
Defines prompts, monitored developers, paths and scoring weights.
"""

from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent
BROWSER_PROFILE_DIR = BASE_DIR / "browser_data"
RAW_ANSWERS_DIR = BASE_DIR / "raw_answers"
DB_PATH = BASE_DIR / "rankings.db"
LATEST_JSON_PATH = BASE_DIR / "rankings_latest.json"

# Ensure directories exist
RAW_ANSWERS_DIR.mkdir(parents=True, exist_ok=True)
BROWSER_PROFILE_DIR.mkdir(parents=True, exist_ok=True)

# Monitored Region
DEFAULT_COUNTRY = "Северный Кипр"
DEFAULT_COUNTRY_CODE = "NC"

# 3 Comprehensive Weekly Prompts
WEEKLY_PROMPTS = [
    {
        "id": "PROMPT_1_TOP_REGIONS",
        "title": "Рейтинг по регионам и масштабу",
        "text": (
            "Назови топ-5 застройщиков Северного Кипра для покупки жилья и инвестиций. "
            "Отдельно выдели лидеров в Кирении (Kyrenia / Girne), Искеле (Long Beach / Iskele) и Фамагусте (Famagusta / Gazimagusa). "
            "Укажи их знаковые сданные проекты и почему ты их рекомендуешь."
        )
    },
    {
        "id": "PROMPT_2_RISKS_REPUTATION",
        "title": "Надежность, титулы и юридические риски",
        "text": (
            "Проанализируй застройщиков Северного Кипра на надежность: у кого чистые титулы (Eşdeğer / Pre-74) и сдача в срок, "
            "а у кого зафиксированы задержки, судебные разбирательства, проблемы с инфраструктурой или низкие отзывы (Google Reviews, Trustpilot, Sikayetvar)? "
            "Кого ты рекомендуешь обходить стороной или проверять с осторожностью?"
        )
    },
    {
        "id": "PROMPT_3_ROI_SERVICE",
        "title": "Инвестиции, доходность и управляющие компании",
        "text": (
            "Какие застройщики Северного Кипра обеспечивают лучшую арендную доходность (ROI), ликвидность перепродажи "
            "и качественное постпродажное обслуживание (собственные управляющие компании)? Сравни ключевых игроков по соотношению цена/качество."
        )
    }
]

# Monitored Developers & Aliases for North Cyprus
TRACKED_DEVELOPERS = [
    {
        "id": "dovec",
        "name": "Döveç Group",
        "aliases": ["döveç", "dovec", "домеч", "довец"],
        "region": "Famagusta / İskele",
        "website": "https://dovecgroup.com"
    },
    {
        "id": "northernland",
        "name": "NorthernLAND",
        "aliases": ["northernland", "northern land", "нозернлэнд", "нозерн лэнд", "нортенлэнд"],
        "region": "İskele / Famagusta / Kyrenia",
        "website": "https://northernland.com"
    },
    {
        "id": "noyanlar",
        "name": "Noyanlar Group",
        "aliases": ["noyanlar", "ноянлар"],
        "region": "İskele (Long Beach)",
        "website": "https://noyanlar.com"
    },
    {
        "id": "afik",
        "name": "Afik Group",
        "aliases": ["afik", "афик", "caesar project", "caesar resort"],
        "region": "İskele / Trikomo",
        "website": "https://afikgroup.com"
    },
    {
        "id": "cyprus_constructions",
        "name": "Cyprus Constructions",
        "aliases": ["cyprus constructions", "сайпрус констракшнс", "maldives homes", "idyll homes"],
        "region": "Esentepe / Kyrenia",
        "website": "https://cyprus-constructions.com"
    },
    {
        "id": "emtan",
        "name": "Emtan Construction",
        "aliases": ["emtan", "эмтан"],
        "region": "Kyrenia",
        "website": "https://emtancons.com"
    },
    {
        "id": "ozyalcin",
        "name": "Özyalçın Construction",
        "aliases": ["özyalçın", "ozyalcin", "озялчин"],
        "region": "Kyrenia",
        "website": "https://ozyalcinconstruction.com"
    },
    {
        "id": "carrington",
        "name": "Carrington Group",
        "aliases": ["carrington", "каррингтон"],
        "region": "Kyrenia / Esentepe",
        "website": "https://carringtongroup.com"
    },
    {
        "id": "kibris_dev",
        "name": "Kıbrıs Developments",
        "aliases": ["kıbrıs developments", "kibris developments", "кибрис девелопментс", "milos park"],
        "region": "Edremit / Kyrenia",
        "website": "https://kibrisdevelopments.com"
    },
    {
        "id": "evergreen",
        "name": "Evergreen Developments",
        "aliases": ["evergreen", "эвергрин"],
        "region": "Esentepe / Lefke",
        "website": "https://evergreencyprus.com"
    },
    {
        "id": "isatis",
        "name": "Isatis Construction",
        "aliases": ["isatis", "исатис"],
        "region": "Famagusta / Yeniboğaziçi",
        "website": "https://www.isatis.co"
    },
    {
        "id": "akol",
        "name": "Akol Global",
        "aliases": ["akol", "акол"],
        "region": "İskele / Famagusta",
        "website": "https://akolglobal.com"
    },
    {
        "id": "kensington",
        "name": "Kensington Cyprus",
        "aliases": ["kensington", "кенсингтон"],
        "region": "Esentepe",
        "website": "https://kensingtoncyprus.com"
    },
    {
        "id": "uzun",
        "name": "Uzun Group",
        "aliases": ["uzun", "узун"],
        "region": "Famagusta / İskele",
        "website": "https://uzungroup.com"
    }
]
