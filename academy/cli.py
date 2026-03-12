"""CLI for managing the AOXCORE training campus."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .default_tracks import get_default_tracks
from .training_space import bootstrap_training_campus


def _campus_manifest_path(base_dir: Path) -> Path:
    return base_dir / "training" / "campus" / "manifest.json"


def cmd_bootstrap(base_dir: Path) -> int:
    manifest_path = bootstrap_training_campus(base_dir, get_default_tracks())
    print(f"Training campus ready: {manifest_path}")
    return 0


def cmd_list_tracks(base_dir: Path) -> int:
    manifest_path = _campus_manifest_path(base_dir)
    if not manifest_path.exists():
        print("Manifest not found. Run `bootstrap` first.")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    print("AOXCORE Training Tracks")
    for track in manifest.get("tracks", []):
        print(f"- {track['stage']} | {track['name']} | domains={','.join(track['target_domains'])}")
    return 0


def cmd_validate(base_dir: Path) -> int:
    manifest_path = _campus_manifest_path(base_dir)
    if not manifest_path.exists():
        print("Manifest not found. Run `bootstrap` first.")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    missing = []
    for track in manifest.get("tracks", []):
        track_root = manifest_path.parent / track["slug"]
        for folder in track.get("isolated_folders", []):
            if not (track_root / folder).exists():
                missing.append(str(track_root / folder))

    if missing:
        print("Campus validation failed. Missing paths:")
        for path in missing:
            print(f"- {path}")
        return 2

    print("Campus validation passed.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AOXCORE Training Campus CLI")
    parser.add_argument("--base-dir", default=".", help="Project root for training/campus")

    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("bootstrap", help="Create or refresh the default training campus")
    subparsers.add_parser("list-tracks", help="List tracks from manifest.json")
    subparsers.add_parser("validate", help="Validate that track isolation folders exist")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    base_dir = Path(args.base_dir).resolve()

    if args.command == "bootstrap":
        return cmd_bootstrap(base_dir)
    if args.command == "list-tracks":
        return cmd_list_tracks(base_dir)
    if args.command == "validate":
        return cmd_validate(base_dir)

    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
