## Context
- Please read https://www.jonoalderson.com/conjecture/its-time-for-modern-css-to-kill-the-spa/ for context on using modern CSS to create fast, flicker-free experiences
- Read README.md 

## Scope
- TODO: Add where we store templates and css

## Technical Requirements
- Uses HTML and CSS only - NO frameworks, NO build steps, NO third-party libraries (no Tailwind, etc.)
- Uses modern HTML and CSS features (View Transitions API, Container Queries, :has(), etc.)
- Minimizes use of JavaScript
- Simplicity of code and implementation trumps all other goals
- Do not make code longer or more complex to support older browsers. Do not try to support older browsers.

## Design Requirements
- - Prevents flicker between page transitions using View Transitions API
- All pages must look good on both mobile, desktop, and tablet devices
- Mobile responsiveness is required on all pages. 

## Performance Requirements
- Efficient and fast to load
- Use CSS preloading if it improves user experience, but keep code simple.
- Single shared CSS file that can be cached by browser
- OR inline critical CSS to prevent render blocking
- OR include all CSS at start of each .html file

## Architecture Requirements
- Must be possible to change design aspects from one central location
- CSS architecture should work for both Django templates and static landing page

## Deliverables
1. Document ofcolors and design tokens in docs/adr/
