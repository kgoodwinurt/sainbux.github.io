# Palette UX & Accessibility Journal

Journal of critical UX and accessibility learnings for this repository.

## 2025-08-09 - [Keyboard Interactivity & WCAG Contrast Alignment]
**Learning:** Legacy UI element styles such as custom outline resets on interactive items often bypass system-level focus highlights, violating accessibility standards (WCAG 2.1 Success Criterion 2.4.7 - Focus Visible). Additionally, color choices like `#009fdf` on white backgrounds provide insufficient contrast (around 3.1:1), falling short of the AA target ratio (4.5:1).
**Action:** Consolidate active elements to adhere to standard focus rings (`:focus-visible` with `#007bbd` and positive offset) and upgrade primary actionable buttons to use the AA contrast-compliant `#007bbd` color. Ensure icon-only interactive links are fully augmented with semantic `aria-label` attributes and interactive transition wrappers (`.social-icon`).
