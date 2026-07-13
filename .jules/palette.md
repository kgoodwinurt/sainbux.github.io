## 2026-07-13 - Icon-Only Accessibility and Interaction Pattern
**Learning:** Icon-only social links in this project lacked accessible names (aria-label) and visual focus indicators, making them unusable for screen reader and keyboard users. Additionally, static icons provide no feedback on interaction.
**Action:** Always provide `aria-label` and `title` for icon-only links. Implement `:focus-visible` with an outline-offset to ensure clear keyboard navigation. Apply subtle CSS transitions (e.g., `translateY` and color change) to provide visual delight and feedback on hover.
