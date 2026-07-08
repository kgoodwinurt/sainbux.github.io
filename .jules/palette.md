## 2026-07-08 - Interactive States for Text vs Icons
**Learning:** Applying visual "lift" (transform: translateY) to inline text links disrupts vertical alignment and creates visual jank. Standardized interactive feedback for text should focus on color and focus-visible outlines, while "lift" effects should be reserved for standalone icon elements.

**Action:** Created separate `.social-icon` class for standalone social media icons and used standard anchor styling for inline professional text links.

## 2026-07-08 - Context-Aware Navigation
**Learning:** In multi-page static sites, navigation links to shared sections (e.g., Contact) should remain local if the section exists on the current page. Forcing a redirect to the homepage for a section available locally creates an unnecessary and disruptive page reload.

**Action:** Restored local anchor link for `#contact` in `about.html` while maintaining `index.html#research` for sections not present on the sub-page.
