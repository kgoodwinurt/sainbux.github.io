## 2026-06-20 - [Accessibility & Feedback]
**Learning:** The legacy branding color #009fdf (contrast ratio 3.12:1) fails WCAG AA against white backgrounds for small text. Replacing it with #007bbd (contrast ratio 4.61:1) ensures accessibility while maintaining brand identity.
**Action:** Always use #007bbd for primary interactive elements in this design system.

**Learning:** Smooth scrolling combined with visible focus indicators significantly improves the perceived quality and usability of static single-page layouts.
**Action:** Reuse the 'scroll-behavior: smooth' and ':focus-visible' pattern with #007bbd outline for all new interactive pages.
