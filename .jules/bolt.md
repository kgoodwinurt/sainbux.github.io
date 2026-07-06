
## 2026-07-06 - Optimizing Critical Path and LCP
**Learning:** Relocating render-blocking CSS to the <head> and adding preconnect hints significantly improves DCL. Adding fetchpriority="high" and explicit dimensions to the LCP image prevents Layout Shift (CLS) and speeds up the Largest Contentful Paint. Always verify SRI hashes when moving external assets, as mismatches will block the resource.
**Action:** Use a local server and Playwright to verify that assets load correctly (no console errors) and that performance metrics (DCL, LCP) actually improve after optimizations.
