# Modern CSS Features Reference

This document provides examples of modern CSS features used in the Venka website redesign. These features enable powerful functionality without JavaScript.

## 1. View Transitions API

Provides smooth animations between page navigations in multi-page applications.

### Basic Implementation

```html
<!-- In HTML head -->
<meta name="view-transition" content="same-origin">
```

```css
/* Enable view transitions */
@view-transition {
  navigation: auto;
}

/* Customize the transition */
::view-transition-old(root) {
  animation: 0.3s ease-out fade-out;
}

::view-transition-new(root) {
  animation: 0.3s ease-in fade-in;
}

@keyframes fade-out {
  from { opacity: 1; }
  to { opacity: 0; transform: translateY(-10px); }
}

@keyframes fade-in {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
```

### Named View Transitions

```css
/* Mark elements for special transitions */
.hero-title {
  view-transition-name: hero-title;
}

::view-transition-old(hero-title),
::view-transition-new(hero-title) {
  animation-duration: 0.5s;
}
```

## 2. CSS Container Queries

Style elements based on their container size rather than viewport.

```css
/* Define container */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* Query container size */
@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 150px 1fr;
  }
}

@container card (max-width: 399px) {
  .card {
    display: flex;
    flex-direction: column;
  }
}

/* Container query units */
.card-title {
  font-size: clamp(1.5rem, 5cqw, 2.5rem);
  /* cqw = container query width */
}
```

## 3. CSS :has() Selector

Parent selector that styles based on children.

```css
/* Style form with errors */
.form:has(.input-error) {
  border: 2px solid var(--color-error);
  background: var(--color-error-light);
}

/* Navigation with active item */
.nav:has(.nav-item.active) {
  background: var(--color-surface);
}

/* Card with image */
.card:has(img) {
  grid-template-columns: 200px 1fr;
}

/* Disable submit if form has errors */
.form:has(.input-error) .submit-button {
  opacity: 0.5;
  pointer-events: none;
}
```

## 4. CSS Cascade Layers

Manage CSS specificity with explicit layers.

```css
/* Define layer order */
@layer reset, base, components, utilities, overrides;

/* Reset layer - lowest priority */
@layer reset {
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
}

/* Base styles */
@layer base {
  body {
    font-family: var(--font-sans);
    line-height: 1.5;
    color: var(--color-text);
  }
}

/* Components */
@layer components {
  .button {
    padding: 0.5rem 1rem;
    border-radius: 0.375rem;
  }
}

/* Utilities - higher priority */
@layer utilities {
  .mt-4 { margin-top: 1rem; }
  .text-center { text-align: center; }
}

/* Import external CSS into layers */
@import url("normalize.css") layer(reset);
```

## 5. CSS Subgrid

Align nested grid items with parent grid.

```css
/* Parent grid */
.layout {
  display: grid;
  grid-template-columns: 200px 1fr 300px;
  gap: 2rem;
}

/* Child uses parent's grid */
.card {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: span 3; /* spans all parent columns */
}

/* Nested items align to parent grid */
.card-header { grid-column: 1; }
.card-content { grid-column: 2; }
.card-sidebar { grid-column: 3; }

/* Row subgrid */
.nested-grid {
  display: grid;
  grid-template-rows: subgrid;
  grid-row: span 4;
}
```

## 6. CSS Color Functions

Modern color manipulation without preprocessors.

```css
:root {
  --brand-color: #5e4cdb;
  
  /* Color mixing */
  --brand-light: color-mix(in srgb, var(--brand-color) 20%, white);
  --brand-dark: color-mix(in srgb, var(--brand-color), black 20%);
  
  /* Relative colors */
  --brand-hsl: hsl(from var(--brand-color) h s l);
  --brand-muted: hsl(from var(--brand-color) h calc(s * 0.5) l);
  --brand-vivid: hsl(from var(--brand-color) h calc(s * 1.2) l);
  
  /* Contrast colors */
  --text-on-brand: color-contrast(var(--brand-color) vs white, black);
}

/* LCH color space for perceptually uniform colors */
.gradient {
  background: linear-gradient(
    in lch,
    lch(50% 100 0),
    lch(50% 100 360)
  );
}
```

## 7. CSS Logical Properties

Support for all writing modes and RTL languages.

```css
/* Instead of margin-left/right */
.element {
  margin-inline-start: 1rem;  /* margin-left in LTR */
  margin-inline-end: 2rem;    /* margin-right in LTR */
}

/* Instead of padding-top/bottom */
.element {
  padding-block-start: 1rem;  /* padding-top */
  padding-block-end: 2rem;    /* padding-bottom */
}

/* Logical sizing */
.sidebar {
  inline-size: 300px;        /* width in horizontal writing */
  max-block-size: 100vh;     /* max-height in horizontal writing */
}

/* Logical positioning */
.tooltip {
  inset-inline-start: 0;     /* left in LTR */
  inset-block-start: 100%;   /* top */
}
```

## 8. CSS :is() and :where()

Simplify complex selectors.

```css
/* Instead of repeating selectors */
/* Old way: */
.header a:hover,
.nav a:hover,
.footer a:hover {
  color: var(--color-accent);
}

/* New way with :is() */
:is(.header, .nav, .footer) a:hover {
  color: var(--color-accent);
}

/* :where() has 0 specificity */
:where(.card) {
  padding: 1rem; /* Easy to override */
}

/* Combining with :not() */
:is(h1, h2, h3):not(:where(.no-margin)) {
  margin-block-end: 1rem;
}
```

## 9. CSS Nesting

Native CSS nesting (no preprocessor needed).

```css
.card {
  background: var(--color-surface);
  padding: 1.5rem;
  
  /* Nested elements */
  .card-header {
    font-size: 1.25rem;
    margin-bottom: 1rem;
  }
  
  .card-content {
    color: var(--color-text-secondary);
    
    p {
      margin-block: 0.5rem;
    }
  }
  
  /* Nested pseudo-classes */
  &:hover {
    box-shadow: var(--shadow-lg);
  }
  
  /* Nested media queries */
  @media (min-width: 768px) {
    padding: 2rem;
  }
}
```

## 10. CSS Scroll Snap

Smooth, controlled scrolling without JavaScript.

```css
/* Scroll container */
.carousel {
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  
  /* Hide scrollbar */
  scrollbar-width: none;
  -ms-overflow-style: none;
  &::-webkit-scrollbar { display: none; }
}

/* Scroll items */
.carousel-item {
  scroll-snap-align: center;
  scroll-snap-stop: always;
  flex: 0 0 100%;
}

/* Vertical scroll sections */
.sections {
  height: 100vh;
  overflow-y: auto;
  scroll-snap-type: y proximity;
}

.section {
  min-height: 100vh;
  scroll-snap-align: start;
}
```

## 11. CSS Anchor Positioning

Position elements relative to other elements (experimental).

```css
/* Define anchor */
.button {
  anchor-name: --trigger;
}

/* Position relative to anchor */
.tooltip {
  position: absolute;
  anchor-default: --trigger;
  
  /* Position above anchor */
  bottom: anchor(top);
  left: anchor(center);
  translate: -50% -0.5rem;
}

/* Fallback positioning */
@supports not (anchor-name: --a) {
  .tooltip {
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
  }
}
```

## 12. Preference Media Queries

Respect user preferences beyond light/dark mode.

```css
/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

/* High contrast */
@media (prefers-contrast: high) {
  :root {
    --color-background: #ffffff;
    --color-text: #000000;
    --color-accent: #0000ff;
  }
}

/* Reduced transparency */
@media (prefers-reduced-transparency: reduce) {
  .glass-effect {
    backdrop-filter: none;
    background: var(--color-surface);
  }
}

/* Color scheme */
@media (prefers-color-scheme: dark) {
  :root {
    /* Dark mode colors */
  }
}
```

## Browser Support Notes

- **View Transitions**: Chrome 111+, Safari 18+
- **Container Queries**: Chrome 105+, Safari 16+, Firefox 110+
- **:has()**: Chrome 105+, Safari 15.4+, Firefox 121+
- **Cascade Layers**: All modern browsers
- **Subgrid**: Firefox 71+, Safari 16+, Chrome 117+
- **Color Functions**: Partial support, use fallbacks
- **Logical Properties**: All modern browsers
- **Nesting**: Chrome 120+, Safari 16.5+, Firefox 117+

## Progressive Enhancement Strategy

```css
/* Base styles that work everywhere */
.element {
  background: #5e4cdb;
}

/* Enhanced with modern features */
@supports (color: color-mix(in srgb, red 50%, blue)) {
  .element {
    background: color-mix(in srgb, var(--brand-color) 80%, white);
  }
}

/* Feature detection for :has() */
@supports selector(:has(*)) {
  .form:has(.error) {
    border-color: red;
  }
}
```

These modern CSS features enable powerful, performant styling without JavaScript dependencies, creating a better user experience while maintaining clean, maintainable code.
