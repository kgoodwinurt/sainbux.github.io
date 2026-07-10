# Palette's Journal - Critical UX/Accessibility Learnings

## 2026-07-10 - Improving Interactive Elements Contrast and Feedback

**Learning:** Buttons with low contrast (e.g., #009fdf on white) fail WCAG AA standards, making them hard to read for users with visual impairments. Additionally, icon-only social links lack semantic meaning for screen readers without proper ARIA labels and titles.

**Action:** Always use high-contrast colors (e.g., #007bbd) for interactive elements and ensure all icon-only buttons have descriptive `aria-label` and `title` attributes. Implement clear `:focus-visible` states to support keyboard navigation.
