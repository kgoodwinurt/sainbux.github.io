# Sentinel Security Journal

## 2026-07-04 - Security Hardening of Static Site
**Vulnerability:** Lack of defense-in-depth measures in a static site, including missing SRI for external assets, missing tabnabbing protection for external links, and absent Content Security Policy.
**Learning:** Even static sites hosted on GitHub Pages benefit significantly from browser-level security controls. Subresource Integrity (SRI) prevents malicious code injection if a CDN is compromised. `rel="noopener noreferrer"` prevents potential tabnabbing attacks where a linked site could gain control over the original page's window.
**Prevention:** Always implement a restrictive CSP, use SRI for all third-party resources, and ensure all external `_blank` links use secure `rel` attributes.
