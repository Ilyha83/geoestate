# -*- coding: utf-8 -*-
import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

# 1. Cyprus Constructions
try:
    req = urllib.request.Request('https://cyprus-constructions.com/projects/', headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
        h = r.read().decode('utf-8', errors='ignore')
        for img in set(re.findall(r'https?://[^\s"\'<>)]+\.(?:jpg|png|webp)', h)):
            if 'maldives' in img.lower() or 'mykonos' in img.lower() or 'phuket' in img.lower() or 'idyll' in img.lower():
                print("CC:", img)
except Exception as e:
    print("CC error:", e)

# 2. Carrington
try:
    req2 = urllib.request.Request('https://carringtongroup.com/', headers=headers)
    with urllib.request.urlopen(req2, context=ctx, timeout=10) as r:
        h2 = r.read().decode('utf-8', errors='ignore')
        for img in set(re.findall(r'https?://[^\s"\'<>)]+\.(?:jpg|png|webp)', h2)):
            if 'marina' in img.lower() or 'sea-magic' in img.lower() or 'poseidon' in img.lower():
                print("Carrington:", img)
except Exception as e:
    print("Carrington error:", e)
