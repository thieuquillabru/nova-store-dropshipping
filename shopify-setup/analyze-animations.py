import os

extract_folder = os.path.join(os.path.expanduser('~'), 'Desktop', 'Template_extracted')

# Read key files for animation analysis
files_to_analyze = [
    ('chimes-site-complet/chimes/script.js', 'Chimes - Main Script'),
    ('chimes-site-complet/chimes/chimes.js', 'Chimes - Chimes Logic'),
    ('chimes-site-complet/chimes/utils.js', 'Chimes - Utils'),
    ('controller-site-complet/controller-site/index.html', 'Controller - HTML'),
    ('street-flavor/street-flavor/assets/index-CZY-90W-.js', 'Street Flavor - JS'),
]

for filepath, title in files_to_analyze:
    full_path = os.path.join(extract_folder, filepath)
    print(f"\n{'='*70}")
    print(f"  {title}")
    print('='*70)
    
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Extract animation-related content
            lines = content.split('\n')
            anim_lines = []
            for i, line in enumerate(lines, 1):
                lower = line.lower()
                if any(kw in lower for kw in ['animate', 'transition', 'transform', 'keyframes', 
                    'animation', 'ease', 'duration', 'delay', 'requestanimationframe',
                    'gsap', 'motion', 'spring', 'tween', 'lerp', 'interpolate',
                    'hover', 'mouse', 'click', 'scroll', 'wheel', 'drag',
                    'particle', 'physics', 'velocity', 'force', 'gravity',
                    'rotate', 'scale', 'translate', 'skew', 'opacity', 'blur',
                    'shadow', 'gradient', 'glow', 'bounce', 'fade', 'slide',
                    'canvas', 'webgl', 'three.js', 'scene', 'camera', 'renderer']):
                    anim_lines.append(f"{i}: {line.strip()[:120]}")
            
            print(f"Found {len(anim_lines)} animation-related lines:")
            for line in anim_lines[:50]:
                print(line)
            if len(anim_lines) > 50:
                print(f"... and {len(anim_lines) - 50} more")
    else:
        print("File not found")

print("\n" + "="*70)
print("  ANALYSIS COMPLETE")
print("="*70)