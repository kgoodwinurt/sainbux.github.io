# Palette UX/Accessibility Journal

## 2025-10-24 - Interactive Accessibility and Color Contrast Enhancements
**Learning:** Legacy focus outlines and color contrast ratios often violate accessibility guidelines. Applying a consistent `:focus-visible` ring across interactive elements (buttons, navigation, social links) ensures keyboard navigating users have a highly visible indicator. Moreover, upgrading key buttons/links to a compliant color like `#007bbd` from legacy `#009fdf` achieves a WCAG AA contrast ratio (> 4.5:1) without compromising the design system.
**Action:** Always combine interactive state styling (:hover, :focus-visible) and ensure semantic icon-only elements feature explicit screen-reader accessible attributes (`aria-label`).
