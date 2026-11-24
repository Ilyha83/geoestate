# -*- coding: utf-8 -*-
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

for u in ['https://cyprusconstructions.com/', 'https://www.cyprusconstructions.com/']:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            print(u, r.status)
            for m in set(re.findall(r'https?://[^\s"\'<>)]+\.(?:jpg|png|webp)', html)):
                if 'maldives' in m.lower():
                    print("  Maldives:", m)
    except Exception as e:
        print(u, e)
