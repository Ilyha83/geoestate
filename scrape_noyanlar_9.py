# -*- coding: utf-8 -*-
import urllib.request, ssl, re, json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

urls = [
    ("Ocean Life Residence", "https://noyanlar.com/projects/ocean-life-residence/"),
    ("Olea Residence", "https://noyanlar.com/projects/olea-residence/"),
    ("Sea Breeze", "https://noyanlar.com/projects/sea_breeze/"),
    ("The Blue Residence", "https://noyanlar.com/projects/the_blue_residence/"),
    ("Four Seasons Life III", "https://noyanlar.com/projects/four_seasons_3/"),
    ("La Palazzo", "https://noyanlar.com/projects/la_palazzo/"),
    ("Solmaris", "https://noyanlar.com/projects/solmaris/"),
    ("Sky Diora", "https://noyanlar.com/projects/sky_diora/"),
    ("Terra Life", "https://noyanlar.com/projects/terra_life/")
]

results = []

for name, u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            body = r.read().decode('utf-8', errors='ignore')
            print(f"\n=== {name} (HTTP {r.status}, len {len(body)}) ===")
            
            # H1 or title
            h1 = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.DOTALL)
            h1_txt = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else name
            print("  Title:", h1_txt)
            
            # Prices
            prices = re.findall(r'£\s*[\d,]+', body)
            price_from = prices[0] if prices else ""
            print("  Prices found:", list(set(prices))[:3])
            
            # Images
            imgs = re.findall(r'https?://noyanlar\.com/wp-content/uploads/[^\s\"\'<>)]+\.(?:jpg|jpeg|png|webp)', body)
            filtered_imgs = [i for i in imgs if not any(x in i.lower() for x in ['logo', 'icon', 'flag', 'arrow', 'user', 'banner', 'footer', 'avatar', 'thumb'])]
            print(f"  Images ({len(filtered_imgs)}):")
            for im in filtered_imgs[:3]:
                print("   ", im)
                
            # Check coordinates or location
            coords = re.findall(r'([34][0-9]\.[0-9]{3,})[,\s]+([34][0-9]\.[0-9]{3,})', body)
            print("  Coords found:", coords[:2])
            
            # Features / bullets
            bullets = re.findall(r'<li[^>]*>(.*?)</li>', body, re.DOTALL)
            clean_b = [re.sub(r'<[^>]+>', '', b).strip() for b in bullets if len(re.sub(r'<[^>]+>', '', b).strip()) > 10 and not any(k in b for k in ['WhatsApp', 'Главная', 'Projects', 'Menu', 'Privacy'])]
            print(f"  Bullets ({len(clean_b)}):", clean_b[:3])
            
            results.append({
                'name': name,
                'h1': h1_txt,
                'url': u,
                'price': price_from,
                'image': filtered_imgs[0] if filtered_imgs else '',
                'all_images': filtered_imgs[:5],
                'coords': coords[0] if coords else None,
                'bullets': clean_b[:5]
            })
    except Exception as e:
        print(f"Error {name}: {e}")

with open(r'd:\Qoder\ai_developer_ranking\noyanlar_9_scraped.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
