# Nexum Audio website

Seven English static pages: the suite overview, five product pages and Open Source.
The November 2026 update includes current development screenshots, Nexum Rec and
Windows packages with matching full source snapshots. Demo waveforms use synthetic
audio; private recordings and external preset packs are not included.

Open index.html locally, or serve this directory with a static HTTP server.
Shared styles: assets/style.css. Interactions: assets/site.js. No frontend build,
external fonts, tracking or accounts are required to browse the site.

Checks: `python tools/check-site.py` and `node --check assets/site.js`.
Download checksums and source commit IDs are stored in downloads/releases.json.
The source ZIP includes the shared core and dependency sources once. Its README
explains the NEXUM_CORE_DIR override for companion builds.

GitHub Pages deployment is maintained by .github/workflows/static.yml. Keep the
existing Pages audience and domain settings. Pushes require explicit owner request;
use nexum-audio as author, committer and authenticated account.
