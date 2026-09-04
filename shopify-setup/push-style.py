import os
import subprocess

cwd = os.path.join(os.path.expanduser('~'), '.cline', 'data', 'workspaces', 'chat')
os.chdir(cwd)

# Git operations
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'docs: Analyse approfondie des styles UI/UX\n\n- Chimes: Editorial minimaliste, beige/brun, JetBrains Mono\n- Controller-site: Premium dark glass, or/dore, Archivo/Inter\n- Street-flavor: Fun/pop, Bagel Fat One, Poppins\n\nSynthese et variables CSS recommandees pour Nova Store'])
result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True, timeout=120)
print('PUSH:', result.returncode)