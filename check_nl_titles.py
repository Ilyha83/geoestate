# -*- coding: utf-8 -*-
import urllib.request, re, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request('https://northernland.com/en/projects/', headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')
    # Find all project names
    matches = re.findall(r'<h[2345][^>]*>(.*?)</h[2345]>', html, re.I)
    for m in matches:
        clean = re.sub(r'<[^>]+>', '', m).strip()
        if len(clean) > 2:
            print("Project title:", clean)
