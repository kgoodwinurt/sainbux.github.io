## 2026-07-07 - Social Link Hardening and CSP
**Vulnerability:** External links lacked `noopener noreferrer`, potentially exposing the site to tabnabbing. The site also lacked a Content Security Policy (CSP), making it vulnerable to XSS.
**Learning:** For static sites, a CSP can be effectively implemented via a `<meta>` tag. The `rel="me"` attribute is also essential for decentralized identity verification on platforms like Mastodon.
**Prevention:** Implement CSP `<meta>` tags as a standard security layer and always use `rel="me noopener noreferrer"` for external social media links.
