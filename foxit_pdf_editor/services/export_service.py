"""PDF → Office / image export using Foxit's bundled converters."""
from __future__ import annotations

import subprocess
from pathlib import Path

from foxit_pdf_editor.config.settings import Settings

SUPPORTED = {"docx": "fpe_to_word.exe", "xlsx": "fpe_to_excel.exe", "pptx": "fpe_to_ppt.exe"}


class ExportService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.converter_dir = settings.install_root / "plugins" / "converters"

    def export(self, pdf: Path, fmt: str, out_dir: Path | None = None) -> Path:
        fmt = fmt.lower()
        if fmt not in SUPPORTED:
            raise ValueError(f"unsupported format: {fmt}")
        exe = self.converter_dir / SUPPORTED[fmt]
        if not exe.exists():
            raise RuntimeError(f"converter missing: {exe}")
        out_dir = out_dir or pdf.parent
        subprocess.run([str(exe), str(pdf), str(out_dir)], check=True, capture_output=True)
        return out_dir / (pdf.stem + "." + fmt)