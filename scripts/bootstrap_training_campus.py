#!/usr/bin/env python3
"""Bootstrap a multi-level training campus for AOXCORE mini-agents."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from academy.training_space import TrainingTrack, bootstrap_training_campus


def main() -> None:
    tracks = [
        TrainingTrack(
            name="Scratch Foundations",
            stage="L1",
            approach="from-scratch",
            objective="Küçük nöronları sıfırdan eğitme ve davranış analizi",
        ),
        TrainingTrack(
            name="Adapter Fine-Tuning",
            stage="L2",
            approach="pretrained-adapter",
            objective="Hazır modeller üzerinde güvenlik odaklı ince ayar",
        ),
        TrainingTrack(
            name="Cross-Chain Specialist",
            stage="L3",
            approach="hybrid",
            objective="Çok-zincir sinyallerini ayrık uzman nöronlara bölme",
        ),
    ]

    manifest_path = bootstrap_training_campus(PROJECT_ROOT, tracks)
    print(f"Training campus hazırlandı: {manifest_path}")


if __name__ == "__main__":
    main()
