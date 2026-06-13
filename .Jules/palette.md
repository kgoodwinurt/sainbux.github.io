## 2025-05-14 - [Color Contrast & ARIA Redundancy]
**Learning:** The brand color #009fdf (light blue) fails WCAG AA contrast (2.8:1) against white text. Switching to #007bbd (darker blue) achieves 4.5:1 while maintaining brand feel. Also, adding aria-labels to links that already have text content creates redundancy for screen readers.
**Action:** Always check contrast of brand colors in buttons. Use aria-labels ONLY for icon-only or ambiguous interactive elements.
