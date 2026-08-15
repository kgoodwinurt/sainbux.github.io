## 2026-08-15 - Font Awesome Relocation and Resource Hints
**Learning:** Relocating render-blocking external CDN CSS (Font Awesome) to `<head>` alongside a `<link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>` hint and specifying high fetch priority / dimensions on the header image reduces `DOMContentLoaded` (DCL) time from ~110.68ms to ~23.74ms (~78.5% improvement) on static HTML pages without triggering CSP errors.
**Action:** Always relocate external CSS stylesheets to `<head>` and pair them with `preconnect` resource hints for the hosting CDN domain on static pages.
