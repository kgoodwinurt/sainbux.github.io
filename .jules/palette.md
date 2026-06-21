# Palette Journal - UX & Accessibility Learnings

## 2026-06-21 - Accessible Icon Links and Color Contrast Compliance
**Learning:** Icon-only links without ARIA labels are invisible to screen readers, and brand colors like #009fdf often fail WCAG contrast requirements on white backgrounds.
**Action:** Always provide descriptive `aria-label` attributes for icon-only components and verify color contrast ratios for primary interaction elements early in the development process.
