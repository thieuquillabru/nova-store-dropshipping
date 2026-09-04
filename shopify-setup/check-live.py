import urllib.request
import re

req = urllib.request.Request('https://pfd2zx-7h.myshopify.com/', headers={
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'User-Agent': 'Mozilla/5.0'
})
resp = urllib.request.urlopen(req, timeout=15)
html = resp.read().decode('utf-8', errors='ignore')

print('STATUS:', resp.status)
print('LONGUEUR:', len(html), 'chars')
print('---')
print('HAS_LIQUID_GLASS:', 'liquid-glass' in html)
print('HAS_GLASS_BG:', 'backdrop-filter' in html)
print('HAS_RITUAL:', 'Ritual' in html.lower() or 'ritual' in html.lower())
print('HAS_ORIGIN:', 'Origin' in html)
print('---')

# Chercher le nom du thème
theme_match = re.search(r'"theme"\s*:\s*"([^"]+)"', html)
if theme_match:
    print('THEME_NAME:', theme_match.group(1))

# Chercher les fichiers CSS
css_matches = re.findall(r'<link[^>]*href="([^"]+\.css[^"]*)"', html)
print('---')
print('CSS_FILES:')
for css in css_matches[:10]:
    print(' ', css[:100])

# Chercher les produits
print('---')
print('HAS_PRODUITS:', 'Clavier' in html or 'T-shirt' in html or 'Nouveaut' in html)
print('HAS_CHIMES:', 'chimes' in html.lower())
print('HAS_CONTROLLER:', 'controller' in html.lower())
print('HAS_STREET:', 'street' in html.lower())