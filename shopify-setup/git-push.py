import os
import subprocess

cwd = os.path.join(os.path.expanduser('~'), '.cline', 'data', 'workspaces', 'chat')
os.chdir(cwd)

# Configure git
subprocess.run(['git', 'config', 'user.email', 'thieuquilla@gmail.com'])
subprocess.run(['git', 'config', 'user.name', 'thieuquilla'])

# Create .gitignore
gitignore_content = """# Dependencies
node_modules/
__pycache__/
*.pyc

# Environment
.env
.env.local

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Logs
*.log
"""

with open('.gitignore', 'w') as f:
    f.write(gitignore_content)

# Add all files
result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
print('ADD:', result.returncode, result.stdout[:200] if result.stdout else '', result.stderr[:200] if result.stderr else '')

# Commit
commit_msg = """feat: Business Model complet Nova Store Dropshipping

- Business Model A à Z
- Documentation dropshipping Shopify x AliExpress
- Shopify theme files (Origin modifié)
- Glassmorphism CSS style iOS 26
- Produits fictifs configurés
- Collection Nouveautés

Created: 2026-01-05"""

result = subprocess.run(['git', 'commit', '-m', commit_msg], capture_output=True, text=True)
print('COMMIT:', result.returncode, result.stdout[:300] if result.stdout else '', result.stderr[:300] if result.stderr else '')

print('DONE')
