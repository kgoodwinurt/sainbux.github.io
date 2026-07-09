## 2026-07-09 - Harden Static Pages with CSP, SRI, and Secure Links

**Vulnerability:**
The static site was missing modern security headers (CSP), had no integrity verification for third-party scripts (SRI), and external links lacked protection against tab-nabbing. External images also leaked the referring URL.

**Learning:**
Static sites can significantly improve their security posture using only HTML `<meta>` and attribute-level enhancements. Content Security Policy (CSP) via `<meta>` tag provides a strong baseline, and Subresource Integrity (SRI) is crucial when relying on CDNs.

**Prevention:**
Always include a CSP meta tag in static HTML. Use SRI for all CDN-hosted assets. Ensure all external links (`target="_blank"`) have `rel="noopener noreferrer"`. Use `referrerpolicy="no-referrer"` for external resources to protect user privacy.
