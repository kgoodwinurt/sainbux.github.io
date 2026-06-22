## 2025-06-22 - Avoid audit scripts in repository root
**Learning:** Adding large audit scripts with external dependencies to a simple static project's root is considered "over-reaching" and adds technical debt.
**Action:** Keep verification scripts in `/home/jules/verification/` and ensure they are not committed to the repository root.
