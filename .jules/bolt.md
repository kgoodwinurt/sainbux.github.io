## 2025-05-14 - Critical Path and LCP Optimization
**Learning:** Relocating render-blocking CSS (Font Awesome) from the bottom of the body to the head, combined with preconnect hints, significantly improves DOMContentLoaded (DCL) times (from ~671ms to ~40ms). Additionally, optimizing the LCP element (profile image) with `fetchpriority="high"` and explicit dimensions improves FCP/LCP and prevents CLS.
**Action:** Always prioritize moving CSS to the `<head>` and use resource hints (`preconnect`, `fetchpriority`) for critical assets.

## 2025-05-14 - Clean Repository Maintenance
**Learning:** Utility scripts used for profiling and verification (e.g., `profile_perf.py`) should not be committed to the repository to avoid technical debt and clutter.
**Action:** Remove all temporary automation and measurement scripts before submitting changes.
