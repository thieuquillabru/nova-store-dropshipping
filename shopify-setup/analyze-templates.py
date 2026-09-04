import os

extract_folder = os.path.join(os.path.expanduser('~'), 'Desktop', 'Template_extracted')

templates = ['chimes', 'controller-site', 'street-flavor']

for template in templates:
    template_path = os.path.join(extract_folder, template)
    print(f"\n{'='*70}")
    print(f"  ANALYSE: {template.upper()}")
    print('='*70)
    
    # Lister tous les fichiers récursivement
    for root, dirs, files in os.walk(template_path):
        level = root.replace(template_path, '').count(os.sep)
        indent = '  ' * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = '  ' * (level + 1)
        for file in sorted(files):
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            print(f'{subindent}{file} ({size:,} bytes)')