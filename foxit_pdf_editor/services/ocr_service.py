"""OCR service — wraps the patched OCR plugin shipped with Foxit PDF Editor."""
from __future__ import annotations

import subprocess
from pathlib import Path

from loguru import logger

from foxit_pdf_editor.config.settings import Settings


class OcrService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.ocr_exe = settings.install_root / "plugins" / "ocr" / "fpe_ocr.exe"

    def available(self) -> bool:
        return self.ocr_exe.exists()

    def run(self, pdf: Path, lang: str = "eng") -> Path:
        if not self.available():
            raise RuntimeError("OCR plugin missing — reinstall patched Foxit PDF Editor")
        out = pdf.with_stem(pdf.stem + f"_ocr_{lang}")
        cmd = [str(self.ocr_exe), "--input", str(pdf), "--lang", lang, "--output", str(out)]
        logger.info("running OCR: {}", " ".join(cmd))
        subprocess.run(cmd, check=True, capture_output=True)
        return out