## 2025-05-15 - Hardening External Resources and Links
**Vulnerability:** External resources (Font Awesome CDN) were missing Subresource Integrity (SRI) hashes, and external links opening in new tabs (`target="_blank"`) were missing `rel="noopener noreferrer"`.
**Learning:** Even static portfolio sites are vulnerable to CDN-based supply chain attacks and tabnabbing if basic security attributes are omitted. SRI ensures that the fetched resource matches a known-good hash, while `rel="noopener noreferrer"` prevents the destination page from gaining partial access to the source page via `window.opener`.
**Prevention:** Always enforce SRI for CDN resources and include `rel="noopener noreferrer"` for all external links using `target="_blank"` or custom targets.
