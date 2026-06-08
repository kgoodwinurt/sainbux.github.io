# Bolt's Performance Journal

## 2025-06-08 - Initializing Bolt Journal
**Learning:** This is a static site with inlined CSS, which is great for FCP. However, it lacks image dimensions and resource hints.
**Action:** Always check for missing `width`/`height` on images and use `rel="preconnect"` for third-party assets.

## 2025-06-08 - Responsiveness vs Inline Styles
**Learning:** Inline CSS `width` (e.g., `style="width: 150px"`) has higher specificity than CSS media queries, which can break mobile responsiveness. The HTML `width` attribute (e.g., `width="150"`) provides a base size that is easily overridden by CSS.
**Action:** Use HTML `width`/`height` attributes for CLS prevention and only use inline styles for non-responsive properties like `border-radius`.
