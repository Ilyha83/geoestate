# -*- coding: utf-8 -*-
import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def check_url(name, url):
    print(f"\n=== Checking {name}: {url} ===")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            print(f"Status: {r.status}, Length: {len(html)}")
            return html
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

# 1. DOVEC
dovec_html = check_url("Dovec", "https://www.dovecgroup.com/ru/projects")
if dovec_html:
    # Find all project cards and images
    s3_matches = list(set(re.findall(r'https://dovec-site-assets\.s3[^\s"\'<>)]+', dovec_html)))
    print("Dovec S3 links found:")
    for m in s3_matches:
        if 'cover' in m or 'project' in m or 'cms' in m:
            print("  ", m)

# 2. NORTHERNLAND
nl_html = check_url("NorthernLAND", "https://northernland.com/ru/projects/")
if nl_html:
    nl_imgs = list(set(re.findall(r'https://northernland\.com/storage/[^\s"\'<>)]+', nl_html)))
    print("NorthernLAND images found:")
    for m in nl_imgs[:15]:
        print("  ", m)

# 3. NOYANLAR
noyan_html = check_url("Noyanlar", "https://www.noyanlar.com/ru/projects")
if noyan_html:
    n_imgs = list(set(re.findall(r'https?://[^\s"\'<>)]+noyanlar[^\s"\'<>)]+\.(?:jpg|png|webp)', noyan_html, re.I)))
    print("Noyanlar images found:")
    for m in n_imgs[:15]:
        print("  ", m)

# 4. CARRINGTON
carr_html = check_url("Carrington", "https://carringtongroup.com/projects/")
if carr_html:
    c_imgs = list(set(re.findall(r'https?://carringtongroup\.com/wp-content/[^\s"\'<>)]+\.(?:jpg|png|webp)', carr_html, re.I)))
    print("Carrington images found:")
    for m in c_imgs[:15]:
        print("  ", m)
