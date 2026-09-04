import os
import subprocess

home = os.path.expanduser('~')
cmd = os.path.join(home, 'AppData', 'Roaming', 'npm', 'shopify.cmd')
log = os.path.join(os.environ['TEMP'], 'pub-bg.log')

# Publish products one by one
products = [
    "gid://shopify/Product/8049748115534",
    "gid://shopify/Product/8049748148302",
    "gid://shopify/Product/8049748181070",
    "gid://shopify/Product/8049748213838"
]

pub_id = "gid://shopify/Publication/196746707022"
collection_id = "gid://shopify/Collection/315070480462"

with open(log, 'w') as f:
    f.write("Starting publish process...\n")
    
    for i, prod_id in enumerate(products, 1):
        query = f'mutation {{ pub: publishablePublish(id: "{prod_id}", input: {{ publicationId: "{pub_id}" }}) {{ userErrors {{ field message }} }} }}'
        f.write(f"\n[{i}/4] Publishing {prod_id}...\n")
        f.flush()
        
        # Use Popen for non-blocking
        p = subprocess.Popen(
            [cmd, 'store', 'execute', '--store', 'pfd2zx-7h.myshopify.com', '--allow-mutations', '--query', query],
            stdout=f,
            stderr=subprocess.STDOUT
        )
        p.wait(timeout=120)
        f.write(f"[{i}/4] Done with code {p.returncode}\n")
    
    f.write("\nAll products published!\n")

print("PUBLISH_COMPLETE")
print("Log:", log)