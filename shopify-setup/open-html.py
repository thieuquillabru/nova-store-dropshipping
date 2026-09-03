import os
import webbrowser

# Change to the correct directory
os.chdir(os.path.join(os.path.expanduser('~'), '.cline', 'data', 'workspaces', 'chat', 'shopify-setup'))

# Now open the HTML file
html_file = os.path.join(os.path.expanduser('~'), '.cline', 'data', 'workspaces', 'chat', 'apercu-glassmorphism.html')
url = 'file:///' + html_file.replace('\\', '/')
print('URL:', url)
print('Exists:', os.path.exists(html_file))
webbrowser.open(url)
print('OPENED')