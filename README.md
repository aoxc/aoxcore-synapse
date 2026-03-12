# AOXCORE - Synapse Module

> **Status:** Experimental Research & Neural Prototyping (Alpha) 🧪  
> *Exploring systemic security through minimalist intelligent agents.*

---

### 🧬 Philosophy: Minimalist Intelligence
The **Synapse** module is an experimental laboratory within the AOXCON ecosystem. Our primary objective is not to build monolithic AI, but to deploy **minimalist, high-integrity agents** designed to enhance blockchain security and coordination.

We believe that small, specialized "neurons" (agents) are more resilient, verifiable, and secure than complex, opaque systems.

### 🏗️ Strategic Objectives
* **🛡️ Micro-Agent Security:** Use lightweight agents to monitor cross-chain state transitions and detect anomalies in real time.
* **🧠 Decentralized Logic:** Research small-scale neural patterns that can support decision-making across XLayer, Sui, and Cardano.
* **🔐 Verifiable Integrity:** Prioritize transparency and simplicity so each agent action remains predictable and auditable.

---

### 🛠️ Current Focus
- [x] Conceptual framework for micro-agents
- [/] Prototyping "Neuron-0" security monitoring flow
- [ ] Multi-chain state synchronization tests

---

### 🏫 AI Training Campus (Mainnet-Oriented)
The repository includes a **fully isolated training campus** for building domain-specific mini AOXCAN assistants.

#### Target assistant families
- **CLI Generalist Assistant** (foundation)
- **XLayer Operations Specialist**
- **Sui/Move Specialist**
- **Cardano Integration Specialist**
- **Cross-Chain Mainnet Guard** (specialist coordination)

#### Isolation model
Each track gets independent artifacts so experiments never collide:

- `datasets/`
- `docs_en/`
- `curriculum/`
- `algorithms/`
- `checkpoints/`
- `eval/`
- `logs/`
- `reports/`
- `exports/`

#### CLI commands
```bash
python -m academy.cli --base-dir . bootstrap
python -m academy.cli --base-dir . list-tracks
python -m academy.cli --base-dir . validate
```

Legacy bootstrap script is still available:

```bash
python scripts/bootstrap_training_campus.py
```

The command set generates and validates `training/campus/manifest.json` with track domains, algorithm plans, and readiness gates.

---

### 🌱 Open Source Note
This project is intentionally open and iterative. If a training approach fails, the structure is designed so others can continue the work cleanly, track by track, with reproducible outputs.
