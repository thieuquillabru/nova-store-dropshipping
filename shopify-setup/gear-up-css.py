import urllib.request
import os

base_url = 'https://thieuquillabru.github.io/gear-up/'
css_files = ['./fonts/fonts.css', './css/app.css', './css/custom.css']

save_dir = os.path.join(os.path.expanduser('~'), '.cline', 'data', 'workspaces', 'chat', 'gear-up-css')
os.makedirs(save_dir, exist_ok=True)

for css_file in css_files:
    url = base_url + css_file
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=15)
        content = resp.read().decode('utf-8', errors='ignore')
        
        save_path = os.path.join(save_dir, css_file.replace('/', '_'))
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'Downloaded: {css_file} ({len(content)} chars)')
    except Exception as e:
        print(f'Error: {css_file} - {e}')

# Also download the full HTML
req = urllib.request.Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req, timeout=15)
html = resp.read().decode('utf-8', errors='ignore')

with open(os.path.join(save_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Downloaded index.html ({len(html)} chars)')