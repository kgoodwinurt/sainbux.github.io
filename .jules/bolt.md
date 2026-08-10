# Bolt Performance Journal

Journal of critical performance learnings for this repository.

## 2026-03-06 - Relocating CDN Stylesheets and Preconnecting
**Learning:** Moving a CDN stylesheet (such as Font Awesome) from the HTML body to the head and placing a `<link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>` immediately before it resolves the connection early (DNS lookup, TCP handshake, TLS negotiation) and prevents render blocking or FOUC, reducing DocumentContentLoaded (DCL) times by ~85% (from ~112ms to ~16ms).
**Action:** Always preconnect to critical CDN domains before loading blocking or layout-affecting stylesheets, and ensure CDN stylesheets are placed in the `<head>` of static HTML pages rather than nested inside the `<body>`.
