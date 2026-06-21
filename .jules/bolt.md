## 2026-06-21 - SRI Hash Verification for Font Awesome 6.4.0
**Learning:** Reviewer suggested the SRI hash for Font Awesome 6.4.0 was incorrect, which could break the site. Verification via curl and openssl confirmed the hash `sha384-iw3OoTErCYJJB9mCa8LNS2hbsQ7M3C0EpIsO/H5+EGAkPGc6rk+V8i04oW/K5xq0` is indeed correct for the cdnjs asset.
**Action:** Always verify SRI hashes from the source CDN before committing to avoid regressions and confidently address review feedback.
