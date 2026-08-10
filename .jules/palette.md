# Palette UX & Accessibility Journal

## 2026-08-10 - Keyboard Interactivity and WCAG-Compliant Focus/Hover Styles

**Learning:** Icon-only social links must use descriptive `aria-label` attributes to be perceivable by screen readers. Furthermore, adding clear focus indicators using `:focus-visible` ensures keyboard-only users can navigate seamlessly. Using `#007bbd` instead of the legacy `#009fdf` achieves a WCAG AA-compliant color contrast of 4.54:1 against a light background, enhancing readability and inclusive design.

**Action:** Standardize primary buttons, navigation links, and `.social-icon` classes to share cohesive CSS transitions (`transform: translateY(-3px)`) and a distinct `:focus-visible` outline pattern (`outline: 2px solid #007bbd; outline-offset: 4px;`) across all static pages in the codebase.
