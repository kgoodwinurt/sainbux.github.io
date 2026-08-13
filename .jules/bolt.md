# Bolt Performance Journal

## 2026-08-13 - CDN Stylesheet Preconnect & Relocation
**Learning:** Moving render-blocking CDN assets (such as the Font Awesome CSS stylesheet) from the body to the head, coupled with a preceding preconnect resource hint to `https://cdnjs.cloudflare.com` with `crossorigin`, drastically reduces DocumentContentLoaded (DCL) times by establishing early TLS connections and preventing parsed body content rendering blocks.
**Action:** Always preconnect to external CDN origins and locate essential styling links in the document `<head>` to minimize critical path rendering latency.
