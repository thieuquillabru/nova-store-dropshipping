import os
import webbrowser

f = os.path.join(os.path.expanduser('~'), '.cline', 'data', 'workspaces', 'chat', 'apercu-boutique.html')
url = 'file:///' + f.replace('\\', '/')
print('Opening:', url)
webbrowser.open(url)
print('DONE')