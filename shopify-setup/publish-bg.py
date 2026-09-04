import os
import subprocess
import time

home = os.path.expanduser('~')
cmd = os.path.join(home, 'AppData', 'Roaming', 'npm', 'shopify.cmd')
log = os.path.join(os.environ['TEMP'], 'publish-final.log')

products = [
    "gid://shopify/Product/8049748115534",
    "gid://shopify/Product/8049748148302",
    "gid://shopify/Product/8049748181070",
    "gid://shopify/Product/8049748213838"
]

pub_id = "gid://shopify/Publication/196746707022"
collection_id = "gid://shopify/Collection/315070480462"

with open(log, 'w') as f:
    f.write("Nova Store - Publishing Tech Products\n")
    f.write("=" * 50 + "\n\n")
    
    # Publish each product
    for i, prod_id in enumerate(products, 1):
        title = ["Clavier RGB", "Souris Sans Fil", "Support Laptop", "Hub USB-C"][i-1]
        query = f'mutation {{ pub: publishablePublish(id: "{prod_id}", input: {{ publicationId: "{pub_id}" }}) {{ userErrors {{ field message }} }} }}'
        
        f.write(f"[{i}/4] Publishing: {title}\n")
        f.flush()
        
        p = subprocess.Popen(
            [cmd, 'store', 'execute', '--store', 'pfd2zx-7h.myshopify.com', '--allow-mutations', '--query', query],
            stdout=f,
            stderr=subprocess.STDOUT
        )
        
        try:
            p.wait(timeout=180)
            f.write(f"[{i}/4] Published! (code: {p.returncode})\n\n")
        except subprocess.TimeoutExpired:
            f.write(f"[{i}/4] TIMEOUT - may still be processing...\n\n")
            p.kill()
        
        time.sleep(2)
    
    # Add to collection
    f.write("Adding products to collection...\n")
    for i, prod_id in enumerate(products, 1):
        query = f'mutation {{ add: collectionAddProductsV2(id: "{collection_id}", productIds: ["{prod_id}"]) {{ userErrors {{ field message }} }} }}'
        f.write(f"[{i}/4] Adding to collection...\n")
        f.flush()
        
        p = subprocess.Popen(
            [cmd, 'store', 'execute', '--store', 'pfd2zx-7h.myshopify.com', '--allow-mutations', '--query', query],
            stdout=f,
            stderr=subprocess.STDOUT
        )
        
        try:
            p.wait(timeout=120)
            f.write(f"[{i}/4] Added! (code: {p.returncode})\n\n")
        except subprocess.TimeoutExpired:
            f.write(f"[{i}/4] TIMEOUT\n\n")
            p.kill()
        
        time.sleep(1)
    
    f.write("\nCOMPLETE!\n")

print("PUBLISH_FINISHED")
print("Log:", log)