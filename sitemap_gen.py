import os 

def generate_sitemap(directory):
    urls = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(('.html', '.md', '.css', '.js', '.png', '.gif', '.webp', '.jpg', '.jpeg', '.txt', '.ttf')):
                path = os.path.join(dirpath, filename)
                url = path.replace(directory, '').replace('\\', '/')
                urls.append(f"  <url><loc>https://sctech.mooo.com/{url}</loc></url>")
    return "\n".join(urls)

sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap-image/1.1">
""" + generate_sitemap('./') + "\n</urlset>"

with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
