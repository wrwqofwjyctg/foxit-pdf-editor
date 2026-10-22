"""Runtime settings loader for the patched Foxit PDF Editor."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(dotenv_path=Path.home() / ".foxit-pdf-editor" / ".env", override=False)


@dataclass(slots=True)
class Settings:
    build_tag: str = "2026.4.2-patched"
    install_root: Path = field(default_factory=lambda: Path(os.environ.get(
        "FOXIT_INSTALL_ROOT", r"C:\Program Files\Foxit Software\Foxit PDF Editor")))
    patch_dir: Path = field(default_factory=lambda: Path(os.environ.get(
        "FOXIT_PATCH_DIR", r"C:\Program Files\Foxit Software\Foxit PDF Editor\plugins\fpm")))
    license_store: Path = field(default_factory=lambda: Path.home() / ".foxit-pdf-editor" / "licenses")
    log_path: Path = field(default_factory=lambda: Path.home() / ".foxit-pdf-editor" / "foxit.log")
    log_level: str = "INFO"
    enable_ocr: bool = True
    enable_cloud_sync: bool = False
    plugin_dirs: list[Path] = field(default_factory=list)


def load_settings() -> Settings:
    s = Settings()
    s.log_path.parent.mkdir(parents=True, exist_ok=True)
    s.license_store.mkdir(parents=True, exist_ok=True)
    if os.environ.get("FOXIT_ENABLE_OCR", "1") == "0":
        s.enable_ocr = False
    if os.environ.get("FOXIT_CLOUD", "0") == "1":
        s.enable_cloud_sync = True
    return s