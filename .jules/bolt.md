## 2026-07-03 - Critical Path Optimization for Static Portfolio
**Learning:** Relocating render-blocking CSS to the <head>, adding preconnect hints, and explicitly sizing the LCP image significantly improved performance. DOMContentLoaded (DCL) dropped from ~478ms to ~37ms (~92% reduction) by moving Font Awesome to the head and preconnecting to the CDN.
**Action:** Always prioritize moving CSS to the head and providing dimensions for LCP images to prevent layout shifts and speed up rendering.
