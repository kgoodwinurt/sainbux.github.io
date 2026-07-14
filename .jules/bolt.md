# Bolt's Performance Journal

## 2025-05-14 - Initial Assessment
**Learning:** This is a static site with critical rendering path issues. External CSS (Font Awesome) is loaded late in the body, and the LCP image lacks optimization attributes.
**Action:** Relocate critical assets to <head> and add resource hints.
