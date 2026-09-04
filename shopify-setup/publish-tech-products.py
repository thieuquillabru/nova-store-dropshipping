import os
import subprocess

home = os.path.join(os.path.expanduser('~'))
cmd = os.path.join(home, 'AppData', 'Roaming', 'npm', 'shopify.cmd')
log_file = os.path.join(os.environ['TEMP'], 'publish-tech-products.log')

# Query to publish products and add to collection
query = """mutation {
  pub1: publishablePublish(id: "gid://shopify/Product/8049748115534", input: { publicationId: "gid://shopify/Publication/196746707022" }) { userErrors { field message } }
  pub2: publishablePublish(id: "gid://shopify/Product/8049748148302", input: { publicationId: "gid://shopify/Publication/196746707022" }) { userErrors { field message } }
  pub3: publishablePublish(id: "gid://shopify/Product/8049748181070", input: { publicationId: "gid://shopify/Publication/196746707022" }) { userErrors { field message } }
  pub4: publishablePublish(id: "gid://shopify/Product/8049748213838", input: { publicationId: "gid://shopify/Publication/196746707022" }) { userErrors { field message } }
  add1: collectionAddProductsV2(id: "gid://shopify/Collection/315070480462", productIds: ["gid://shopify/Product/8049748115534"]) { userErrors { field message } }
  add2: collectionAddProductsV2(id: "gid://shopify/Collection/315070480462", productIds: ["gid://shopify/Product/8049748148302"]) { userErrors { field message } }
  add3: collectionAddProductsV2(id: "gid://shopify/Collection/315070480462", productIds: ["gid://shopify/Product/8049748181070"]) { userErrors { field message } }
  add4: collectionAddProductsV2(id: "gid://shopify/Collection/315070480462", productIds: ["gid://shopify/Product/8049748213838"]) { userErrors { field message } }
}"""

with open(log_file, 'w') as f:
    result = subprocess.run(
        [cmd, 'store', 'execute', '--store', 'pfd2zx-7h.myshopify.com', '--allow-mutations', '--query', query],
        stdout=f,
        stderr=subprocess.STDOUT,
        timeout=180
    )

print('EXIT_CODE:', result.returncode)
print('LOG:', log_file)