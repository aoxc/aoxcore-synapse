"""Default track definitions for the AOXCORE training campus."""

from __future__ import annotations

from .training_space import TrainingTrack


def get_default_tracks() -> list[TrainingTrack]:
    """Return the default mainnet-oriented AOXCAN training tracks."""

    return [
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
        ),
    ]
