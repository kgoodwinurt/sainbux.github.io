## 2026-07-08 - Critical Rendering Path Optimization
**Learning:** Moving render-blocking assets (Font Awesome) to the `<head>` and adding preconnect hints significantly reduces DCL, even in simple static sites. Adding `fetchpriority="high"` and explicit dimensions to the LCP element (profile image) improves both perceived performance and layout stability (CLS).
**Action:** Always check for late-loading stylesheets and unoptimized LCP elements in static landing pages.
