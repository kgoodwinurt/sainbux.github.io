## 2025-05-22 - [Security Improvement] Enhancing Subresource Integrity and External Link Security

**Vulnerability:** Missing Subresource Integrity (SRI) for external CSS and missing `rel="noopener noreferrer"` on external links.
**Learning:** External assets loaded from CDNs without SRI can be a vector for supply chain attacks. External links without `rel="noopener noreferrer"` are vulnerable to reverse tabnabbing.
**Prevention:** Always use SRI for external resources and include security attributes for all links that open in a new tab.
