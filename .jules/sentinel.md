## 2026-06-16 - Hardening Static Portfolio Site
**Vulnerability:** XSS, Tabnabbing, and Resource Integrity Risks.
**Learning:** Even a static site needs security headers like CSP. Browsers ignore `frame-ancestors` in `<meta>` tags. ORCID icons may use multiple subdomains (`orcid.org`, `info.orcid.org`), requiring both in `img-src`.
**Prevention:** Always implement CSP, SRI for CDNs, and `rel="noopener noreferrer"` for external links. Verify CSP with a browser-based tool (like Playwright) to catch blocked resources.
