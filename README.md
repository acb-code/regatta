# 🏁 regatta

**Algorithmic Game Theory and Strategic Interaction — from fundamentals to frontier methods.**

`regatta` is a personal learning and research repository for building and understanding computational approaches to game theory.  
It draws inspiration from DeepMind’s work on **PSRO**, **AlphaRank**, and **DeepNash**, as well as OpenSpiel and classical theoretical foundations.

---

### 🧠 Goals
- Recreate **foundational game-theoretic algorithms** from scratch.
- Implement **modern learning and regret-minimization methods**.
- Reproduce **frontier results** from DeepMind, OpenAI, and academia.
- Provide an **experimental sandbox** for exploring equilibria and population dynamics.

---

### 📂 Structure
```
regatta/
├── docs/              # Notes, references, and reproductions
├── regatta/
│   ├── core/          # Foundational algorithms and data structures
│   ├── learning/      # Learning and regret-minimization algorithms
│   ├── experiments/   # Jupyter experiments and reproductions
│   └── utils/         # Shared helpers and common utilities
├── pyproject.toml     # Project packaging and dependency configuration
└── requirements.txt   # Lightweight dependency pinning for quick installs
```

---

### 🚀 Getting Started

```bash
git clone https://github.com/acb-code/regatta.git
cd regatta
pip install -e .
```

For development:
```bash
pip install -e ".[dev]"
```

---

### 🧰 Conda Environment Setup

You can create a dedicated Conda environment for `regatta` to keep dependencies isolated.

```bash
# Create environment
conda create -n regatta python=3.10 -y

# Activate environment
conda activate regatta

# Install dependencies
pip install -e .
```

For development (with testing, linting, etc.):
```bash
pip install -e ".[dev]"
```

Alternatively, you can use the `requirements.txt` file directly:
```bash
pip install -r requirements.txt
```

To verify setup:
```bash
python -m pytest -q
```

Optional (if you prefer Jupyter):
```bash
# Register the environment as a Jupyter kernel
python -m ipykernel install --user --name regatta --display-name "regatta"
```
Then select the **“regatta”** kernel in your Jupyter notebooks under `regatta/experiments/`.

---

### 📚 References
- **Shoham & Leyton-Brown (2008)** – *Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations*
- **Balduzzi et al. (2018)** – *PSRO: Policy-Space Response Oracles*
- **Omidshafiei et al. (2019)** – *AlphaRank: Multi-agent Evaluation via Evolutionary Dynamics*
- **Perolat et al. (2022)** – *Mastering the Game of Stratego with Model-Free Multiagent Reinforcement Learning*

---

### ⚓ License
MIT © Alexander Braafladt
