## 2025-05-14 - Implementing Defense-in-Depth for Static Sites

**Vulnerability:** Lack of security headers (CSP), missing Subresource Integrity (SRI) on CDNs, and potential tabnabbing/referrer leakage on external links.

**Learning:** For static sites hosted on platforms like GitHub Pages, security headers cannot be configured via server configuration files (e.g., .htaccess or nginx.conf). They must be enforced via `<meta>` tags within the HTML `<head>`. Additionally, 'unsafe-inline' was required in the CSP to support the project's existing practice of using internal style blocks and inline styles for responsiveness.

**Prevention:** Always include a CSP `<meta>` tag in the `<head>` of all HTML files. Use SRI hashes for all external scripts and styles to prevent supply chain attacks. Ensure all external links with `target="_blank"` include `rel="noopener noreferrer"`.
