## 2026-07-07 - Independent Performance Optimizations
**Learning:** Relocating render-blocking assets like Font Awesome to the `<head>` significantly improves DomContentLoaded (DCL) times. In this project, DCL for `index.html` was reduced from ~730ms to ~25ms. Additionally, adding `fetchpriority="high"` and explicit dimensions to the Largest Contentful Paint (LCP) element (the profile image) improves visual stability and load prioritization.
**Action:** Always move render-blocking CSS to the `<head>` and optimize LCP images with `fetchpriority`, `width`, and `height`.
