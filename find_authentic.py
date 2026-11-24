# -*- coding: utf-8 -*-
import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error {url}: {e}")
        return ""

# 1. DOVEC
h = fetch('https://www.dovecgroup.com/ru/projects')
print("--- DOVEC PROJECTS ---")
for m in set(re.findall(r'href=["\'](/ru/projects/[^"\']+)["\']', h)):
    print("Project link:", m)

for m in set(re.findall(r'https://dovec-site-assets\.s3[^\s"\'<>)]+', h)):
    print("S3 img:", m)

# 2. NORTHERNLAND
h_nl = fetch('https://northernland.com/en/projects/')
print("\n--- NORTHERNLAND PROJECTS ---")
for m in set(re.findall(r'href=["\'](https://northernland\.com/en/projects/[^"\']+)["\']', h_nl)):
    print("NL Project link:", m)
for m in set(re.findall(r'https://northernland\.com/storage/[^\s"\'<>)]+\.webp', h_nl)):
    print("NL img:", m)

# 3. NOYANLAR
h_noyan = fetch('https://www.noyanlar.com/en/projects')
print("\n--- NOYANLAR PROJECTS ---")
for m in set(re.findall(r'href=["\'](/en/projects/[^"\']+)["\']', h_noyan)):
    print("Noyanlar Project link:", m)
