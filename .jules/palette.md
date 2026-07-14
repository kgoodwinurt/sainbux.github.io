## 2026-07-14 - Selective Application of Interactive Styles
**Learning:** In pages with multiple links to the same social destination (e.g., a text link in bio and an icon in the footer), broad attribute-based selectors or naive search-and-replace can incorrectly apply interactive "lift" effects (.social-icon) to inline text. This disrupts line height and causes visual jank.
**Action:** Restrict interactive classes to dedicated containers or use precise selectors that distinguish between icon-only anchors and inline text anchors.
