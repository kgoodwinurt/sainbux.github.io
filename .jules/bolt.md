# Bolt Performance Journal

This journal documents critical performance-related learnings, including bottlenecks, failed optimizations, and codebase-specific patterns.

## 2025-05-15 - [Critical Path and LCP Optimization]
**Learning:** The `profile.jpg` in the header is the primary LCP element for both `index.html` and `about.html`. It lacked explicit dimensions and high fetch priority, contributing to layout shift and slower LCP. Additionally, Font Awesome was being loaded late from the body.
**Action:** Always apply `fetchpriority="high"`, `width="150"`, and `height="150"` to the header profile image. Move the Font Awesome stylesheet to the `<head>` and use `rel="preconnect"` for `cdnjs.cloudflare.com` to optimize the critical rendering path.
