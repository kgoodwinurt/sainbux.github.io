
## 2025-06-06 - [Static Site Asset Optimization]
**Learning:** For simple static sites with no build step, performance can be significantly improved by manually implementing modern browser hints like `fetchpriority="high"` for LCP images and using the `media="print" onload="this.media='all'"` pattern for non-critical CSS (like Font Awesome).
**Action:** Always check for render-blocking third-party CSS and prioritize above-the-fold images using these low-overhead attributes.
