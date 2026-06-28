## 2026-06-28 - Optimizing Resource Discovery and LCP

**Learning:** Relocating critical stylesheets to the `<head>` and using `preconnect` hints for CDNs significantly improves DCL. Adding `fetchpriority="high"` and explicit dimensions to the main profile image (LCP element) improves FCP and eliminates layout shift (CLS). Removing redundant CSS blocks (duplicates) helps maintain a lean codebase and reduces parsing time.

**Action:** Always check for `<img>` tags in the initial viewport for missing `fetchpriority`, `width`, and `height`. Audit the `<head>` for missing `preconnect` hints to common CDNs.
