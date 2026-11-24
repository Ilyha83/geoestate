# -*- coding: utf-8 -*-
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def probe(name, url):
    print(f"\n--- {name}: {url} ---")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            print("Status:", r.status)
            return html
    except Exception as e:
        print("Error:", e)
        return ""

# Carrington
h_carr = probe("Carrington", "https://carringtongroup.com/")
if h_carr:
    for m in set(re.findall(r'href=[\"\']([^\"\']*(?:project|marina|magic|poseidon|residence)[^\"\']*)[\"\']', h_carr, re.I)):
        print("Carr link:", m)

# Ozyalcin
h_oz = probe("Ozyalcin", "https://ozyalcinconstruction.com/")
if not h_oz:
    h_oz = probe("Ozyalcin Alt", "https://www.ozyalcinconstruction.com/")
if h_oz:
    for m in set(re.findall(r'href=[\"\']([^\"\']*(?:project|projeler|195|casa|residence)[^\"\']*)[\"\']', h_oz, re.I)):
        print("Oz link:", m)

# Cyprus Constructions ongoing
h_cc = probe("CC", "https://cyprusconstructions.com/")
if h_cc:
    for m in set(re.findall(r'href=[\"\'](/en/[^\"\']+)[\"\']', h_cc)):
        print("CC link:", m)
