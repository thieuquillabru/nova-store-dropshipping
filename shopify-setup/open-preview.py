import os
import webbrowser

home = os.path.expanduser('~')
f = os.path.join(home, '.cline', 'data', 'workspaces', 'chat', 'apercu-glassmorphism.html')
url = 'file:///' + f.replace('\\', '/')
print('Opening:', url)
webbrowser.open(url)
print('DONE')