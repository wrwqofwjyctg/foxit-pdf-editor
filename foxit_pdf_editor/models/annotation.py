from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Annotation:
    page: int
    kind: str  # highlight | note | stamp | redact
    rect: tuple[float, float, float, float]
    content: str = ""
    color: str = "#FFD400"

    def to_dict(self) -> dict:
        return {
            "page": self.page, "kind": self.kind, "rect": list(self.rect),
            "content": self.content, "color": self.color,
        }