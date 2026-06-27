## 2026-06-27 - Subdomain Specificity in CSP for External Assets
**Vulnerability:** Content Security Policy (CSP) blocking external assets due to overly restrictive domain whitelisting.
**Learning:** External services like ORCID may serve assets from subdomains (e.g., `info.orcid.org`) that differ from the primary domain (`orcid.org`). A CSP `img-src` directive must explicitly include these subdomains or use a wildcard if trusted.
**Prevention:** Always verify CSP implementation using automated tools (like Playwright) to monitor console violations and ensure all necessary asset sources are whitelisted.
