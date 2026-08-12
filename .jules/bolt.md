# Bolt Journal

Journal of critical performance learnings for this repository.

## 2026-08-12 - Critical Path Asset Optimizations for Fast Static Pages
**Learning:** Relocating external CDNs like Font Awesome stylesheets from the bottom of the body to the head, coupled with a preconnect resource hint (`<link rel="preconnect" ... crossorigin>`), drastically reduces DocumentContentLoaded (DCL) times on static portfolio pages (e.g. from ~100ms down to ~17ms). Additionally, applying `fetchpriority="high"` on above-the-fold hero images (Largest Contentful Paint) prioritizes image fetching and prevents unnecessary layout shifts.
**Action:** Always preconnect to critical domains early in the head block, load critical stylesheets in the head to avoid FOUC/render delays, and explicitly declare high fetch priority on key LCP elements.
