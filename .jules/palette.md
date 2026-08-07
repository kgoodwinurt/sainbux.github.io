# Palette Journal - Critical UX & Accessibility Learnings

## 2025-02-18 - Keyboard Interactivity & High Contrast on Static Pages
**Learning:** For pure HTML/CSS portfolio sites, keyboard accessibility requires a unified focus state strategy across diverse elements like buttons, navigation anchors, and icon-only social links. In addition, replacing legacy interactive colors with WCAG AA compliant variations (e.g., `#007bbd` instead of `#009fdf`) drastically improves readability without altering the visual language.
**Action:** Always verify keyboard navigation outlines (`:focus-visible`) and `aria-label` attributes on icon-only interactive controls, and utilize WCAG-compliant color choices on white backgrounds.
