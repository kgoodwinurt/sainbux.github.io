# Sentinel Journal

## 2025-10-24 - Security Hardening
**Vulnerability:** External links using `target="_blank"` without `rel="noopener noreferrer"` and external CDN resources without SRI.
**Learning:** Even static sites can have security vulnerabilities like reverse tabnabbing and supply chain risks via CDNs.
**Prevention:** Always use `rel="noopener noreferrer"` for external links and enforce Subresource Integrity (SRI) with `crossorigin` attributes for all CDN resources.
