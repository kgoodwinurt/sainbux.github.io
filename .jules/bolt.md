
## 2026-07-15 - Optimizing Critical Path for Static Site
**Learning:** Moving render-blocking assets like Font Awesome from the body to the head, combined with preconnect resource hints for their CDN, can reduce DocumentContentLoaded (DCL) by over 90% in static HTML pages.
**Action:** Always audit the placement of third-party CSS and use preconnect/dns-prefetch for external origins serving critical assets.
