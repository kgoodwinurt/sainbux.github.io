## 2026-07-14 - [Security Hardening of Static Site Assets]
**Vulnerability:** Tabnabbing (reverse tab-nabbing), lack of Content Security Policy (CSP), and missing Subresource Integrity (SRI).
**Learning:** Even static portfolios are vulnerable to identity-related security risks. External links without `rel="noopener noreferrer"` allow malicious target sites to control the referring page. Lack of SRI on CDNs (like Font Awesome) means a compromise of the CDN could lead to site-wide style/icon injection or potential XSS if the CDN serves JS instead of CSS.
**Prevention:** Always implement a strict CSP, use SRI for all third-party CDNs, and use `rel="noopener noreferrer"` on all links with `target="_blank"` or named targets.
