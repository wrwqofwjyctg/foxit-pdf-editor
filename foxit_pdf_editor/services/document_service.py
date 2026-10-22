"""Document open/save/merge service backed by pikepdf + pypdf."""
from __future__ import annotations

from pathlib import Path

import pikepdf
from loguru import logger

from foxit_pdf_editor.config.settings import Settings


class DocumentService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._cache: dict[Path, pikepdf.Pdf] = {}

    def open(self, path: Path) -> pikepdf.Pdf:
        if path in self._cache:
            return self._cache[path]
        pdf = pikepdf.open(path)
        self._cache[path] = pdf
        logger.debug("opened {} ({} pages)", path.name, len(pdf.pages))
        return pdf

    def merge(self, sources: list[Path], out: Path) -> Path:
        merged = pikepdf.Pdf.new()
        for src in sources:
            with pikepdf.open(src) as pdf:
                merged.pages.extend(pdf.pages)
        merged.save(out)
        merged.close()
        return out

    def strip_restrictions(self, path: Path, out: Path | None = None) -> Path:
        pdf = self.open(path)
        try:
            del pdf.Root.Perms
        except (AttributeError, KeyError):
            pass
        target = out or path.with_stem(path.stem + "_unlocked")
        pdf.save(target, encryption=None)
        return target

    def close(self) -> None:
        for pdf in self._cache.values():
            pdf.close()
        self._cache.clear()