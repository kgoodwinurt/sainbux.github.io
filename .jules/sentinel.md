## 2025-05-15 - Improving Subresource Integrity and Link Security
**Vulnerability:** Missing SRI on external CSS and missing \`rel="noopener noreferrer"\` on links with \`target="_blank"\`.
**Learning:** External assets from CDNs pose a supply-chain risk if not verified with SRI. Links opening in new tabs without protection are vulnerable to reverse tabnabbing.
**Prevention:** Always enforce SRI for CDN resources and ensure \`rel="noopener noreferrer"\` is applied to all external links.
