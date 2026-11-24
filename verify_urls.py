# -*- coding: utf-8 -*-
import urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

urls = [
    # DOVEC (S3)
    "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/querencia/cover.jpg",
    "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/courtyardplatinum/exterior/2023-09-05-courtyard-platinum-4.jpg",
    "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/laisla/cover.jpg",
    "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/fourseasonslife3/cover.jpg",
    "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/natulux/featured-card/natulux-featured-0e1597b1.jpg",
    "https://dovec-site-assets.s3.eu-north-1.amazonaws.com/cms/projects/lacasalia/featured-card/la-casalia-features-bcf7ee80.jpg",

    # NORTHERNLAND (CDN)
    "https://northernland.com/storage/spot/63/the-biggest-project-of-northern-cyprus.webp",
    "https://northernland.com/storage/spot/243/sun-bathed-life-casa-del-mare.webp",
    "https://northernland.com/storage/gallery/150/northernland-premier_1670413286.webp",
    "https://northernland.com/storage/spot/270/the-beach-pool.webp",
    "https://northernland.com/storage/gallery/154/56-palms.webp",

    # NOYANLAR (CDN)
    "https://noyanlar.com/wp-content/uploads/2026/11/noyanlar-2026-11-ocean-life-aqua-park-768x432.webp",
    "https://noyanlar.com/wp-content/uploads/2026/05/royalsun_elite_exterior-1-1536x1024.jpg",
    "https://noyanlar.com/wp-content/uploads/2026/11/noyanlar-2026-11-bellagio-rezidence-1024x576.webp",
    "https://noyanlar.com/wp-content/uploads/2026/11/noyanlar-2026-11-miracle-villa-havuz.webp",
    "https://noyanlar.com/wp-content/uploads/2026/09/park_residence_exterior-6-300x169.jpg"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
            print(f"OK ({r.status}) -> {u.split('/')[-1]}")
    except Exception as e:
        print(f"FAILED -> {u}: {e}")
