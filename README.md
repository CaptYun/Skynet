# Skynet

Skynet is a research project and simulation framework for exploring decentralized task allocation in congested urban airspace scenarios.  
The project is inspired by NASA's DFR concept and models coordination between autonomous aerial agents using algorithms such as GRAPE and CBBA.

---

## ✈️ Project Structure

```
Skynet/
├── docs/          # Obsidian-compatible markdown documents
├── code/          # Python and Jupyter-based simulators
├── figures/       # Output visualizations
├── papers/        # Reference materials and BibTeX
├── README.md
└── .gitignore
```

---

## 📄 Key Components

- `Scenario1_01_Problem.md`: Problem definition for Scenario 1 (airspace sharing)
- `Scenario1_03_MRTA.md`: Mathematical model for Multi-Robot Task Allocation
- `scenario1_simulation.py`: Python simulation loop with basic GRAPE logic
- `scenario1_simulation.ipynb`: Interactive version with Matplotlib visualization

---

## 🚀 How to Run

You can run the simulation locally:

```bash
# Clone the repository
git clone https://github.com/CaptYun/Skynet.git
cd Skynet/code

# Run Python simulation
python scenario1_simulation.py
```

Or view/edit the Jupyter version in:
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CaptYun/Skynet/blob/main/code/scenario1_simulation.ipynb)
- VS Code + Jupyter extension
- Jupyter Notebook

---

## 🔗 View Markdown Notes on GitHub

Markdown documents for Scenario 1:
- [MRTA 모델 구조](https://github.com/CaptYun/Skynet/blob/main/docs/Scenario1_03_MRTA.md)
- [우선권 기반 Task 정의](https://github.com/CaptYun/Skynet/blob/main/docs/Scenario1_02_Tasks.md)
- [알고리즘 비교 전략](https://github.com/CaptYun/Skynet/blob/main/docs/Scenario1_04_Algorithms.md)

---

## 📜 License

MIT License (TBD)
