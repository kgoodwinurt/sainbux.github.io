# Sentinel Security Journal

## 2025-05-15 - Security Hardening Initial Scan
**Vulnerability:** Lack of security headers (CSP) and missing SRI on third-party assets (Font Awesome) increases the risk of XSS and supply chain attacks.
**Learning:** Static sites on GitHub Pages should explicitly define CSP via meta tags and use SRI for all external CDNs to ensure integrity.
**Prevention:** Always include CSP and SRI in the baseline template for new pages.
