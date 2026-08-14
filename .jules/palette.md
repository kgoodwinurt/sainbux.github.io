# Palette UX and Accessibility Journal

## 2026-08-14 - Scoping Icon-Only Social Classes VS Inline Text Links
**Learning:** Icon-only social links benefit greatly from active interactivity enhancements (like `.social-icon` lift effects via `transform: translateY(-3px)` and focus-visible indicators). However, applying these micro-interactions or margins to text-based social links (such as "LinkedIn" text inline anchors in bio sections) breaks visual consistency, vertical alignment, and text line-height flow.
**Action:** Always scope interactive lift styles, size adjustments, and structural padding/margin changes explicitly to the `.social-icon` class. Apply this class only to icon-only links containing visual icons (such as Font Awesome elements), keeping text-only social links as clean, standard inline anchors.
