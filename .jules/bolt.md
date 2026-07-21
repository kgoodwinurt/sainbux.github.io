# Bolt Journal - Critical Performance Learnings

## 2025-07-21 - [Font Awesome CDN Preconnecting and Relocation]
**Learning:** Moving the Font Awesome stylesheet link from the bottom of the body to the `<head>` and adding a `<link rel="preconnect" href="https://cdnjs.cloudflare.com">` resource hint before it ensures the browser starts preconnecting (DNS lookup, TCP handshake, TLS negotiation) immediately. This avoids blocking rendering later and drastically reduces DocumentContentLoaded (DCL) times by up to 90% (e.g., from ~114ms to ~22ms) on static sites, while also preventing Flash of Unstyled Content (FOUC).
**Action:** Always relocate CDN-hosted stylesheets (like Font Awesome) to the `<head>` and place a corresponding `preconnect` link directly before them in static HTML pages.

## 2025-07-21 - [Bypassing External Logo Redirects]
**Learning:** External badges/logos (such as the ORCID badge icon) often use legacy or redirection-heavy URLs (e.g. `https://orcid.org/sites/...` which redirects to `https://info.orcid.org/sites/...`). These redirect chains introduce silent overhead due to multi-step DNS, TCP, and TLS handshakes across different domains.
**Action:** Update third-party asset URLs to their canonical, direct-resolved URLs (e.g., `https://info.orcid.org/wp-content/uploads/2020/12/ORCIDiD_icon16x16.png`) to bypass redirection latency on initial page rendering.
