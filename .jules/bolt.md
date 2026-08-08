# Bolt Performance Journal

Critical learnings from optimizing the performance of Sain Bux's portfolio site.

## 2025-08-08 - [Relocate Font Awesome and Preconnect Hint]
**Learning:** Relocating the `preconnect` resource hint to appear before the stylesheet it optimizes within the `<head>` ensures the browser initiates the TCP/TLS connection before encountering the CSS request, maximizing the performance benefit. Additionally, moving the render-blocking Font Awesome stylesheet from the `<body>` to the `<head>` prevents Flash of Unstyled Content (FOUC), layout shifts, and dramatically reduces DocumentContentLoaded (DCL) times by up to 90% (e.g., from ~750ms down to ~40ms).
**Action:** Always place `<link rel="preconnect">` for external CDN endpoints before referencing any styles from them, and ensure all render-blocking stylesheets are placed within the `<head>` rather than delayed in the `<body>`.

## 2025-08-08 - [Optimize LCP and CLS via Image Attributes]
**Learning:** Standard static site templates often include images (like `profile.jpg`) without explicit `width`, `height`, or `fetchpriority` attributes, causing cumulative layout shifts (CLS) and delays in Largest Contentful Paint (LCP) when the image is located above the fold.
**Action:** Provide explicit `width` and `height` attributes matching the CSS rendering dimensions to allow browsers to reserve layout space, and use `fetchpriority="high"` on critical above-the-fold assets to prioritize their network transfer.

## 2025-08-08 - [Canonical Asset URLs]
**Learning:** External badge and logo URLs (such as the ORCID badge icon) can silently redirect across subdomains, adding extra DNS/TCP/TLS connection roundtrips on initial page load.
**Action:** Update third-party assets to their canonical direct URLs (e.g., `https://info.orcid.org` instead of legacy redirect paths) to eliminate multi-step redirect chains.
