import os
import subprocess

cwd = os.path.join(os.path.expanduser('~'), '.cline', 'data', 'workspaces', 'chat')
os.chdir(cwd)

# Write analysis
analysis_path = os.path.join(cwd, 'docs', 'TEMPLATE_ANALYSIS.md')
with open(analysis_path, 'w', encoding='utf-8') as f:
    f.write("""# Analyse des Templates de Reference

## Chimes - Simulation Physique Interactive
- Canvas 2D + Integration Verlet
- TweakPane pour controle temps reel
- Design system CSS complet
- Lazy loading JS avec import() dynamique

## Controller-site - Showcase Produit 3D
- Three.js + GLTF + Draco compression
- WebAssembly pour decoding haute perf
- Bundle JS/CSS separes
- Photos WebP optimisees

## Street-favor - Site Vitrine Alimentaire
- Design minimaliste et premium
- Typographie forte
- Structure semantique SEO
- Approach mobile-first

## Plan d'Action Nova Store
1. Design minimaliste (street-flavor)
2. Animations interactives (chimes)
3. Showcase produits 3D si applicable (controller-site)

Analyse cree le 5 janvier 2026
""")

print("Analysis written")

# Git operations
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'docs: Analyse des 3 templates de reference'])
result = subprocess.run(['git', 'push', '-u', 'origin', 'main'], capture_output=True, text=True, timeout=120)
print('PUSH:', result.returncode)