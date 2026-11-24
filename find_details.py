# -*- coding: utf-8 -*-
import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

def fetch(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error {url}: {e}")
        return ""

# 1. DOVEC Courtyard
h_court = fetch('https://www.dovecgroup.com/ru/projects/courtyard-platinum')
print("Courtyard Platinum S3 imgs:")
for m in set(re.findall(r'https://dovec-site-assets\.s3[^\s"\'<>)]+', h_court)):
    if 'cover' in m or 'hero' in m or 'featured' in m or 'courtyard' in m.lower():
        print("  ", m)

# 2. NOYANLAR (check homepage to find projects link)
h_noy = fetch('https://www.noyanlar.com/')
print("\nNoyanlar links:")
for m in set(re.findall(r'href=["\']([^"\']*(?:project|residence|ocean|bellagio|royal)[^"\']*)["\']', h_noy, re.I)):
    print("  ", m)

# 3. CARRINGTON (check their actual site)
h_carr = fetch('https://www.carringtongroup.com/')
print("\nCarrington links & images:")
for m in set(re.findall(r'https?://(?:www\.)?carringtongroup\.com/wp-content/uploads/[^\s"\'<>)]+\.(?:jpg|png|webp)', h_carr, re.I)):
    print("  ", m)
