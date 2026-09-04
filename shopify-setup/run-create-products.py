import os
import subprocess

home = os.path.join(os.path.expanduser('~'))
cmd = os.path.join(home, 'AppData', 'Roaming', 'npm', 'shopify.cmd')
query_file = os.path.join(home, '.cline', 'data', 'workspaces', 'chat', 'shopify-setup', 'create-tech-products.graphql')
log_file = os.path.join(os.environ['TEMP'], 'create-tech-products.log')

with open(log_file, 'w') as f:
    result = subprocess.run(
        [cmd, 'store', 'execute', '--store', 'pfd2zx-7h.myshopify.com', '--allow-mutations', '--query-file', query_file],
        stdout=f,
        stderr=subprocess.STDOUT,
        timeout=120
    )

print('EXIT_CODE:', result.returncode)
print('LOG:', log_file)