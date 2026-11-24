# -*- coding: utf-8 -*-
import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

def get_images(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'https?://[^\s"\'<>)]+\.(?:jpg|jpeg|png|webp)', html)
            # Filter relevant
            good = [i for i in imgs if 'wp-content/uploads' in i and ('project' in i or 'residence' in i or 'banner' in i or 'slider' in i or 'ocean' in i or 'park' in i or 'bellagio' in i or 'miracle' in i or 'royal' in i)]
            return good
    except Exception as e:
        print(f"Error {url}: {e}")
        return []

for p in ['ocean-life-residence', 'park-residence', 'royalsun_elite_residence', 'bellagio', 'miracle_villa_residence']:
    u = f'https://noyanlar.com/projects/{p}/'
    imgs = get_images(u)
    print(f"\n--- {p} ---")
    for img in list(set(imgs))[:4]:
        print("  ", img)
