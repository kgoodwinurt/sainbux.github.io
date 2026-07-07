## 2026-07-07 - Accessibility and Micro-interactions
**Learning:** Icon-only social links are inaccessible to screen reader users if they lack descriptive `aria-label` and `title` attributes. Additionally, using `:focus-visible` ensures that keyboard users have a clear visual indicator of their current position without cluttering the UI for mouse users.
**Action:** Always provide `aria-label` and `title` for icon-only links and implement clear `:focus-visible` styles using `outline-offset` for better visibility.
