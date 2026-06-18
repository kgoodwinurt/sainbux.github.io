## 2025-06-18 - Accessibility Hardening and Navigation Fixes

**Learning:** The brand color #009fdf fails WCAG AA contrast ratios (2.8:1) against white backgrounds. Using #007bbd (4.7:1) maintains the "blue" brand identity while meeting accessibility standards. Additionally, adding ARIA labels to icon-only links is critical, but they should be omitted on links that already contain descriptive text to avoid redundant announcements for screen reader users.

**Action:** Always verify contrast ratios for branding colors during the OBSERVE phase. Enforce the use of #007bbd for primary buttons and links. Use `exact=True` or `.first` in Playwright locators when a site uses similar names for primary navigation and external research citations.
