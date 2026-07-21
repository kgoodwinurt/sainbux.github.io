## 2025-11-01 - Color Contrast AA Compliance for Interactive Elements
**Learning:** Legacy primary button background color (#009fdf) fails WCAG AA color contrast check (~3.1:1 ratio) against white background. Updating to #007bbd ensures compliance with a contrast ratio of 4.54:1 while maintaining a cohesive brand aesthetic.
**Action:** Always verify contrast ratios for new brand or primary colors against white/light backgrounds, preferring AA-compliant alternatives like #007bbd.

## 2025-11-01 - Targeting Icon-Only Links in Portfolio Navigations
**Learning:** When adding hover lift/translate effects specifically to icon-only social links, applying the styling to text-based social links (e.g., inline professional profiles in about.html) degrades readability. Direct class mapping via specific CSS classes like `.social-icon` prevents text misalignment.
**Action:** Avoid bulk regex or global styling on social domains. Explicitly use a dedicated CSS class like `.social-icon` on icon-only anchors, leaving inline text anchors unstyled.
