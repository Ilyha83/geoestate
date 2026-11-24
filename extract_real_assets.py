# -*- coding: utf-8 -*-
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# 1. Carrington project links
req = urllib.request.Request("https://carringtongroup.com/projects/", headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
        html = r.read().decode('utf-8', errors='ignore')
        print("Carrington links:")
        for m in set(re.findall(r'href=[\"\'](https?://carringtongroup\.com/[^\"\']+)[\"\']', html)):
            if any(k in m for k in ['marina', 'magic', 'poseidon', 'suncity', 'project', 'olive']):
                print(" ", m)
        for img in set(re.findall(r'https?://carringtongroup\.com/wp-content/uploads/[^\s\"\'<>)]+\.(?:jpg|jpeg|png|webp)', html)):
            print("  Carr Img:", img)
except Exception as e:
    print("Carr err:", e)

# 2. Ozyalcin images
for p in ['zenith-by-ozyalcin', 'casa-oliva-2-by-ozyalcin', 'solea']:
    url = f"https://ozyalcinconstruction.com/projeler/{p}/"
    req2 = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req2, context=ctx, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https?://ozyalcinconstruction\.com/wp-content/uploads/[^\s\"\'<>)]+\.(?:jpg|jpeg|png|webp)', html)
            print(f"\nOzyalcin {p}:")
            for img in set(imgs)[:3]:
                print(" ", img)
    except Exception as e:
        print(f"Ozyalcin {p} err:", e)

# 3. CC projects
for p in ['Bahamas_homes', 'Hawaii_homes', 'mykonos_homes']:
    url = f"https://cyprusconstructions.com/en/{p}"
    req3 = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req3, context=ctx, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', html)
            print(f"\nCC {p}:")
            for img in set(imgs):
                if any(k in img.lower() for k in ['detailpage', 'home', 'bg', 'banner']):
                    print(" ", img)
    except Exception as e:
        print(f"CC {p} err:", e)
