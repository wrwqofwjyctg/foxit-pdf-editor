"""Application bootstrap for the patched Foxit PDF Editor desktop shell."""
from __future__ import annotations

import sys
from pathlib import Path

from loguru import logger
from PyQt6.QtWidgets import QApplication

from foxit_pdf_editor.config.settings import load_settings
from foxit_pdf_editor.core.license_bypass import LicenseBypass
from foxit_pdf_editor.services.document_service import DocumentService
from foxit_pdf_editor.ui.main_window import MainWindow


def bootstrap() -> int:
    settings = load_settings()
    logger.add(settings.log_path, rotation="5 MB", retention=3, level=settings.log_level)
    logger.info("foxit-pdf-editor {} starting", settings.build_tag)

    bypass = LicenseBypass.from_settings(settings)
    if not bypass.apply():
        logger.warning("license bypass soft-failed; continuing in trial-stub mode")

    doc_service = DocumentService(settings)
    app = QApplication(sys.argv)
    win = MainWindow(settings=settings, doc_service=doc_service)
    win.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(bootstrap())