"""Utilities for building isolated training areas for mini-agent education."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import json
from typing import Iterable

ISOLATED_FOLDERS = (
    "datasets",
    "docs_en",
    "curriculum",
    "algorithms",
    "checkpoints",
    "eval",
    "logs",
    "reports",
    "exports",
)


@dataclass(frozen=True)
class TrainingTrack:
    """A single education track for a group of mini-model experiments."""

    name: str
    stage: str
    approach: str
    objective: str
    target_domains: tuple[str, ...]
    algorithms: tuple[str, ...]
    readiness_gate: str

    @property
    def slug(self) -> str:
        return f"{self.stage}__{self.name}".lower().replace(" ", "-")


def _build_track_readme(track: TrainingTrack) -> str:
    return "\n".join(
        [
            f"# Track: {track.name}",
            "",
            f"- Stage: **{track.stage}**",
            f"- Approach: **{track.approach}**",
            f"- Objective: **{track.objective}**",
            f"- Domains: **{', '.join(track.target_domains)}**",
            f"- Algorithms: **{', '.join(track.algorithms)}**",
            f"- Mainnet Readiness Gate: **{track.readiness_gate}**",
            "",
            "This area is strictly isolated from other tracks.",
        ]
    )


def _build_curriculum_doc(track: TrainingTrack) -> str:
    return "\n".join(
        [
            f"# {track.name} Curriculum",
            "",
            "## Mission",
            f"Train small AOXCAN assistants for: {', '.join(track.target_domains)}.",
            "",
            "## Phases",
            "1. Dataset curation from English docs and CLI transcripts.",
            "2. Baseline training with selected algorithm families.",
            "3. Safety and hallucination audits.",
            "4. Domain benchmark and stress testing.",
            "5. Mainnet-readiness report.",
            "",
            "## Success Criteria",
            f"- Must satisfy gate: {track.readiness_gate}",
            "- Must keep outputs reproducible and versioned.",
            "- Must not leak artifacts across other tracks.",
        ]
    )


def _build_algorithm_doc(track: TrainingTrack) -> str:
    lines = ["# Algorithm Plan", "", "This track should compare these strategies:", ""]
    lines.extend([f"- {algo}" for algo in track.algorithms])
    return "\n".join(lines)


def _build_docs_seed(track: TrainingTrack) -> str:
    return "\n".join(
        [
            "# English Documentation Seed",
            "",
            "Use this folder for English source material and synthetic Q/A datasets:",
            "- Protocol specs",
            "- SDK/CLI references",
            "- Runbooks for operators",
            "- Security incident postmortems",
            "",
            f"Track focus: {', '.join(track.target_domains)}",
        ]
    )


def bootstrap_training_campus(base_dir: str | Path, tracks: Iterable[TrainingTrack]) -> Path:
    """Create an isolated multi-level training campus structure.

    Each track gets fully separated folders to avoid experiment collisions.
    """

    root = Path(base_dir)
    campus_dir = root / "training" / "campus"
    campus_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "version": 2,
        "description": "AOXCORE mini-model education campus",
        "mainnet_goal": "Reliable domain-specific mini AOXCAN assistants",
        "tracks": [],
    }

    for track in tracks:
        track_root = campus_dir / track.slug
        for folder in ISOLATED_FOLDERS:
            (track_root / folder).mkdir(parents=True, exist_ok=True)

        (track_root / "README.md").write_text(_build_track_readme(track), encoding="utf-8")
        (track_root / "curriculum" / "CURRICULUM.md").write_text(_build_curriculum_doc(track), encoding="utf-8")
        (track_root / "algorithms" / "ALGORITHMS.md").write_text(_build_algorithm_doc(track), encoding="utf-8")
        (track_root / "docs_en" / "DATASET_SOURCES.md").write_text(_build_docs_seed(track), encoding="utf-8")

        manifest["tracks"].append(asdict(track) | {"slug": track.slug, "isolated_folders": list(ISOLATED_FOLDERS)})

    manifest_path = campus_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest_path
