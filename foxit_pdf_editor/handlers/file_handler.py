"""Drag-and-drop / open-with file router."""
from __future__ import annotations

from pathlib import Path

from loguru import logger

from foxit_pdf_editor.services.document_service import DocumentService


class FileHandler:
    def __init__(self, doc_service: DocumentService) -> None:
        self.doc_service = doc_service

    def handle(self, paths: list[str]) -> list[Path]:
        opened: list[Path] = []
        for raw in paths:
            p = Path(raw)
            if p.suffix.lower() != ".pdf":
                logger.warning("ignoring non-PDF: {}", p)
                continue
            try:
                self.doc_service.open(p)
                opened.append(p)
            except Exception as e:  # noqa: BLE001
                logger.error("failed to open {}: {}", p, e)
        return opened