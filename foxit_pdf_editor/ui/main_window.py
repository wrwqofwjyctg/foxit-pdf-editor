"""Qt6 main window for the patched Foxit PDF Editor."""
from __future__ import annotations

from PyQt6.QtWidgets import QMainWindow, QStatusBar, QTabWidget, QWidget

from foxit_pdf_editor.config.settings import Settings
from foxit_pdf_editor.services.document_service import DocumentService


class MainWindow(QMainWindow):
    def __init__(self, settings: Settings, doc_service: DocumentService) -> None:
        super().__init__()
        self.settings = settings
        self.doc_service = doc_service
        self.setWindowTitle(f"Foxit PDF Editor — {settings.build_tag}")
        self.resize(1280, 800)
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("All features unlocked (patched build)")

    def add_tab(self, widget: QWidget, title: str) -> None:
        self.tabs.addTab(widget, title)