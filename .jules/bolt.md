# Bolt Agent Performance Journal

## 2026-08-07 - Relocate Font Awesome & Optimize Resource Connection
**Learning:** Relocating the Font Awesome CSS link from the end of the `<body>` to the `<head>`, and adding a `preconnect` resource hint for `cdnjs.cloudflare.com` right before it, dramatically reduces DocumentContentLoaded (DCL) times for static pages. This connects the browser early to the Font Awesome CDN, eliminating DNS resolution and TCP/TLS handshakes from blocking initial render.
**Action:** Always place resource preconnect links before the corresponding stylesheet in `<head>` to avoid rendering and layout shifts, and profile results using Playwright.

## 2026-08-07 - Eliminate Multi-Step Asset Redirects
**Learning:** External assets (such as the ORCID badge icon) hosted on paths that silently redirect across multiple subdomains can introduce significant latency due to repeated DNS, TCP, and TLS connection setups on page load.
**Action:** Update third-party asset URLs to their canonical direct links (e.g., direct WP uploads or CDN URLs) to prevent multi-hop redirects and speed up asset fetching.
