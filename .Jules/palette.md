## 2026-06-23 - [Accessibility and Navigation Hardening]
**Learning:** Icon-only social links are common accessibility gaps in personal portfolios. Adding `aria-label` and `title` provides multi-modal clarity (screen readers + tooltips). Also, internal anchors in multi-page static sites must be qualified with the page name (e.g., `index.html#id`) when referenced from other pages to prevent broken navigation.
**Action:** Always audit icon-only elements for ARIA labels and ensure cross-page anchor links are fully qualified.
