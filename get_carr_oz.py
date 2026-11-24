# -*- coding: utf-8 -*-
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

# 1. Ozyalcin images
for p in ['zenith-by-ozyalcin', 'casa-oliva-2-by-ozyalcin', 'solea']:
    url = f"https://ozyalcinconstruction.com/projeler/{p}/"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            imgs = list(set(re.findall(r'https?://ozyalcinconstruction\.com/wp-content/uploads/[^\s\"\'<>)]+\.(?:jpg|jpeg|png|webp)', html)))
            print(f"\nOzyalcin {p}:")
            for img in imgs[:5]:
                print(" ", img)
    except Exception as e:
        print(f"Ozyalcin {p} err:", e)

# 2. Carrington projects page
u_carr = "https://carringtongroup.com/"
req_c = urllib.request.Request(u_carr, headers=headers)
try:
    with urllib.request.urlopen(req_c, context=ctx, timeout=8) as r:
        html = r.read().decode('utf-8', errors='ignore')
        imgs = list(set(re.findall(r'https?://carringtongroup\.com/wp-content/uploads/[^\s\"\'<>)]+\.(?:jpg|jpeg|png|webp)', html)))
        print(f"\nCarrington home images:")
        for img in imgs[:10]:
            print(" ", img)
except Exception as e:
    print("Carr err:", e)
