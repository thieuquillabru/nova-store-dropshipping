import os
import zipfile

desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
template_folder = os.path.join(desktop, 'Template site')
extract_folder = os.path.join(desktop, 'Template_extracted')

# Créer le dossier d'extraction
os.makedirs(extract_folder, exist_ok=True)

zips = [
    'chimes-site-complet.zip',
    'controller-site-complet.zip',
    'street-flavor.zip'
]

for zip_name in zips:
    zip_path = os.path.join(template_folder, zip_name)
    extract_path = os.path.join(extract_folder, zip_name.replace('.zip', ''))
    os.makedirs(extract_path, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"Extraction: {zip_name}")
    print('='*60)
    
    with zipfile.ZipFile(zip_path, 'r') as z:
        # Lister le contenu
        file_list = z.namelist()
        print(f"Fichiers: {len(file_list)}")
        
        # Extraire
        z.extractall(extract_path)
        
        # Analyser la structure
        print("\nStructure:")
        for f in sorted(file_list)[:50]:  # Limiter à 50 pour la lisibilité
            print(f"  {f}")
        
        if len(file_list) > 50:
            print(f"  ... et {len(file_list) - 50} autres fichiers")

print(f"\n\nExtraction terminée dans: {extract_folder}")