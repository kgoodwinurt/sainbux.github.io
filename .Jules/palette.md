## 2026-06-24 - Navigation and Accessibility Enhancements
**Learning:** Found that internal anchor links (like #research) in the navigation bar break when the user navigates to a different page (about.html) where the target section doesn't exist.
**Action:** Always use absolute-path-style relative links (index.html#research) in shared navigation components to ensure they work from any page.

**Learning:** Redundant CSS blocks (duplicate body and section selectors) increase file size without benefit.
**Action:** Consolidate CSS rules into single selectors to maintain clean code and improve maintainability.
