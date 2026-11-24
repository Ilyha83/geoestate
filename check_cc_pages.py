# -*- coding: utf-8 -*-
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request('https://cyprus-constructions.com/', headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
    html = r.read().decode('utf-8', errors='ignore')
    for m in set(re.findall(r'href=[\"\']([^\"\']*(?:project|residence|maldives|phuket|mykonos|idyll|bahamas)[^\"\']*)[\"\']', html, re.I)):
        print("Link:", m)
    for m in set(re.findall(r'https?://cyprus-constructions\.com/[^\s"\'<>]+\.(?:jpg|png|webp)', html)):
        print("Img:", m)
