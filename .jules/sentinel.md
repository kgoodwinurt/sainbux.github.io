# Sentinel Journal

## 2025-07-03 - Initial Security Assessment
**Vulnerability:** Lack of Content Security Policy (CSP), missing Subresource Integrity (SRI) for external CSS, and missing security attributes on external links and images.
**Learning:** Static HTML sites often overlook defense-in-depth headers and attributes because they don't have a backend to set them. However, meta tags and HTML attributes can provide significant protection against XSS, resource hijacking, and tabnabbing.
**Prevention:** Always implement CSP via meta tags for static sites and ensure all external resources have SRI hashes.
