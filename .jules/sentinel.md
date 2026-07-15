## 2026-07-15 - Hardening Static Site with CSP and SRI
**Vulnerability:** Lack of Content Security Policy (CSP), missing Subresource Integrity (SRI) on CDN assets, and unprotected external links (tab-nabbing).
**Learning:** Even simple static sites benefit from defense-in-depth. In this project, an ORCID badge image was served from 'info.orcid.org', which necessitated an explicit whitelist entry in the CSP distinct from 'orcid.org'.
**Prevention:** Always verify CSP implementation with automated tools like Playwright to catch cross-subdomain violations. When performing bulk updates with 'sed' to add security attributes, verify that existing attributes aren't duplicated or incorrectly merged.
