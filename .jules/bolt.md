## 2026-06-24 - [Critical Path and Resource Loading Optimizations]
**Learning:** Moving CDN-hosted CSS to the <head> and preconnecting to the CDN domain significantly improves early resource discovery and prevents FOUC. Using fetchpriority="high" on LCP images (like the header profile pic) combined with explicit dimensions effectively reduces LCP and prevents CLS.

**Learning:** The codebase uses CRLF line endings (\r\n). Automated text replacements (sed, git-merge-diff) can fail if they don't account for these. Using Python in binary mode or explicitly matching \r\n is more robust for this environment.

**Action:** Always check line endings before performing multi-line regex or search-and-replace operations. Continue using fetchpriority and explicit dimensions for key above-the-fold images.
