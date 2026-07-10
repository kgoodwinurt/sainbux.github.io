## 2026-07-10 - Optimizing Critical Rendering Path for Static Sites
**Learning:** Moving render-blocking assets like Font Awesome to the <head> and adding preconnect for the CDN significantly improves DOMContentLoaded (DCL). In this repository, DCL was reduced from ~146ms to ~30ms. Adding explicit dimensions and fetchpriority to the main header image also helps with LCP and preventing CLS.
**Action:** Always check for render-blocking assets at the bottom of the body and relocate them to the head with appropriate resource hints (preconnect/preload) and image attributes.
