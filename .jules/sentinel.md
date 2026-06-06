## 2025-05-15 - [Subresource Integrity and Tabnabbing Protection]
**Vulnerability:** External CDNs can be compromised to serve malicious scripts/styles, and external links with `target="_blank"` are vulnerable to tabnabbing if `rel="noopener noreferrer"` is missing.
**Learning:** Always verify SRI hashes using reliable methods (like `curl | openssl`). Manually copied hashes can be incorrect and break site functionality.
**Prevention:** Use a script to verify SRI hashes for all external resources and ensure all external links have the proper `rel` attributes.
