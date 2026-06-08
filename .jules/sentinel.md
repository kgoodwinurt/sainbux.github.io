## 2025-06-08 - Enhancing Frontend Security with rel and SRI
**Vulnerability:** Reverse Tabnabbing and potential CDN Compromise.
**Learning:** External links with `target="_blank"` without `rel="noopener noreferrer"` can allow the destination page to access the source page's `window.opener` object. Additionally, loading third-party assets from CDNs without Subresource Integrity (SRI) creates a risk of malicious code injection if the CDN is compromised.
**Prevention:** Always use `rel="noopener noreferrer"` for external links using `target="_blank"` and enforce SRI with `integrity` and `crossorigin="anonymous"` for all CDN resources.
