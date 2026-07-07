## 2026-07-07 - Defense in Depth for Static Sites
**Vulnerability:** Lack of modern security headers (CSP), missing Subresource Integrity (SRI) for third-party assets, and missing link security attributes (rel="noopener noreferrer").
**Learning:** Even simple static sites can be secured using meta tags for CSP. SRI is critical when relying on CDNs to prevent malicious code injection if the provider is compromised. rel="me" is a useful addition for decentralized identity verification (e.g., Mastodon).
**Prevention:** Always implement CSP and SRI by default. Use automated scripts to verify link attributes across all HTML files.
