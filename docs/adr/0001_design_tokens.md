# 0001 Design Tokens

## Decision
Use a small, centralized set of CSS variables for color, type, spacing, and shape so the UI can be tuned from one place.

## Tokens
- Fonts: `--font-display`, `--font-body`
- Colors: `--color-paper`, `--color-surface`, `--color-ink`, `--color-ink-muted`,
  `--color-accent`, `--color-accent-strong`, `--color-accent-soft`, `--color-error`,
  `--color-error-soft`
- Shape: `--radius-card`, `--radius-input`
- Shadows: `--shadow-card`

## Usage
Defined in `src/retail/static/retail/site.css` and consumed by all templates to keep styling consistent and minimal.
