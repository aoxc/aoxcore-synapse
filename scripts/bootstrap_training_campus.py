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
            name="Foundation From Scratch",
            stage="L1",
            approach="from-scratch",
            objective="Core reasoning and instruction-following for mini AOXCANs",
            target_domains=("cli", "general-ops"),
            algorithms=("small-transformer", "distillation", "curriculum-learning"),
            readiness_gate=">=80% task accuracy on internal CLI benchmark",
        ),
        TrainingTrack(
            name="XLayer Operations Specialist",
            stage="L2",
            approach="pretrained-adapter",
            objective="Operator assistant for XLayer deployments and troubleshooting",
            target_domains=("xlayer", "cli"),
            algorithms=("lora", "dpo", "retrieval-augmented-finetune"),
            readiness_gate="No critical mistakes across 50 XLayer runbook scenarios",
        ),
        TrainingTrack(
            name="Sui Move Specialist",
            stage="L2",
            approach="pretrained-adapter",
            objective="Support Move dev and validator operations on Sui",
            target_domains=("sui", "move", "cli"),
            algorithms=("qlora", "sft", "toolformer-style supervision"),
            readiness_gate=">=90% pass on Sui CLI + Move Q/A benchmark",
        ),
        TrainingTrack(
            name="Cardano Integration Specialist",
            stage="L2",
            approach="hybrid",
            objective="Assist Cardano tooling and transaction operations",
            target_domains=("cardano", "cli"),
            algorithms=("adapter-fusion", "contrastive-tuning", "self-consistency"),
            readiness_gate="Zero unsafe guidance in wallet/transaction workflows",
        ),
        TrainingTrack(
            name="Cross Chain Mainnet Guard",
            stage="L3",
            approach="hybrid-ensemble",
            objective="Coordinate specialists and detect multi-chain anomalies",
            target_domains=("xlayer", "sui", "cardano", "security"),
            algorithms=("mixture-of-experts", "ensemble-routing", "rule-neural-hybrid"),
            readiness_gate="Stable incident triage quality for 30-day simulation",
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
    print(f"Training campus ready: {manifest_path}")
    print(f"Training campus hazırlandı: {manifest_path}")


if __name__ == "__main__":
    main()
