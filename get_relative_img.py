# -*- coding: utf-8 -*-
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request('https://cyprusconstructions.com/en/maldives_homes', headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
    html = r.read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', html)
    for i in set(imgs):
        print("IMG:", i)
