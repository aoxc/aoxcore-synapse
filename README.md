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
python -m academy.cli recommend
```

Legacy bootstrap script is still available:

```bash
python scripts/bootstrap_training_campus.py
```

The command set generates and validates `training/campus/manifest.json` with track domains, algorithm plans, and readiness gates.
#### Is this the right path?
Short answer: **yes**, if you keep strict promotion gates.

- Keep domain-specialized tracks (XLayer / Sui / Cardano / CLI) isolated.
- Use L1 as a mandatory base before promoting to L2/L3 specialists.
- Treat `validate` as a quality gate in CI so broken tracks cannot progress.
- Prefer iterative open-source contribution per track instead of one huge training run.


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
*Built with integrity for a decentralized future.*

### 🏫 AI Training Campus (Mainnet-Oriented)
Bu repo artık sadece klasör açan bir taslak değil; **mainnet'e yakın, görev uzmanı mini AOXCAN** yetiştirmek için seviyeli ve izole bir eğitim sistemi sunar.

#### Hedeflenen mini AOXCAN profilleri
- **XLayer Ops Assistant**
- **Sui/Move Assistant**
- **Cardano Integration Assistant**
- **CLI Generalist Assistant**
- **Cross-Chain Mainnet Guard** (uzmanları koordine eden üst seviye)

#### Eğitim tasarımı
- Her track tamamen izole (`datasets`, `docs_en`, `curriculum`, `algorithms`, `checkpoints`, `eval`, `logs`, `reports`, `exports`)
- İngilizce doküman kaynakları için ayrı `docs_en/` alanı
- Birden fazla algoritma ailesi ile karşılaştırmalı eğitim (LoRA, QLoRA, DPO, MoE, vb.)
- Track bazlı **mainnet readiness gate** tanımı

#### Başlatma

### 🏫 AI Eğitim Kampüsü (Önerilen Düzen)
Bu depo artık farklı seviyelerde, birbirine karışmadan mini-agent eğitimleri yürütmek için **izole track** yapısını destekler.

- **L1 / from-scratch:** Sıfırdan eğitim denemeleri
- **L2 / pretrained-adapter:** Hazır modeller üzerinde güvenli ince ayar
- **L3 / hybrid specialist:** Göreve özel hibrit uzmanlaşma

Her track için `datasets/`, `checkpoints/`, `logs/`, `reports/`, `exports/` klasörleri ayrı açılır. Böylece sonuçlar birbiriyle çakışmaz.

Başlatmak için:

```bash
python scripts/bootstrap_training_campus.py
```

Bu komut `training/campus/manifest.json` içinde tüm track'leri, domain kapsamını, algoritmaları ve readiness gate bilgilerini üretir.
Bu komut `training/campus/manifest.json` üretir ve eğitim alanlarını otomatik kurar.
