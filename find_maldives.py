# -*- coding: utf-8 -*-
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

# Search for real Maldives Homes photos
urls = [
    'https://cyprus-constructions.com/rehber/luxury-resort-style-residences-architecture-master-planning-e6sr',
    'https://cyprus-constructions.com/rehber/luxury-resort-style-residences-architecture-master-planning-mtmb'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            for img in set(re.findall(r'https?://[^\s"\'<>)]+\.(?:jpg|jpeg|png|webp)', html)):
                if not any(k in img.lower() for k in ['logo', 'icon', 'slider-8']):
                    print("Found:", img)
    except Exception as e:
        print(f"Error {u}: {e}")
