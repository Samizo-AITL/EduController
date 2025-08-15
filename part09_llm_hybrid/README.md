---
layout: clean
title: Part09
permalink: /part09_llm_hybrid/
---

---

# 🤖 Part 9: ハイブリッド制御とLLM統合 / Hybrid Control with LLM Integration
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

---

本章では、**状態機械（FSM）・物理制御（PID）・大規模言語モデル（LLM）** を組み合わせた  
柔軟かつ適応的な**三層統合型制御アーキテクチャ**を設計・実装します。  
これは AITL構想（FSM × PID × LLM）に基づき、**AI時代の制御系設計**を探求する教材です。

This chapter explores the design and implementation of a **three-layer hybrid control architecture**,  
combining **FSM (Finite State Machine), PID control, and LLMs (Large Language Models)**.  
It is based on the **AITL framework (FSM × PID × LLM)**, aiming to build adaptable and intelligent control systems for the AI era.

---

## 🎯 **学習目標 / Learning Objectives**

- **FSMとPID制御**の連携手法を理解する  
  Understand how to integrate **FSM with PID control**  
- **LLM（ChatGPT等）を制御判断に活用**する手法を学ぶ  
  Learn how to utilize **LLMs** (e.g., ChatGPT) for control decision-making  
- **ルール・対話ベースの制御戦略**を設計できる  
  Design **rule-based and dialogue-based control strategies**  
- **異常対応・目的推論・シナリオ制御**を体験する  
  Experience **exception handling**, **goal reasoning**, and **scenario control**  
- **AITL三層構造によるPoC実装**を行う  
  Implement a **PoC of the three-layer AITL architecture**

---

## 🧩 **章構成（理論教材）/ Chapter Structure (Theory)**

| **ファイル / File** | **内容 / Description** |
|---------------------|-------------------------|
| [01_fsm_pid_llm.md](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/theory/01_fsm_pid_llm.html) | FSM・PID・LLMによる三層制御構造の全体像<br>Three-layer control architecture |
| [02_scenario_control.md](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/theory/02_scenario_control.html) | シナリオ制御と状態モード切替の設計<br>Scenario-driven control design |
| [03_exception_handling.md](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/theory/03_exception_handling.html) | LLMを用いた異常検出と例外対応<br>LLM-based exception handling |
| [04_goal_reasoning.md](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/theory/04_goal_reasoning.html) | 目的推論と対話型制御の導入<br>Goal reasoning and dialog-driven control |

---

## 🧪 **実装コードとNotebook / Simulation Code & Notebooks**

| **ファイル / File** | **役割 / Function** |
|----------------------|----------------------|
| [fsm_pid_llm_sim.py](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/simulation/fsm_pid_llm_sim.py) | 三層制御統合シミュレーション（FSM × PID × LLM） |
| [goal_reasoning_agent.py](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/simulation/goal_reasoning_agent.py) | LLMベースの目的推論エージェントクラス |
| [hybrid_control_demo.ipynb](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/notebooks/hybrid_control_demo.ipynb) | 統合制御のNotebook可視化デモ（予定） |

> 💡 **特長 / Highlights**  
> - 各スクリプトは教育用に設計されており、センサ入力、PID制御、FSM遷移、LLM出力を可視化可能  
> - コードの一部改変からシステム全体設計まで段階的に学べる構成です  
> - 対話応答例や意図推論もLLMログとして出力されます

---

## 📘 **章と実装対応表 / Mapping Between Theory and Code**

| **教材章 / Section** | **内容 / Topic** | **実装ファイル / Script** | **備考 / Notes** |
|------------------|------------------|-----------------------------|------------------|
| 第1章 | FSM・PID・LLM統合 | `fsm_pid_llm_sim.py` | 統合制御PoC、状態遷移＋PID＋LLM |
| 第2章 | シナリオ制御 | `fsm_pid_llm_sim.py` | FSMに基づくモード管理 |
| 第3章 | 例外処理 | LLMログ出力部 | 状況判断・切替ロジック含む |
| 第4章 | 目的推論制御 | `goal_reasoning_agent.py` | 自律的意思決定のシミュレーション |

---

## 🔜 **今後の展開 / Next Steps**

- ChatGPT API とリアル連携による**実機制御**の検証  
- ロボット／GUI／音声対話と連携した**シナリオベース制御**  
- オンライン学習・強化学習との**自己適応統合制御**（👉 Part 10予定）

---

## 📚 **参考資料 / References**

- OpenAI ChatGPT: [https://platform.openai.com/](https://platform.openai.com/)  
- 本教材: [EduController (GitHub)](https://github.com/Samizo-AITL/EduController)  
- FSM/PID/LLMの統合構想：AITL構想（AITL-H）

---

## 👤 **著者 / Author**

| **項目 / Item** | **内容 / Details** |
|------------------|---------------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |

---

## 📄 **ライセンス / License**
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)  

> 教材・コード・図表の性質に応じたハイブリッドライセンスを採用。  
> *Hybrid licensing based on the nature of the materials, code, and diagrams.*

| 📌 項目 / Item | ライセンス / License | 説明 / Description |
|------|------|------|
| **コード（Code）** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布が可能<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須<br>*Attribution required* |
| **図表・イラスト（Figures & diagrams）** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ許可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

**⬅️ [前章 / Previous Chapter](https://samizo-aitl.github.io/EduController/part08_data_driven/)**  
データ駆動型制御（Koopman演算子、行列識別など）を扱います。  
Covers data-driven control methods including the Koopman operator and system identification.

**[次章 / Next Chapter ➡️➡️](https://samizo-aitl.github.io/EduController/part10_pendulum/)**  
倒立振子の総合制御（PID / LQR / DDPG / HDLなど）を扱います。  
Covers integrated control of inverted pendulum systems including PID, LQR, DDPG, and HDL implementation.

**🏠 [トップページ / Back to Home](https://samizo-aitl.github.io/EduController/)**
