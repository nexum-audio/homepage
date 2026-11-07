# Nexum Audio — local website

Open index.html directly in your browser. All six pages, navigation, product
previews and downloads work without a build step, web server or internet access.

## Pages
- index.html: suite overview, product previews, downloads and installation FAQ
- nexum.html, fx.html, tune.html, gate.html: individual product pages
- open-source.html: shared codebase, licenses and build instructions

## Editing
Page content is stored directly in the HTML files. Shared styling is in
assets/style.css; interactions are in assets/site.js. The assets folder also
contains logos, mockups and plugin screenshots. No external fonts, trackers,
account systems, form services or frontend frameworks are loaded.

The optional tools/ scripts regenerate pages and release ZIPs from the local
development projects. build-pages.py applies the English translation pass
automatically. No scripts are needed to browse or host the website.

## Downloads
Four Windows x64 ZIPs include VST3, standalone, README and license texts. The
shared source ZIP contains all four products, shared UI, JUCE, Rubber Band,
Zstandard, Catch2, tests and relative CMake paths. Original implementation:
AGPL-3.0-only, authorized by the project owner. Third-party licenses are retained.
External sound packs, private DAW projects and user settings are not included.
Checksums: downloads/SHA256SUMS.txt. Metadata: downloads/releases.json.

## Hosting later on nexum-audio.com
Copy the six HTML pages together with assets/ and downloads/ into the web root.
Links are relative and there are no server dependencies. README.md and tools/
do not need to be uploaded. Nothing has been deployed; domain/DNS settings
have not been changed.

## Verification
Desktop/mobile browser checks, interactive preview, mobile navigation, image
zoom, code copying and an actual Windows download were tested. Local links and
anchors, ZIP integrity and SHA-256 checksums were checked. Source CMake paths
were checked for portability; the archive has not been fully rebuilt from scratch.
