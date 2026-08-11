# Sentinel Security Journal

Journal of critical security learnings for this repository.

## 2025-08-11 - Content Security Policy Hardening & Markdown Link Protection
**Vulnerability:** Weak CSP policy allowing plugin content execution (`object-src` undefined/unsafe) and mixed content protocol downgrades; unvalidated target="_blank" HTML anchor tags in `README.md` introducing potential reverse-tabnabbing exploits (unauthorized access of opener window).
**Learning:** Standard static hosting setups without HTTP header configurations rely heavily on the HTML `<meta>` tag CSP representation. Leaving directives like `object-src` blank defaults to permissive rules, leaving the app open to legacy object-based injections. Furthermore, while automated tools handle `target="_blank"` link protection for typical Markdown syntax, explicit HTML anchor syntax in Markdown files is often skipped and must be checked separately.
**Prevention:** Always restrict legacy object/embed plugins with `object-src 'none';` and enforce HTTPS upgrade transitions using `upgrade-insecure-requests;` within Content Security Policy meta definitions. Programmatically scan custom HTML link structures in `README.md` files to ensure they consistently utilize `rel="noopener noreferrer"`.
