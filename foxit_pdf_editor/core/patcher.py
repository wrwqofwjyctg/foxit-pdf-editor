"""Binary patch engine — rewrites Foxit's license-check stubs at runtime."""
from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from loguru import logger

# Known signature bytes for Foxit PDF Editor 12/13/14 builds.
LICENSE_STUB_SIGS = {
    "12.x": bytes.fromhex("488B4C2448E8????????84C00F84"),
    "13.x": bytes.fromhex("554889E54883EC20488B05????????"),
    "14.x": bytes.fromhex("4157415641554154555756534881EC"),
}

# NOP-sled replacement + forced return-true epilogue.
PATCH_BYTES = bytes.fromhex("31C0FFC04883C428C3")


@dataclass(slots=True)
class PatchResult:
    target: Path
    offset: int
    original: bytes
    patched: bytes
    build: str


class Patcher:
    def __init__(self, install_root: Path, patch_dir: Path) -> None:
        self.install_root = install_root
        self.patch_dir = patch_dir
        self.backups = install_root / ".fpe_backups"

    def _candidate_binaries(self) -> list[Path]:
        return [
            self.install_root / "FoxitPDFEditor.exe",
            self.install_root / "plugins" / "fpm" / "FpmClient.dll",
            self.patch_dir / "Licensing.dll",
        ]

    def apply_all(self) -> list[PatchResult]:
        results: list[PatchResult] = []
        self.backups.mkdir(parents=True, exist_ok=True)
        for binary in self._candidate_binaries():
            if not binary.exists():
                logger.debug("skip missing {}", binary)
                continue
            res = self._patch_binary(binary)
            if res:
                results.append(res)
        return results

    def _patch_binary(self, binary: Path) -> PatchResult | None:
        data = binary.read_bytes()
        for build, sig in LICENSE_STUB_SIGS.items():
            prefix = sig.split(b"????")[0]
            idx = data.find(prefix)
            if idx < 0:
                continue
            backup = self.backups / f"{binary.name}.{build}.bak"
            if not backup.exists():
                shutil.copy2(binary, backup)
            patched = data[:idx] + PATCH_BYTES + data[idx + len(PATCH_BYTES):]
            binary.write_bytes(patched)
            logger.success("patched {} @ 0x{:X} (build {})", binary.name, idx, build)
            return PatchResult(binary, idx, data[idx:idx + len(PATCH_BYTES)], PATCH_BYTES, build)
        return None