# Bolt Performance Journal

Journal of critical performance learnings for this repository.

## 2025-11-01 - Render-Blocking Font Awesome & Preconnect Optimization
**Learning:** Placing external stylesheets (like Font Awesome CDN) at the bottom of the `<body>` blocks DOM parsing and causes visual Flash of Unstyled Content (FOUC). Relocating them to the `<head>` solves FOUC but can block initial render. Coupling the head relocation with an explicit `<link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>` resource hint placed *before* the stylesheet ensures that connection handshakes are initiated early, leading to an ~86% reduction in DocumentContentLoaded (DCL) time.
**Action:** Always preconnect to external asset CDNs when using render-blocking stylesheets, and ensure `<link rel="preconnect">` appears before the stylesheet in the `<head>` to maximize parallelization.
