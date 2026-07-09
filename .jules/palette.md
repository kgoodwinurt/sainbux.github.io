## 2026-07-09 - Accessibility & Navigation Polish

**Learning:** The legacy primary button color (#009fdf) had a contrast ratio of ~2.9:1, failing WCAG AA standards. Switching to #007bbd (4.61:1) ensures accessibility without sacrificing the brand's blue aesthetic. Additionally, internal fragment links in sub-pages (e.g., #research in about.html) often break when the target section only exists on the home page.

**Action:** Always verify contrast ratios for primary UI elements. Ensure sub-page navigation links use absolute paths (index.html#section) for home-page-only sections. Use .social-icon class for interactive icon-only links to centralize hover/focus-visible behaviors.
