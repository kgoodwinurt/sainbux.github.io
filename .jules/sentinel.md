## 2026-06-29 - Security Enhancements for External Resources

**Vulnerability:** External resources (CDN scripts/styles, third-party images) were loaded without integrity checks or privacy protections, and external links lacked protection against reverse tabnabbing.

**Learning:** Static sites often rely on CDNs. Using Subresource Integrity (SRI) and Content Security Policy (CSP) provides a critical layer of defense-in-depth even without a backend. For ORCID images, adding `referrerpolicy="no-referrer"` is a specific privacy enhancement for research profiles.

**Prevention:** Always include SRI for CDN assets and use a CSP. Ensure all `target="_blank"` links have `rel="noopener noreferrer"`.
