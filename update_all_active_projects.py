# -*- coding: utf-8 -*-
import json, shutil, os

with open(r'd:\Qoder\ai_developer_ranking\official_projects.json', 'r', encoding='utf-8') as f:
    projs = json.load(f)

# Keep all non-Noyanlar projects
other_projs = [p for p in projs if p['developer_name'] != 'Noyanlar Group']

# Define the exact 9 Noyanlar projects requested by user
noyanlar_9 = [
    {
        "id": "noy_ocean_life",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Ocean Life Residence",
        "region": "İskele / Long Beach",
        "type": "Курортный комплекс у моря в стиле античного Саламиса (21 блок)",
        "price_from": "£89,000",
        "features": [
            "21 блок, видовые апартаменты и роскошные террасы",
            "Огромные лагунные бассейны, аквапарк и спа-центр",
            "5 минут пешком до золотых песков Long Beach"
        ],
        "coords": [35.2860, 33.9020],
        "image": "https://noyanlar.com/wp-content/uploads/2026/05/Ocean-Life-27.jpg",
        "url": "https://noyanlar.com/projects/ocean-life-residence/"
    },
    {
        "id": "noy_olea",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Olea Residence",
        "region": "Geçitkale / Gazimağusa",
        "type": "Эко-резиденция среди оливковых рощ с развитой инфраструктурой",
        "price_from": "£75,000",
        "features": [
            "Спокойная загородная жизнь в окружении реликтовых олив",
            "Высокий арендный и инвестиционный потенциал района Гечиткале",
            "Современная эко-инфраструктура, бассейны и зоны отдыха"
        ],
        "coords": [35.2600, 33.7480],
        "image": "https://noyanlar.com/wp-content/uploads/2026/08/olea_exterior.jpg",
        "url": "https://noyanlar.com/projects/olea-residence/"
    },
    {
        "id": "noy_sea_breeze",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Sea Breeze",
        "region": "İskele / Long Beach",
        "type": "Прибрежный жилой комплекс повышенного комфорта у моря",
        "price_from": "£84,000",
        "features": [
            "Непосредственная близость к морскому побережью Long Beach",
            "Панорамное остекление, просторные балконы и террасы",
            "Развитая внутренняя инфраструктура и ландшафтные сады"
        ],
        "coords": [35.2890, 33.9070],
        "image": "https://noyanlar.com/wp-content/uploads/2026/08/sea_breeze_exterior.jpg",
        "url": "https://noyanlar.com/projects/sea_breeze/"
    },
    {
        "id": "noy_the_blue",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "The Blue Residence",
        "region": "İskele Merkez",
        "type": "Городской курортный комплекс апартаментов в центре Искеле",
        "price_from": "£78,000",
        "features": [
            "Шаговая доступность набережной и всей городской инфраструктуры",
            "Закрытая охраняемая территория с бассейном и зонами отдыха",
            "Идеальный баланс курортного проживания и круглогодичной жизни"
        ],
        "coords": [35.2850, 33.8980],
        "image": "https://noyanlar.com/wp-content/uploads/2026/09/blue_exterior-2.jpg",
        "url": "https://noyanlar.com/projects/the_blue_residence/"
    },
    {
        "id": "noy_four_seasons_3",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Four Seasons Life III",
        "region": "İskele / Boğaz",
        "type": "Морской курортный резорт премиум-класса с приватным пляжем",
        "price_from": "£125,000",
        "features": [
            "Первая береговая линия со своим приватным песчаным пляжем",
            "Пляжные клубы, рестораны на набережной и водные виды спорта",
            "Премиальная отделка и видовые террасы на залив Боаз"
        ],
        "coords": [35.3180, 33.9390],
        "image": "https://noyanlar.com/wp-content/uploads/2026/08/four_seasons_exterior.jpg",
        "url": "https://noyanlar.com/projects/four_seasons_3/"
    },
    {
        "id": "noy_la_palazzo",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "La Palazzo",
        "region": "İskele / Boğaz",
        "type": "Дворцовые приватные виллы неоклассической архитектуры",
        "price_from": "£380,000",
        "features": [
            "Эксклюзивные отдельно стоящие виллы с личными бассейнами",
            "Итальянский мрамор, высокие потолки и приватные сады",
            "Закрытый клубный поселок для респектабельной приватной жизни"
        ],
        "coords": [35.2810, 33.9050],
        "image": "https://noyanlar.com/wp-content/uploads/2026/05/la_plazzo-1.jpeg",
        "url": "https://noyanlar.com/projects/la_palazzo/"
    },
    {
        "id": "noy_solmaris",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Solmaris",
        "region": "İskele / Boğaz",
        "type": "Современный жилой комплекс по соседству с мариной Боаз",
        "price_from": "£110,000",
        "features": [
            "Соседство с живописной гаванью яхт и рыбными ресторанами",
            "Ландшафтный дизайн, зоны барбекю и открытые релакс-бассейны",
            "Гармония лазурного моря и нетронутой природы Средиземноморья"
        ],
        "coords": [35.3140, 33.9320],
        "image": "https://noyanlar.com/wp-content/uploads/2026/08/solmaris_exterior.jpg",
        "url": "https://noyanlar.com/projects/solmaris/"
    },
    {
        "id": "noy_sky_diora",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Sky Diora",
        "region": "Karpaz / Yeni Erenköy",
        "type": "Бутик-резиденция с панорамой моря рядом с Karpaz Gate Marina",
        "price_from": "£95,000",
        "features": [
            "Экологически чистый заповедный полуостров Карпас",
            "В считанных минутах от международной яхтенной марины Karpaz Gate",
            "Панорамный вид на море, чистейшие дикие пляжи и приватность"
        ],
        "coords": [35.5350, 34.1950],
        "image": "https://noyanlar.com/wp-content/uploads/2026/08/sky_diora_exterior.jpg",
        "url": "https://noyanlar.com/projects/sky_diora/"
    },
    {
        "id": "noy_terra_life",
        "developer_id": "noyanlar",
        "developer_name": "Noyanlar Group",
        "name": "Terra Life",
        "region": "İskele / Long Beach",
        "type": "Эко-комплекс с приватными патио и садами у побережья",
        "price_from": "£82,000",
        "features": [
            "Отличная транспортная доступность, близость к морю и набережной",
            "Зеленая парковая территория, открытые бассейны и спортивные зоны",
            "Высокая ликвидность для долгосрочной и сезонной курортной аренды"
        ],
        "coords": [35.2870, 33.9030],
        "image": "https://noyanlar.com/wp-content/uploads/2026/08/Kapak.jpg",
        "url": "https://noyanlar.com/projects/terra_life/"
    }
]

# Insert Noyanlar in rank order:
# 1. Döveç (6)
# 2. NorthernLAND (6)
# 3. Özyalçın (3)
# 4. Carrington (8)
# 5. Noyanlar (9)
# 6. Cyprus Constructions (5)

dovec = [p for p in other_projs if p['developer_name'] == 'Döveç Group']
northernland = [p for p in other_projs if p['developer_name'] == 'NorthernLAND']
ozyalcin = [p for p in other_projs if p['developer_name'] == 'Özyalçın Construction']
carrington = [p for p in other_projs if p['developer_name'] == 'Carrington Group']
cc = [p for p in other_projs if p['developer_name'] == 'Cyprus Constructions']

all_projs = dovec + northernland + ozyalcin + carrington + noyanlar_9 + cc

print(f"Total projects assembled: {len(all_projs)}")
print(f"  Döveç Group: {len(dovec)}")
print(f"  NorthernLAND: {len(northernland)}")
print(f"  Özyalçın: {len(ozyalcin)}")
print(f"  Carrington: {len(carrington)}")
print(f"  Noyanlar Group: {len(noyanlar_9)}")
print(f"  Cyprus Constructions: {len(cc)}")

# Write to official_projects.json
with open(r'd:\Qoder\ai_developer_ranking\official_projects.json', 'w', encoding='utf-8') as f:
    json.dump(all_projs, f, ensure_ascii=False, indent=2)

# Write to projects_data.js
js_content = "window.OFFICIAL_PROJECTS = " + json.dumps(all_projs, ensure_ascii=False, indent=2) + ";\n"
with open(r'd:\Qoder\ai_developer_ranking\projects_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Copy to dist
dist_dir = r'd:\Qoder\ai_developer_ranking\dist'
if not os.path.exists(dist_dir):
    os.makedirs(dist_dir)

with open(os.path.join(dist_dir, 'official_projects.json'), 'w', encoding='utf-8') as f:
    json.dump(all_projs, f, ensure_ascii=False, indent=2)

with open(os.path.join(dist_dir, 'projects_data.js'), 'w', encoding='utf-8') as f:
    f.write(js_content)

shutil.copy2(r'd:\Qoder\ai_developer_ranking\index.html', os.path.join(dist_dir, 'index.html'))

print("Updated official_projects.json, projects_data.js, and synced to dist/!")
