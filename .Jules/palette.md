## 2026-06-26 - Accessible Social Links and Navigation Consistency
**Learning:** Icon-only social links in this project lacked descriptions for screen readers and security attributes. Additionally, anchor links between pages must include the target filename (e.g., `index.html#research`) to avoid broken navigation in static environments.
**Action:** Always verify icon-only elements have `aria-label` and ensure cross-page anchor links are fully qualified with the page path.
