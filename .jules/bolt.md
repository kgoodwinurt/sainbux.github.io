## 2025-06-10 - Optimizing LCP and CLS for static sites
**Learning:** For static sites without a build step, explicit HTML attributes like `width`, `height`, and `fetchpriority` are the most effective way to improve Core Web Vitals (LCP and CLS) without adding complexity. Preconnecting to critical CDNs (like Font Awesome) significantly reduces the time to first icon render.
**Action:** Always check for missing image dimensions and LCP priority candidates in static HTML files.
