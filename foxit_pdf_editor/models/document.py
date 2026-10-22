"""Document metadata model."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class DocumentMeta:
    path: Path
    page_count: int
    title: str = ""
    author: str = ""
    created: datetime | None = None
    encrypted: bool = False
    tags: list[str] = field(default_factory=list)

    @property
    def display_name(self) -> str:
        return self.title or self.path.stem