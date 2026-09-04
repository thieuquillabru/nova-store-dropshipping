import os
import subprocess

cwd = os.path.join(os.path.expanduser('~'), '.cline', 'data', 'workspaces', 'chat')
os.chdir(cwd)

# Set branch to main
subprocess.run(['git', 'branch', '-M', 'main'])

# Push to GitHub
result = subprocess.run(
    ['git', 'push', '-u', 'origin', 'main'],
    capture_output=True,
    text=True,
    timeout=120
)

print('PUSH_EXIT:', result.returncode)
if result.stdout:
    print('STDOUT:', result.stdout[:500])
if result.stderr:
    print('STDERR:', result.stderr[:500])

if result.returncode == 0:
    print('SUCCESS: Pushed to https://github.com/thieuquillabru/nova-store-dropshipping')
else:
    print('FAILED')
