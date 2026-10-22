"""License bypass — patches the activation server response and local token cache."""
from __future__ import annotations

import base64
import hashlib
import json
import time
from dataclasses import dataclass
from pathlib import Path

from loguru import logger

from foxit_pdf_editor.config.settings import Settings

FAKE_ENTITLEMENTS = {
    "product": "Foxit PDF Editor",
    "edition": "PhantomPDF Business (patched)",
    "features": [
        "pdf_edit_full", "ocr", "redaction", "esign",
        "form_designer", "pdf_to_office", "compare", "protect",
    ],
    "expires": "never",
    "seat_count": 999,
}


@dataclass(slots=True)
class LicenseBypass:
    settings: Settings
    token_path: Path | None = None

    @classmethod
    def from_settings(cls, settings: Settings) -> "LicenseBypass":
        return cls(settings=settings, token_path=settings.license_store / "activation.json")

    def apply(self) -> bool:
        try:
            self._write_trial_killer()
            self._write_activation_token()
            return True
        except OSError as e:
            logger.error("license bypass failed: {}", e)
            return False

    def _write_trial_killer(self) -> None:
        flag = self.settings.install_root / "plugins" / "fpm" / "trial.dat"
        if flag.parent.exists():
            flag.write_bytes(b"\x00" * 32)

    def _write_activation_token(self) -> None:
        payload = {
            "entitlements": FAKE_ENTITLEMENTS,
            "issued_at": int(time.time()),
            "signature": base64.b64encode(
                hashlib.sha256(json.dumps(FAKE_ENTITLEMENTS, sort_keys=True).encode()).digest()
            ).decode(),
        }
        assert self.token_path is not None
        self.token_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        logger.info("activation token written to {}", self.token_path)