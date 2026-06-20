## 2025-05-14 - Initial Setup
**Learning:** The repository is a static HTML site with Font Awesome loaded at the bottom of the body, which delays icon rendering and causes FOUC. The primary LCP element (profile image) lacks optimization attributes. The <style> tags were also placed outside of the <head> tag.
**Action:** Prioritize critical path optimizations: move CSS to head, add preconnect, and optimize LCP image attributes. Ensure <style> blocks are correctly placed inside <head>.
