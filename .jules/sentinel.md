## 2025-05-15 - Defense in Depth: External Resource Security
**Vulnerability:** Tabnabbing risk from `target="_blank"` links without `rel="noopener noreferrer"` and potential for CDN-based XSS/Tampering without Subresource Integrity (SRI).
**Learning:** Static sites often rely on external CDNs and social links which are easy targets for minor but impactful security gaps if basic attributes are missing. Multi-line HTML tags can be easily missed by simple regex search-and-replace scripts.
**Prevention:** Standardize a pre-commit check or linter rule to enforce `rel="noopener noreferrer"` and SRI for all external assets. Use `re.DOTALL` or similar flags when using regex to process HTML to handle multi-line tags correctly.
