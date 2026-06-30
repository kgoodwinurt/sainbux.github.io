## 2026-06-30 - Accessible Interactive Social Links
**Learning:** Icon-only social links require explicit `aria-label` and `title` attributes for accessibility, while the nested icon should be hidden from screen readers. Using `rel="me"` is a standard for decentralized identity verification.
**Action:** Always wrap social icons in an anchor with `aria-label`, `title`, and `rel="me noopener noreferrer"`, and mark the `<i>` tag with `aria-hidden="true"`. Use `:focus-visible` for keyboard navigation indicators.

## 2026-06-30 - Color Contrast Compliance
**Learning:** Brand colors often fail WCAG AA contrast ratios (4.5:1 for normal text). The original `#009fdf` (~2.8:1) was insufficient for accessibility.
**Action:** Use `#007bbd` (~4.6:1) as a compliant alternative to light blue brand colors to ensure readability for all users.
