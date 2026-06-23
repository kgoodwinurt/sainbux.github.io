# Sentinel's Journal

## 2025-05-14 - Initial Security Audit
**Vulnerability:** Missing security headers (CSP), missing SRI for CDN assets, and potential reverse tabnabbing via `target="_blank"` links without `rel="noopener noreferrer"`.
**Learning:** Even static sites benefit from defense-in-depth measures like CSP and SRI to prevent XSS and ensure the integrity of third-party assets.
**Prevention:** Always include CSP meta tags and use SRI for external scripts/styles. Ensure all external links using `target="_blank"` also include `rel="noopener noreferrer"`.
