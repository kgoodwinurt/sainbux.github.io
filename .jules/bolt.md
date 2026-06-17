## 2026-06-17 - [Optimize LCP and critical resource loading]
**Learning:** Moving external stylesheets from <body> to <head> prevents Flash of Unstyled Content (FOUC) and ensures they are discovered early by the browser's preload scanner. Adding `fetchpriority="high"` and explicit dimensions to the Largest Contentful Paint (LCP) image significantly improves performance metrics and prevents Cumulative Layout Shift (CLS).
**Action:** Always place critical external resources in the <head> with `rel="preconnect"` and optimize the primary LCP element with `fetchpriority="high"`.
