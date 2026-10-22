from __future__ import annotations

from pathlib import Path

DEFAULT_ROOT = Path(r"C:\Program Files\Foxit Software\Foxit PDF Editor")


def resolve_install_root(override: str | None = None) -> Path:
    if override:
        return Path(override)
    return DEFAULT_ROOT if DEFAULT_ROOT.exists() else Path.home() / "Foxit PDF Editor"