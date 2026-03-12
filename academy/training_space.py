"""Utilities for building isolated training areas for mini-agent education."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json
from typing import Iterable


@dataclass(frozen=True)
class TrainingTrack:
    """A single education track for a group of mini-model experiments."""

    name: str
    stage: str
    approach: str
    objective: str

    @property
    def slug(self) -> str:
        return f"{self.stage}__{self.name}".lower().replace(" ", "-")


def bootstrap_training_campus(base_dir: str | Path, tracks: Iterable[TrainingTrack]) -> Path:
    """Create an isolated multi-level training campus structure.

    Each track gets fully separated folders to avoid experiment collisions.
    """

    root = Path(base_dir)
    campus_dir = root / "training" / "campus"
    campus_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "version": 1,
        "description": "AOXCORE mini-model education campus",
        "tracks": [],
    }

    for track in tracks:
        track_root = campus_dir / track.slug
        for folder in ("datasets", "checkpoints", "logs", "reports", "exports"):
            (track_root / folder).mkdir(parents=True, exist_ok=True)

        readme = track_root / "README.md"
        readme.write_text(
            "\n".join(
                [
                    f"# Track: {track.name}",
                    "",
                    f"- Stage: **{track.stage}**",
                    f"- Approach: **{track.approach}**",
                    f"- Objective: **{track.objective}**",
                    "",
                    "Bu alan diğer track'lerden izole tasarlanmıştır.",
                ]
            ),
            encoding="utf-8",
        )

        manifest["tracks"].append(asdict(track) | {"slug": track.slug})

    manifest_path = campus_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest_path
