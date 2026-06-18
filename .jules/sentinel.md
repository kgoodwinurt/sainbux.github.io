## 2025-06-18 - Hardening Static HTML Portfolio
**Vulnerability:** Lack of security headers (CSP), missing SRI for CDNs, and potential tab-nabbing (noopener).
**Learning:** Static sites on GitHub Pages benefit significantly from a meta-tag based CSP even if headers aren't configurable. Subresource Integrity (SRI) is critical for CDN-hosted assets like Font Awesome.
**Prevention:** Use binary mode ('rb'/'wb') in Python scripts for text replacement in this repository to avoid corrupting CRLF line endings or non-ASCII characters. Always verify SRI hashes directly from the source using `curl` and `openssl`.
