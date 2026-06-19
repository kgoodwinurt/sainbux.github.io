## 2026-06-19 - Accessibility and Navigation Polish
**Learning:** Icon-only links (like social media icons) are a common accessibility bottleneck in personal portfolios. Adding ARIA labels is a low-effort, high-impact fix. Smooth scrolling improves UX but MUST respect `prefers-reduced-motion` to avoid causing vestibular issues for sensitive users.
**Action:** Always check for aria-label on icons and ensure scroll-behavior: smooth is paired with a media query query for reduced motion. Use #007bbd instead of #009fdf for better contrast against white backgrounds.
