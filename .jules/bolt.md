## 2025-06-09 - LCP and CLS Optimization for Profile Image
**Learning:** The `profile.jpg` image in the header is the primary LCP candidate. Relying on inline CSS for its dimensions instead of HTML attributes contributes to Cumulative Layout Shift (CLS) and delays browser-side space reservation.
**Action:** Always use HTML `width` and `height` attributes for static images to reserve aspect ratio and apply `fetchpriority="high"` for the critical profile image to optimize the loading waterfall.
