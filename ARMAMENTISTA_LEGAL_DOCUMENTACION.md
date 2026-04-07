# Armamentista Legal - Documentación 🎖️

## Descripción General

Esta es la página principal de la **División Armamentista Legal** de Umbrella Corporation. Presenta de manera profesional y atractiva los catálogos de productos relacionados con equipamiento de defensa y seguridad.

## Estructura de la Página

### 1️⃣ **Navegación (NAV)**
- **Logo de Umbrella Corp** - Enlace a la página principal (`/`)
- **Menú de links** - Links para navegar
- **Botón "Atrás"** - Regresa a la página de inicio
- **Menú móvil** - Se activa en pantallas pequeñas

### 2️⃣ **Sección Hero**
```
┌─────────────────────────────────────────┐
│  Especimen: ARMAMENTISTA — AUTORIZADA   │
│                                         │
│  📦 Logo de Umbrella                    │
│                                         │
│  Seguridad Avanzada Legal               │
│                                         │
│  "Umbrella no vende armas... vende      │
│   seguridad avanzada."                  │
│                                         │
│  [Botón] Ver Catálogo  [Botón] Inicio   │
└─────────────────────────────────────────┘
```

**Panel derecho**: Información en tiempo real
- Nivel de autorización
- Productos activos (47)
- Estado de división

### 3️⃣ **Catálogo de Productos**
9 tarjetas con las siguientes categorías:

| # | Producto | Icono | Descripción |
|---|----------|-------|-------------|
| 1 | Equipamiento Táctico | 🎖️ | Uniformes, sistemas MOLLE, arneses |
| 2 | Protección Balística | 🛡️ | Chalecos, placas cerámicas |
| 3 | Cascos Inteligentes | ⚙️ | Comunicación integrada, AR |
| 4 | Trajes de Protección | 👔 | Resistencia química, HEPA |
| 5 | Rifles Autorizados | 🔫 | Rifles NATO certificados |
| 6 | Control No Letal | ⚡ | Electrochoque, gases, gomas |
| 7 | Tecnología Militar | 🚁 | Visión nocturna, térmica, radar |
| 8 | Drones de Vigilancia | 🛰️ | Cuadricópteros, cámaras 4K |
| 9 | Reconocimiento | 📡 | IA, biometría, mapeo real-time |

Cada tarjeta tiene:
- Icono emoji 🎨
- Nombre del producto
- Lista de items (máx 4)
- Link "Explorar →"

### 4️⃣ **Footer**
- Logo y descripción de la corporación
- Enlaces de soporte (Documentación, Contacto, FAQ)
- Enlaces legales (Términos, Privacidad, Certificaciones)

---

## Cómo Personalizar

### 📝 **Cambiar el contenido de un producto**

Busca en el HTML la sección `<!-- Card X -->` y modifica:

```html
<div class="prod-icon">🎖️</div>                    <!-- Cambiar emoji -->
<h3 class="prod-name">Equipamiento Táctico</h3>   <!-- Cambiar título -->
<ul class="prod-items">
    <li>Uniforme de combate...</li>                <!-- Cambiar items -->
    <li>Sistemas de carga modular...</li>
    ...
</ul>
```

### 🎨 **Cambiar colores**

En la sección `<style>` al inicio del archivo, modifica las variables CSS:

```css
:root {
    --red:#c8102e;        /* Color rojo principal */
    --bg:#e8eaeb;         /* Fondo gris claro */
    --hosp-deep:#1c3a4a;  /* Fondo azul oscuro */
    --green:#00c864;      /* Color verde accent */
    /* ... más variables */
}
```

### 🔗 **Agregar nuevas tarjetas de productos**

1. Copia y pega una tarjeta existente (dentro de `<div class="prod-grid">`)
2. Cambia el emoji, nombre e items
3. Los estilos se aplicarán automáticamente

---

## Acceso a la Página

**URL Local**: `http://localhost:8000/armamentista-legal/`

**Estructura de archivos**:
```
umbrella-corporation/
├── manage.py
└── umbrella_corporation/
    ├── Armamentista/
    │   ├── views.py           ← Lógica de vistas
    │   ├── urls.py            ← Rutas de esta app
    │   └── templates/
    │       └── armamentista_legal.html    ← ⭐ PÁGINA PRINCIPAL
    └── umbrella_corporation/
        └── urls.py            ← Rutas globales
```

---

## Notas Técnicas

### 📜 Estilos y Scripts

- **CSS**: Inline (dentro del `<style>`)
- **JavaScript**: Minimal (~20 líneas)
  - Cursor personalizado
  - Efecto de navbar al scroll
  - Menú móvil toggle

### 🎯 Responsive Design

| Pantalla | Cambios |
|----------|---------|
| Desktop (>1100px) | Grid 2 columnas, nav normal |
| Tablet (768-1100px) | Grid 1 columna, nav ajustado |
| Móvil (<768px) | Grid 1 columna, menú hamburguesa |

### ♿ Accesibilidad

- Contraste de colores suficiente
- Links claros y funcionales
- Fuentes legibles
- Estructura semántica HTML

---

## Mantenimiento

### ✅ Checklist para mantener la página

- [ ] Verificar que todos los links funcionen
- [ ] Revisar que los estilos sean consistentes
- [ ] Probar en móvil y desktop
- [ ] Actualizar descripciones de productos según sea necesario
- [ ] Mantener el mensaje de "Seguridad Avanzada Legal"

---

## Preguntas Frecuentes

**¿Puedo cambiar el título?**
Sí, en la sección Hero cambia `<h1 class="h-h1">Seguridad<br><span class="r">Avanzada</span>...`

**¿Cómo agrego más productos?**
Añade nuevas tarjetas antes de cerrar `</div>` (fin del `prod-grid`)

**¿Dónde van las imágenes?**
Crea una carpeta `static/` dentro de `Armamentista/` y referéncialas con `{% static 'imagen.png' %}`

**¿Puedo cambiar el logo?**
Sí, reemplaza la URL de la imagen del PNG de Umbrella por tu propia URL

---

## Información de la Rama

- **Rama GitHub**: `armamento-legal`
- **División**: Armamentista Legal
- **Responsable**: [Tu nombre]
- **Fecha creación**: 31 de Marzo, 2026

✨ **¡La página está lista para usar!** ✨
