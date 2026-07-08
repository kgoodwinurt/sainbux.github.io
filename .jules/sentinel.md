## 2026-07-08 - Secure Link Attributes for Named Targets
**Vulnerability:** Tab-nabbing via named targets.
**Learning:** Standard security scanners often only check `target="_blank"`. However, named targets like `target="orcid.widget"` are equally vulnerable to tab-nabbing if they don't include `rel="noopener noreferrer"`.
**Prevention:** Always apply `rel="noopener noreferrer"` to any link with a `target` attribute, regardless of the target name.

## 2026-07-08 - CSP Meta Tag Placement
**Vulnerability:** Late enforcement of security policy.
**Learning:** The CSP meta tag should be placed as early as possible in the `<head>`, ideally right after the `<meta charset="UTF-8" />` tag. This ensures the policy is active before the browser begins fetching subsequent resources and keeps the charset within the first 1024 bytes.
**Prevention:** Standardize CSP placement immediately following the charset declaration in all HTML templates.
