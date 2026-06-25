## 2026-06-25 - [Accessibility and Navigation Polish]
**Learning:** Redundant ARIA labels on text links (e.g., `<a aria-label="LinkedIn">LinkedIn</a>`) add unnecessary verbosity for screen readers and can lead to inconsistent styling if not applied uniformly across a list. Icon-only links, however, REQUIRE aria-labels to be accessible.
**Action:** Only add `aria-label` to icon-only interactive elements. For text links, ensure the text itself is descriptive. Ensure any style updates to links in a list are applied consistently to all siblings to maintain visual harmony.
