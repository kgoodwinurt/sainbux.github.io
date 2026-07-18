## 2026-07-18 - Eliminating External Asset Redirect Chains
**Learning:** External badges/logos (such as the ORCID icon) on static landing pages are prone to silent URL updates over time. These can result in multi-step redirect chains (e.g., orcid.org -> info.orcid.org -> info.orcid.org/wp-content/...) that add multiple DNS/TCP/TLS and HTTP redirect roundtrips on initial page load, harming Critical Rendering Path performance.
**Action:** Inspect and audit third-party badges, logos, and scripts during optimization cycles to ensure they target direct, canonical, and final asset URLs.
