## 2026-06-14 - [Social Links Accessibility]
**Learning:** Icon-only social media links without ARIA labels are inaccessible to screen reader users, providing no context for the link's destination.
**Action:** Always add descriptive `aria-label` attributes (e.g., "Facebook", "LinkedIn") to icon-only links and ensure external links use `rel="noopener noreferrer"` for security.
