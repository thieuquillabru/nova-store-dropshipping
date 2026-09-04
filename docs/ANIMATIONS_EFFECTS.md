# Analyse Complete des Animations & Effets

> Etude A-Z de tous les effets visuels, animations et micro-interactions

---

## 1. CHIMES — Animations Physiques & Sonores

### 1.1 Systeme de Physique (Verlet Integration)

```javascript
class Particle {
  constructor({ x, y, pinned = false, id = 0, char = "" }) {
    this.x = x; this.y = y;
    this.oldX = x; this.oldY = y;
    this.pinned = pinned;
    this.char = char;
  }
  
  update(dt) {
    if (this.pinned) return;
    const velX = (this.x - this.oldX) * FRICTION;
    const velY = (this.y - this.oldY) * FRICTION;
    this.oldX = this.x;
    this.oldY = this.y;
    this.x += velX;
    this.y += velY + GRAVITY * dt;
  }
}

const FRICTION = 0.98;
const GRAVITY = 0.2;
const MOUSE_SIZE = 5000;
const MOUSE_STRENGTH = 4;
```

### 1.2 Scene Transition (780ms)

```javascript
async function transitionTo(id, direction) {
  const scene = document.getElementById("scene");
  scene.style.transition = `transform ${SCENE_MS}ms var(--ease-scene), 
                             opacity ${SCENE_MS}ms var(--ease-scene)`;
  scene.style.transform = `translateX(${exitX})`;
  scene.style.opacity = "0.25";
  await sleep(SCENE_MS * 0.78);
  // Reset et entree
  scene.style.transform = `translateX(${enterX})`;
  scene.style.opacity = "0.25";
  void scene.offsetWidth; // Force reflow
  scene.style.transform = "translateX(0)";
  scene.style.opacity = "1";
}
```

### 1.3 Character Stagger

```css
.char {
  animation: charEnter 480ms ease backwards;
  animation-delay: calc(var(--i) * 20ms);
}

@keyframes charEnter {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}
```

### 1.4 Audio (Web Audio API)

```javascript
class Chimes {
  strike(particle, intensity) {
    const ctx = new AudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.value = this.getFreq(particle);
    gain.gain.setValueAtTime(0, ctx.currentTime);
    gain.gain.linearRampToValueAtTime(0.3, ctx.currentTime + 0.01);
    gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + duration);
  }
}
```

---

## 2. CONTROLLER-SITE — Animations 3D Premium

### 2.1 Three.js Scene
```

### 3.2 Parallax & Scroll

```javascript
const ingredients = document.querySelectorAll('.ingredient');
window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  ingredients.forEach((ing, i) => {
    const speed = 0.5 + i * 0.1;
    ing.style.transform = `translateY(${scrollY * speed}px) rotate(${scrollY * 0.1}deg)`;
  });
});
```

### 3.3 CSS Animations

```css
@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(5deg); }
}

.ingredient {
  animation: float 3s ease-in-out infinite;
  animation-delay: calc(var(--i) * 0.2s);
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(100px); }
  to { opacity: 1; transform: translateY(0); }
}

.product-card {
  animation: slideUp 0.6s ease backwards;
  animation-delay: calc(var(--i) * 0.1s);
}
```

### 3.4 Image Crossfade

```javascript
function crossfadeImages(img1, img2) {
  img1.style.transition = 'opacity 1s ease';
  img1.style.opacity = '0';
  img2.style.transition = 'opacity 1s ease';
  img2.style.opacity = '1';
  img2.style.transform = 'scale(1.1)';
  setTimeout(() => {
    img2.style.transition = 'transform 10s ease';
    img2.style.transform = 'scale(1)';
  }, 1000);
}
```

---

## 4. SYNTHESE pour Nova Store

| Animation | Source | Priorite |
|---|---|---|
| Glassmorphism hover | Controller-site | Haute |
| Scroll reveal | Chimes | Haute |
| Magnetic buttons | Controller-site | Moyenne |
| Image zoom | Street-flavor | Moyenne |
| Parallax | Street-flavor | Basse |

### Easing Functions

```css
--ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
--ease-decelerate: cubic-bezier(0, 0, 0.2, 1);
--ease-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275);
```

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

*Analyse cree le 5 janvier 2026 - Nova Store*

```javascript
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, aspect, 0.1, 100);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

// Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
scene.add(ambientLight, directionalLight);
```

### 2.2 GLTF + Draco Loading

```javascript
const loader = new GLTFLoader();
const dracoLoader = new DRACOLoader();
dracoLoader.setDecoderPath('/draco/');
loader.setDRACOLoader(dracoLoader);

loader.load('/models/controller.glb', (gltf) => {
  model = gltf.scene;
  scene.add(model);
  const mixer = new THREE.AnimationMixer(model);
  gltf.animations.forEach(clip => mixer.clipAction(clip).play());
});
```

### 2.3 Scroll-Driven

```javascript
function onScroll() {
  const progress = window.scrollY / maxScroll;
  model.rotation.y = progress * Math.PI * 2;
  camera.position.z = 5 - progress * 2;
}
```

### 2.4 Glassmorphism CSS

```css
.glass-card {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(20px) saturate(125%);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 24px;
  box-shadow: 
    0 18px 44px -18px rgba(0, 0, 0, 0.85),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
  background: rgba(255, 255, 255, 0.12);
  transform: translateY(-8px) scale(1.02);
  box-shadow: 
    0 25px 50px -12px rgba(0, 0, 0, 0.9),
    inset 0 1px 0 rgba(255, 255, 255, 0.15);
}
```

### 2.5 Magnetic Button

```javascript
button.addEventListener('mousemove', (e) => {
  const rect = button.getBoundingClientRect();
  const x = e.clientX - rect.left - rect.width / 2;
  const y = e.clientY - rect.top - rect.height / 2;
  gsap.to(button, {
    x: x * 0.3,
    y: y * 0.3,
    duration: 0.3,
    ease: 'power2.out'
  });
});
```