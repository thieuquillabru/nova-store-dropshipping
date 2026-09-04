import os
import subprocess

cwd = os.path.join(os.path.expanduser('~'), '.cline', 'data', 'workspaces', 'chat')
os.chdir(cwd)

subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'docs: Analyse complete des animations et effets\n\n- Chimes: physique Verlet, transitions, audio Web Audio API\n- Controller-site: Three.js, GLTF, scroll-driven, glassmorphism\n- Street-flavor: parallax, float, slideUp, crossfade\n\nSynthese et checklist pour Nova Store'])
result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True, timeout=120)
print('PUSH:', result.returncode)