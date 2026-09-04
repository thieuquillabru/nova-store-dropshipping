import urllib.request
import re

url = 'https://thieuquillabru.github.io/gear-up/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req, timeout=15)
html = resp.read().decode('utf-8', errors='ignore')

print('STATUS:', resp.status)
print('SIZE:', len(html), 'chars')
print('='*70)

# Extract CSS links
css_links = re.findall(r'<link[^>]*href="([^"]*\.css[^"]*)"', html)
print('CSS FILES:')
for css in css_links:
    print(' ', css)

# Extract style blocks
style_blocks = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
print('STYLE BLOCKS:', len(style_blocks))
for i, block in enumerate(style_blocks):
    print(f'\n--- Style Block {i+1} ({len(block)} chars) ---')
    print(block[:2000])

# Extract header/nav structure
header_match = re.search(r'<header[^>]*>(.*?)</header>', html, re.DOTALL)
if header_match:
    print('\n--- HEADER ---')
    print(header_match.group(1)[:3000])

# Extract nav
nav_match = re.search(r'<nav[^>]*>(.*?)</nav>', html, re.DOTALL)
if nav_match:
    print('\n--- NAV ---')
    print(nav_match.group(1)[:2000])

# Save full HTML
with open('gear-up-source.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('\n\nFull HTML saved to gear-up-source.html')