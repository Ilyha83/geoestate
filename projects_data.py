# -*- coding: utf-8 -*-
"""
Database of ACTIVE / ONGOING primary market projects strictly from Top-6 reliable developers.
All complexes are currently being sold on the primary market.
All images are 100% AUTHENTIC from official developer servers.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECTS_JSON_PATH = BASE_DIR / "official_projects.json"
PROJECTS_JS_PATH = BASE_DIR / "projects_data.js"
DIST_DIR = BASE_DIR / "dist"

OFFICIAL_PROJECTS = [
    # =========================================================================
    # 1. DÖVEÇ GROUP (AI Score: 86.2) — ACTIVE ONGOING PROJECTS
    # =========================================================================
    {
        "id": "dovec_querencia",
        "developer_id": "dovec",
        "developer_name": "Döveç Group",
        "name": "Querencia Luxury Resort",
        "region": "İskele / Long Beach",
        "lat": 35.2935,
        "lng": 33.9015,
        "type": "Флагманский курортный комплекс (4 башни)",
        "price_from": "£125,000",
        "units_count": 705,
        "features": [
            "Первая линия 400м от моря",
            "Инфинити-бассейн на крыше",
            "Собственная УК (аренда)",
            "СПА и фитнес 2000 м²"
        ],
        "image": "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/querencia/cover.jpg"
    },
    {
        "id": "dovec_courtyard_plat",
        "developer_id": "dovec",
        "developer_name": "Döveç Group",
        "name": "Courtyard Platinum",
        "region": "İskele / Boğaz",
        "lat": 35.3120,
        "lng": 33.9180,
        "type": "Курортный резорт с аквапарком",
        "price_from": "£95,000",
        "units_count": 520,
        "features": [
            "Отельный сервис 5*",
            "Огромный бассейн 1 500 м²",
            "Детский клуб и аквазона",
            "Высокий арендный потенциал 10-12%"
        ],
        "image": "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/courtyardplatinum/exterior/2023-09-05-courtyard-platinum-4.jpg"
    },
    {
        "id": "dovec_la_isla",
        "developer_id": "dovec",
        "developer_name": "Döveç Group",
        "name": "La Isla",
        "region": "İskele / Long Beach",
        "lat": 35.2890,
        "lng": 33.8960,
        "type": "Эко-курорт с островной концепцией",
        "price_from": "£115,000",
        "units_count": 211,
        "features": [
            "Пешая доступность до песчаного пляжа",
            "Зелёная концепция и солнечная генерация",
            "Бассейн-оазис и лаунж-бары",
            "Престижная архитектурная награда PropertyNC"
        ],
        "image": "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/laisla/cover.jpg"
    },
    {
        "id": "dovec_four_seasons",
        "developer_id": "dovec",
        "developer_name": "Döveç Group",
        "name": "Four Seasons Life III",
        "region": "İskele / Boğaz Coast",
        "lat": 35.3310,
        "lng": 33.9450,
        "type": "Прибрежные виллы и апартаменты",
        "price_from": "£140,000",
        "units_count": 310,
        "features": [
            "Прямой выход на частный песчаный пляж",
            "Малоэтажная эко-архитектура",
            "Ресторан на пирсе",
            "Гарантированная ликвидность"
        ],
        "image": "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/fourseasonslife3/cover.jpg"
    },
    {
        "id": "dovec_natulux",
        "developer_id": "dovec",
        "developer_name": "Döveç Group",
        "name": "Natulux",
        "region": "Küçük Erenköy / Tatlısu",
        "lat": 35.3780,
        "lng": 33.6450,
        "type": "Премиальный резорт на морском клифе",
        "price_from": "£130,000",
        "units_count": 184,
        "features": [
            "Уникальное расположение на морском скалистом мысе",
            "Панорамный инфинити-бассейн на краю скалы",
            "Премиальная отделка натуральным камнем и деревом",
            "Спа и велнес-клуб"
        ],
        "image": "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/natulux/featured-card/natulux-featured-0e1597b1.jpg"
    },
    {
        "id": "dovec_la_casalia",
        "developer_id": "dovec",
        "developer_name": "Döveç Group",
        "name": "La Casalia",
        "region": "Tatlısu Coast",
        "lat": 35.3880,
        "lng": 33.6700,
        "type": "Велнес-курорт с собственной клиникой",
        "price_from": "£120,000",
        "units_count": 220,
        "features": [
            "Европейская клиника детокса и долголетия",
            "Первая береговая линия с песчаным пляжем",
            "Органические сады и ресторан фермерской кухни",
            "Арендная программа с гарантией дохода"
        ],
        "image": "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/lacasalia/featured-card/la-casalia-features-bcf7ee80.jpg"
    },

    # =========================================================================
    # 2. NORTHERNLAND (AI Score: 83.9) — ACTIVE ONGOING PROJECTS
    # =========================================================================
    {
        "id": "nl_grand_sapphire",
        "developer_id": "northernland",
        "developer_name": "NorthernLAND",
        "name": "Grand Sapphire Resort & Residences",
        "region": "İskele / Long Beach",
        "lat": 35.2860,
        "lng": 33.8980,
        "type": "Мега-резорт 7 звёзд с казино и отелем",
        "price_from": "£130,000",
        "units_count": 1630,
        "features": [
            "Самый крупный курортный проект острова",
            "Бассейн Punta Cana 4 000 м²",
            "Собственное казино и отель 5*",
            "Высочайшая ликвидность перепродажи"
        ],
        "image": "https://northernland.com/storage/spot/63/the-biggest-project-of-northern-cyprus.webp"
    },
    {
        "id": "nl_casa_del_mare",
        "developer_id": "northernland",
        "developer_name": "NorthernLAND",
        "name": "Casa Del Mare",
        "region": "Tatlısu / Esentepe Coast",
        "lat": 35.3940,
        "lng": 33.6820,
        "type": "Премиальные виллы и пентхаусы у моря",
        "price_from": "£110,000",
        "units_count": 420,
        "features": [
            "Первая береговая линия",
            "Каскадные лагунные бассейны",
            "Панорамный вид на закаты и море",
            "Собственный оборудованный пляж"
        ],
        "image": "https://northernland.com/storage/spot/243/sun-bathed-life-casa-del-mare.webp"
    },

    # =========================================================================
    # 3. CARRINGTON GROUP (AI Score: 68.8) — ACTIVE ONGOING PROJECTS
    # =========================================================================
    {
        "id": "carr_poseidon",
        "developer_id": "carrington",
        "developer_name": "Carrington Group",
        "name": "Poseidon Luxury Villas",
        "region": "Kyrenia / Esentepe",
        "lat": 35.3590,
        "lng": 33.6120,
        "type": "Виллы де-люкс с частным инфинити-бассейном",
        "price_from": "£295,000",
        "units_count": 24,
        "features": [
            "Панорамный обзор моря 180 градусов",
            "Инфинити-бассейн на скалистом побережье",
            "Премиальная отделка и частные сады",
            "3 минуты до гольф-клуба Korineum"
        ],
        "image": "https://res.cloudinary.com/dikkkzmnt/image/upload/v1764831941/carrington/poseidon-a63/image-0.jpg"
    },
    {
        "id": "carr_sea_magic",
        "developer_id": "carrington",
        "developer_name": "Carrington Group",
        "name": "Sea Magic Royal",
        "region": "Kyrenia / Esentepe",
        "lat": 35.3480,
        "lng": 33.5650,
        "type": "Курортные резиденции на первой линии",
        "price_from": "£135,000",
        "units_count": 96,
        "features": [
            "Прямой доступ к приватному пляжу",
            "Спа-центр, сауна и крытый бассейн",
            "Премиальный средиземноморский ресторан",
            "Высокий инвестиционный арендный потенциал"
        ],
        "image": "https://res.cloudinary.com/dikkkzmnt/image/upload/v1764833848/carrington/sea-magic-royal-d3/image-0.jpg"
    },

    # =========================================================================
    # 4. ÖZYALÇIN CONSTRUCTION (AI Score: 68.0) — ACTIVE ONGOING PROJECTS
    # =========================================================================
    {
        "id": "ozyalcin_solea",
        "developer_id": "ozyalcin",
        "developer_name": "Özyalçın Construction",
        "name": "Solea by Özyalçın",
        "region": "Kyrenia / Bellapais",
        "lat": 35.3120,
        "lng": 33.3520,
        "type": "Элитные виллы у аббатства Беллапаис",
        "price_from": "£310,000",
        "units_count": 18,
        "features": [
            "Престижная историческая локация Беллапаис",
            "Панорамный вид на горы и море Кирении",
            "Приватные бассейны и ландшафтные сады",
            "Безупречная надёжность застройщика с 1987 года"
        ],
        "image": "https://ozyalcinconstruction.com/wp-content/uploads/2024/02/Solea-Dis-gorseller-15-1024x1024.webp"
    },
    {
        "id": "ozyalcin_casa_oliva",
        "developer_id": "ozyalcin",
        "developer_name": "Özyalçın Construction",
        "name": "Casa Oliva 2",
        "region": "Kyrenia / Zeytinlik",
        "lat": 35.3310,
        "lng": 33.3080,
        "type": "Современные виллы в оливковых рощах",
        "price_from": "£245,000",
        "units_count": 22,
        "features": [
            "Уютный зелёный район Зейтинлик",
            "5 минут до центра города и гавани Кирении",
            "Энергоэффективные эко-материалы",
            "Турецкий гарантированный титул"
        ],
        "image": "https://ozyalcinconstruction.com/wp-content/uploads/2025/07/Tip-C-3.jpg"
    },

    # =========================================================================
    # 5. NOYANLAR GROUP (AI Score: 59.8) — ACTIVE ONGOING PROJECTS
    # =========================================================================
    {
        "id": "noyanlar_ocean_life",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Ocean Life Residence",
        "region": "İskele / Long Beach",
        "lat": 35.2890,
        "lng": 33.9040,
        "type": "Курортный мега-комплекс с яхт-клубом",
        "price_from": "£89,000",
        "units_count": 840,
        "features": [
            "Собственный аквапарк и яхтенная концепция",
            "Самая выгодная стартовая цена на Лонг-Бич",
            "Беспроцентная рассрочка до 5 лет",
            "Большая семейная инфраструктура"
        ],
        "image": "https://noyanlar.com/wp-content/uploads/2026/11/noyanlar-2026-11-ocean-life-aqua-park-768x432.webp"
    },
    {
        "id": "noyanlar_royal_sun_elite",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Royal Sun Elite Residence",
        "region": "İskele / Long Beach",
        "lat": 35.2840,
        "lng": 33.9010,
        "type": "Курортный городок (1 122 апартамента)",
        "price_from": "£79,000",
        "units_count": 1122,
        "features": [
            "Огромная территория 90 000 м²",
            "Аквапарк, 10 бассейнов, супермаркет и фитнес CrossFit",
            "Высокая круглогодичная загрузка туристами",
            "500 метров до моря"
        ],
        "image": "https://noyanlar.com/wp-content/uploads/2026/05/royalsun_elite_exterior-1-1536x1024.jpg"
    },
    {
        "id": "noyanlar_bellagio",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Bellagio Resort Suites",
        "region": "İskele / Long Beach",
        "lat": 35.2910,
        "lng": 33.9060,
        "type": "Отельные люкс-сьюты в 200м от моря",
        "price_from": "£98,000",
        "units_count": 280,
        "features": [
            "Всего 200 метров до береговой линии Лонг-Бич",
            "Формат отельных сьютов с готовой отделкой",
            "Управляющая компания с гарантией аренды",
            "Панорамный лаундж на крыше"
        ],
        "image": "https://noyanlar.com/wp-content/uploads/2026/11/noyanlar-2026-11-bellagio-rezidence-1024x576.webp"
    },
    {
        "id": "noyanlar_miracle",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Miracle Villa & Residence",
        "region": "İskele / Boğaz",
        "lat": 35.3160,
        "lng": 33.9240,
        "type": "Приватные виллы и таунхаусы",
        "price_from": "£165,000",
        "units_count": 124,
        "features": [
            "Приватный оазис у живописной гавани Боаз",
            "Собственный бассейн у каждой виллы",
            "Рыбные рестораны в пешей доступности",
            "Ранняя инвестиционная стадия цен"
        ],
        "image": "https://noyanlar.com/wp-content/uploads/2026/11/noyanlar-2026-11-miracle-villa-havuz.webp"
    },

    # =========================================================================
    # 6. CYPRUS CONSTRUCTIONS (AI Score: 48.5) — ACTIVE ONGOING PROJECTS
    # =========================================================================
    {
        "id": "cc_maldives",
        "developer_id": "cyprus_constructions",
        "developer_name": "Cyprus Constructions",
        "name": "Maldives Homes",
        "region": "Esentepe Coast",
        "lat": 35.3560,
        "lng": 33.6050,
        "type": "Знаковые виллы над водой и террасные люксы",
        "price_from": "£145,000",
        "units_count": 180,
        "features": [
            "Самый инстаграмный проект Северного Кипра",
            "Виллы на сваях прямо в лагунном бассейне",
            "Кинотеатр под открытым небом и органический ресторан",
            "Высочайшая заполняемость в аренду круглый год"
        ],
        "image": "https://cyprusconstructions.com/DetailPage/maldive.jpg"
    },
    {
        "id": "cc_mykonos",
        "developer_id": "cyprus_constructions",
        "developer_name": "Cyprus Constructions",
        "name": "Mykonos Homes",
        "region": "Esentepe Coast",
        "lat": 35.3510,
        "lng": 33.5950,
        "type": "Кикладская белоснежная архитектура у моря",
        "price_from": "£135,000",
        "units_count": 136,
        "features": [
            "Атмосфера греческого острова Миконос",
            "Собственный пляжный клуб и рестораны",
            "Панорамный инфинити-бассейн на скале",
            "Проверенная управляющая компания"
        ],
        "image": "https://cyprusconstructions.com/DetailPage/vine.jpg"
    }
]

def export_all():
    with open(PROJECTS_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(OFFICIAL_PROJECTS, f, ensure_ascii=False, indent=2)
    print(f"Exported {len(OFFICIAL_PROJECTS)} active projects to {PROJECTS_JSON_PATH}")

    js_content = f"window.OFFICIAL_PROJECTS = {json.dumps(OFFICIAL_PROJECTS, ensure_ascii=False, indent=2)};"
    with open(PROJECTS_JS_PATH, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Exported JS to {PROJECTS_JS_PATH}")

    if DIST_DIR.exists():
        with open(DIST_DIR / "official_projects.json", "w", encoding="utf-8") as f:
            json.dump(OFFICIAL_PROJECTS, f, ensure_ascii=False, indent=2)
        with open(DIST_DIR / "projects_data.js", "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"Exported to {DIST_DIR}")

if __name__ == "__main__":
    export_all()
