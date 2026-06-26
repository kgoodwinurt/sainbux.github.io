## 2026-06-26 - Securing Named External Targets
**Vulnerability:** Reverse tabnabbing risk on named targets.
**Learning:** External links using named targets (e.g., `target="orcid.widget"`) are susceptible to reverse tabnabbing just like `target="_blank"`. Attackers on the destination page can use `window.opener` to redirect the source page to a malicious site.
**Prevention:** Always apply `rel="noopener noreferrer"` to any link that opens in a new browsing context, regardless of whether the target name is `_blank` or a custom string.
