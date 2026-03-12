from pathlib import Path

from academy.training_space import TrainingTrack, bootstrap_training_campus


def test_bootstrap_training_campus_creates_isolated_tracks(tmp_path: Path) -> None:
    tracks = [
        TrainingTrack("Scratch", "L1", "from-scratch", "Temel eğitim"),
        TrainingTrack("Fine Tune", "L2", "adapter", "Hazır model eğitimi"),
    ]

    manifest_path = bootstrap_training_campus(tmp_path, tracks)

    assert manifest_path.exists()
    campus_root = tmp_path / "training" / "campus"
    assert (campus_root / "l1__scratch" / "datasets").exists()
    assert (campus_root / "l2__fine-tune" / "checkpoints").exists()
