# Palette Journal - Critical UX/Accessibility Learnings

## 2025-07-07 - Enhanced Accessibility for Social Links
**Learning:** Icon-only social media buttons require descriptive `aria-label` and `title` attributes to be accessible to screen reader users and provide hover context. Using a WCAG AA compliant color like `#007bbd` (4.61:1 contrast) instead of legacy colors like `#009fdf` (~3:1) ensures readability for all users.
**Action:** Apply `aria-label`, `title`, and compliant color contrast to all interactive social links; use `.social-link` class for consistent interactivity.
