# Bolt's Performance Journal

## 2025-07-19 - Font Awesome and LCP Optimization
**Learning:** Relocating Font Awesome stylesheet to `<head>` and adding a preconnect link for `cdnjs.cloudflare.com` drastically reduces DocumentContentLoaded (DCL) times. Adding `fetchpriority="high"`, `width`, and `height` to the `profile.jpg` image optimizes the Largest Contentful Paint (LCP) and prevents Cumulative Layout Shift (CLS).
**Action:** Always place resource hint `preconnect` links immediately before critical stylesheets, relocate style dependencies to the `<head>` to prevent render blocking/FOUC, and specify image dimensions alongside fetch priorities on critical top-of-page image elements.
