## 2026-07-01 - Accessible Social Links and Color Contrast

**Learning:** Icon-only social links require explicit `aria-label` and `title` attributes for accessibility. Furthermore, a custom `.social-link` class providing both visual (hover transform) and keyboard (focus-visible outline) feedback ensures a pleasant experience for all users. The legacy primary button color (#009fdf) had insufficient contrast (approx 3:1), which was improved by switching to #007bbd (approx 4.6:1), meeting WCAG AA standards.

**Action:** Use the `.social-link` class for all icon-only social media integrations and prioritize WCAG AA compliant colors for interactive elements.
