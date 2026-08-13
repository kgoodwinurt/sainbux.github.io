# Palette UX Journal

Journal of critical UX and accessibility learnings for this repository.

## 2026-03-06 - Accessible Icon-Only Social Anchors and Focus Indicators
**Learning:** Icon-only link anchors built solely with font-awesome icons are completely invisible to screen readers without an `aria-label` attribute, presenting a major accessibility barrier. Furthermore, relying on default browser focus rings is insufficient, as custom dark backgrounds (e.g. in footers or styled sections) can make standard outlines invisible.
**Action:** Always provide explicit, translated `aria-label` tags on all icon-only buttons/anchors and define high-contrast, custom `:focus-visible` style rings featuring distinct outlines and outline offsets (e.g., `2px solid #007bbd` outline with `4px` offset) to guarantee clear focus visibility across all user interactions and color themes.
