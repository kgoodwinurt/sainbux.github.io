# Palette UX Journal

Journal of critical UX and accessibility learnings for this repository.

## 2025-08-08 - Improving Social Icon and Primary Interactive Elements Contrast and Navigation
**Learning:** Icon-only social links and low-contrast elements like buttons styled with light blue colors (#009fdf) do not meet WCAG AA standards (4.5:1 ratio) on white/light backgrounds, and lack standard interactive visual lift. Also, keyboard navigators require a quick "skip to content" option to bypass repetitive header navigation, and clear `:focus-visible` styling is essential to show focus state without cluttering mouse user interactions.
**Action:** Replace light-blue button color `#009fdf` with a WCAG AA compliant `#007bbd`, add custom skip-to-content links targets, and implement the `.social-icon` class for subtle transform lift and transition hover/focus effects alongside matching 'aria-label' attributes.
