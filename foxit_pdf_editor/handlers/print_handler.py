"""Windows print spooler hook — routes Foxit PDF Printer jobs to the patched driver."""
from __future__ import annotations

import win32print
from loguru import logger

from foxit_pdf_editor.config.settings import Settings

PATCHED_PRINTER = "Foxit PDF Editor Printer (patched)"


class PrintHandler:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def default_printer(self) -> str:
        return win32print.GetDefaultPrinter()

    def ensure_patched_printer(self) -> bool:
        printers = [p[2] for p in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)]
        if PATCHED_PRINTER in printers:
            return True
        logger.warning("patched printer '{}' not registered — reinstall driver pack", PATCHED_PRINTER)
        return False