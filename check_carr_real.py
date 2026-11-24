# -*- coding: utf-8 -*-
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

# Check Carrington actual site
for host in ['https://www.carringtonholidays.com/', 'https://carringtonwealth.com/', 'https://www.carringtongroup.com/']:
    try:
        req = urllib.request.Request(host, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            print(host, r.status)
            for m in re.findall(r'https?://[^\s\"\'<>)]+\.(?:jpg|png|webp)', html):
                if any(k in m.lower() for k in ['marina', 'poseidon', 'magic', 'project', 'carrington']):
                    print("  ", m)
    except Exception as e:
        print(host, e)
