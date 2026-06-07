## 2026-06-07 - Layout shift and LCP optimization
**Learning:** Adding explicit width/height and fetchpriority to critical assets like the profile image significantly improves CLS and LCP, even on simple static sites. Font Awesome icon loading can be a bottleneck; using preconnect and SRI is essential for both performance and security.
**Action:** Always audit critical images for missing dimensions and ensure CDNs are preconnected.
