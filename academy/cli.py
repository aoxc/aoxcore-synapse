"""CLI for managing the AOXCORE training campus."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .default_tracks import get_default_tracks
from .training_space import REQUIRED_SEED_FILES, bootstrap_training_campus


REQUIRED_TRACK_KEYS = (
    "name",
    "stage",
    "approach",
    "objective",
    "target_domains",
    "algorithms",
    "readiness_gate",
    "slug",
    "isolated_folders",
)
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


def _validate_manifest_shape(manifest: dict) -> list[str]:
    errors: list[str] = []
    if "tracks" not in manifest or not isinstance(manifest["tracks"], list):
        errors.append("manifest.tracks must exist and be a list")
        return errors

    for idx, track in enumerate(manifest["tracks"]):
        for key in REQUIRED_TRACK_KEYS:
            if key not in track:
                errors.append(f"tracks[{idx}] missing key: {key}")

    declared_seed = manifest.get("required_seed_files", [])
    if declared_seed != list(REQUIRED_SEED_FILES):
        errors.append("manifest.required_seed_files does not match expected seed files")

    return errors


def cmd_validate(base_dir: Path) -> int:
    manifest_path = _campus_manifest_path(base_dir)
    if not manifest_path.exists():
        print("Manifest not found. Run `bootstrap` first.")
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    errors = _validate_manifest_shape(manifest)
    missing_paths: list[str] = []

    missing = []
    for track in manifest.get("tracks", []):
        track_root = manifest_path.parent / track["slug"]
        for folder in track.get("isolated_folders", []):
            if not (track_root / folder).exists():
                missing_paths.append(str(track_root / folder))

        for seed_file in manifest.get("required_seed_files", []):
            seed_path = track_root / seed_file
            if not seed_path.exists():
                missing_paths.append(str(seed_path))

    if errors or missing_paths:
        print("Campus validation failed.")
        if errors:
            print("Schema errors:")
            for err in errors:
                print(f"- {err}")
        if missing_paths:
            print("Missing paths:")
            for path in missing_paths:
                print(f"- {path}")
                missing.append(str(track_root / folder))

    if missing:
        print("Campus validation failed. Missing paths:")
        for path in missing:
            print(f"- {path}")
        return 2

    print("Campus validation passed.")
    return 0


def cmd_recommend() -> int:
    print("Recommended path: YES, with guardrails.")
    print("1) Keep specialized tracks per chain/domain (current architecture).")
    print("2) Start with L1 CLI generalist before heavy multi-chain tuning.")
    print("3) Promote to L2/L3 only after passing readiness gates.")
    print("4) Block promotion when safety/hallucination checks fail.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AOXCORE Training Campus CLI")
    parser.add_argument("--base-dir", default=".", help="Project root for training/campus")

    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("bootstrap", help="Create or refresh the default training campus")
    subparsers.add_parser("list-tracks", help="List tracks from manifest.json")
    subparsers.add_parser("validate", help="Validate manifest schema + track isolation + seed files")
    subparsers.add_parser("recommend", help="Print concise guidance for next execution steps")
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
    if args.command == "recommend":
        return cmd_recommend()

    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
