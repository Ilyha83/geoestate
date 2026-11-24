# -*- coding: utf-8 -*-
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

for url in ['https://cyprus-constructions.com/', 'https://www.cyprus-constructions.com/']:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            print("Status:", r.status)
            for m in re.findall(r'https?://[^\s"\'<>)]+\.(?:jpg|jpeg|png|webp)', html):
                if any(k in m.lower() for k in ['maldives', 'mykonos', 'phuket', 'idyll', 'project', 'slider']):
                    print("  Match:", m)
    except Exception as e:
        print(url, e)
