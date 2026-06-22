## 2026-06-22 - Static Site Security Hardening
**Vulnerability:** Potential for XSS, subresource tampering, and reverse tabnabbing (target="_blank").
**Learning:** Even static portfolio sites benefit from a Content Security Policy (CSP) and Subresource Integrity (SRI) to protect against third-party supply chain attacks (CDNs). Using `target="_blank"` without `rel="noopener noreferrer"` remains a common but easily fixable vulnerability that exposes users to tabnabbing.
**Prevention:** Always implement a baseline CSP, use SRI for external assets, and ensure all external links have proper `rel` attributes.
