---
layout: clean
title: Part08
permalink: /part08_data_driven/
---

---

# 📊 Part 8: データ駆動型制御 / Data-Driven Control

本章では、**数式モデルを用いずに観測データから制御器や予測モデルを構築**する  
データ駆動型制御（Data-Driven Control）の基本から応用までを学びます。  
これは現代制御やAI制御とも親和性が高く、**産業界でも注目される実践技術**です。

This chapter focuses on **building controllers and predictive models directly from observational data**,  
without relying on explicit mathematical modeling.  
Data-driven control is highly compatible with modern and AI-based control and is increasingly adopted in industry.

---

## 🎯 **学習目標 / Learning Objectives**

- **モデルフリー制御とデータ駆動制御**の違いを理解する  
  Understand the difference between **model-free and data-driven control**  
- **Koopman演算子**による非線形系の線形化を学ぶ  
  Learn how to **linearize nonlinear systems** using **Koopman operators**  
- **動的モード分解（DMD）**を使ってシステム挙動を抽出する  
  Apply **Dynamic Mode Decomposition (DMD)** for system behavior analysis  
- **サブスペース同定法や識別制御**の考え方を習得する  
  Understand **subspace identification** and model-free design principles  
- **Pythonでの実装と可視化**を通じて手法を体験する  
  Implement and visualize these techniques using **Python**

---

## 📁 **ディレクトリ構成 / Directory Structure**

```plaintext
part08_data_driven/
├── theory/                   # 理論資料 / Theory Notes
│   ├── 01_model_free_control.md
│   ├── 02_koopman_operator.md
│   ├── 03_dmd.md
│   ├── 04_subspace_id.md
│   └── 05_data_vs_model.md
├── simulation/               # 実装コード / Simulation Scripts
│   ├── koopman_linearization.py
│   ├── dmd_analysis.py
│   └── subspace_identification.py
├── notebooks/                # Notebook / 可視化と分析用
│   └── koopman_vs_dmd_visual.ipynb
├── figures/                  # 図版 / Figures
└── README.md
```

---

## 📚 **理論資料（Markdown）/ Theory Notes**

| **タイトル / Title** | **ファイル / File** |
|------------------------|----------------------|
| モデルフリー制御の基礎<br>Basics of Model-Free Control | [01_model_free_control.md](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/01_model_free_control.html) |
| Koopman演算子と線形化<br>Koopman Operator & Linearization | [02_koopman_operator.md](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/02_koopman_operator.html) |
| 動的モード分解（DMD）<br>Dynamic Mode Decomposition | [03_dmd.md](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/03_dmd.html) |
| サブスペース同定法<br>Subspace Identification | [04_subspace_id.md](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/04_subspace_id.html) |
| モデルベース制御との比較<br>Comparison with Model-Based Control | [05_data_vs_model.md](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/05_data_vs_model.html) |

---

## 🧪 **実験コード / Simulation Code (Python)**

| **内容 / Description** | **ファイル / File** |
|------------------------|----------------------|
| Koopmanによる線形化<br>Koopman-based linearization | [koopman_linearization.py](https://samizo-aitl.github.io/EduController/part08_data_driven/simulation/koopman_linearization.py) |
| DMDによるモード解析<br>DMD-based mode analysis | [dmd_analysis.py](https://samizo-aitl.github.io/EduController/part08_data_driven/simulation/dmd_analysis.py) |
| サブスペース同定<br>Subspace system identification | [subspace_identification.py](https://samizo-aitl.github.io/EduController/part08_data_driven/simulation/subspace_identification.py) |

---

## 📊 **可視化Notebook / Visualization Notebook**

- [koopman_vs_dmd_visual.ipynb](https://samizo-aitl.github.io/EduController/part08_data_driven/notebooks/koopman_vs_dmd_visual.ipynb)  
  **KoopmanとDMDの比較と可視化**  
  *Visualization comparing Koopman and DMD approaches*

---

## 🔜 **今後の展開 / Future Extensions**

- **Deep Koopman**や**Autoencoder**による次世代識別手法  
  Next-gen identification with **Deep Koopman** or **Autoencoders**  
- **対象特化のデータ拡張・識別器設計**  
  Domain-specific **data augmentation** and **classifier design**  
- **AITL構想への応用**：観測主導の**適応・学習制御層**の構築  
  Application to **AITL**: observation-based **adaptive learning controllers**

---

## 👤 **著者・ライセンス / Author & License**

| **項目 / Item** | **内容 / Details** |
|------------------|---------------------|
| **著者 / Author** | 三溝 真一（**Shinichi Samizo**） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License（**再配布・改変自由**）<br>**Redistribution and modification allowed** |

---

**⬅️ [前章 / Previous Chapter](https://samizo-aitl.github.io/EduController/part07_rl_control/)**  
強化学習による制御（Q学習、DDPG、PPOなど）を扱います。  
Covers reinforcement learning control methods including Q-learning, DDPG, and PPO.

**[次章 / Next Chapter ➡️➡️](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/)**  
LLM統合・ハイブリッド制御（FSM×PID×LLMなど）を扱います。  
Covers LLM-integrated hybrid control such as FSM×PID×LLM.

**🏠 [トップページ / Back to Home](https://samizo-aitl.github.io/EduController/)**
