---
layout: clean
title: EduController/README.md
---

---

# 🎛️ **EduController：制御理論とAI制御の教育フレームワーク**  
**EduController: Educational Framework for Control Theory and AI Control**

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/)  
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 🔗 **公式リンク | Official Links**

| **言語 / Language** | **GitHub Pages 🌐** | **GitHub 💻** |
|---------------------|--------------------|---------------|
| 🇯🇵 **Japanese** | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/EduController) |
| 🇺🇸 **English** | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/en/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/en) |

---

## 📘 **概要 | Overview**

**JP:**  
**EduController** は、**古典制御**から**現代制御**、さらに **AI ベースの次世代型制御**までを体系的に学べる、**段階的かつ実践的な教材プロジェクト**です。Python による制御理論の直感的理解から **HDL 記述**、**LLM 統合設計**まで幅広くサポートします。  

**EN:**  
**EduController** is a **step-by-step**, **practical educational project** covering **classical**, **modern**, and **AI-based next-generation control**. It supports learning from **control theory in Python** to **HDL coding** and **LLM-integrated design**.

---

## 🧭 **構成概要 | Structure Overview**

| **系統 / Track** | **内容（JP）** | **Overview (EN)** |
|------------------|---------------|-------------------|
| 🎛️ **制御理論系 (Part 01〜05)** | 古典制御、状態空間、デジタル制御、実装演習 | Classical control, state-space, digital control, practical implementation |
| 🤖 **AI制御系 (Part 06〜08)** | ニューラルネット、強化学習、データ駆動制御 | Neural networks, reinforcement learning, data-driven control |
| 🧠 **統合・応用制御系 (Part 09〜10)** | LLM統合制御、倒立振子総合制御 | LLM-integrated control, inverted pendulum control |

---

## 📚 **章構成一覧 | Chapter Structure**

### 🎛️ **制御理論系 / Classical & Modern Control**

| **Chapter** | **Title** | **Summary** |
|-------------|-----------|-------------|
| **Part 01** | **古典制御理論 / Classical Control Theory**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part01_classical/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part01_classical) | **PID制御**を中心に、**時間領域・周波数領域**の解析・設計を体系的に学習。<br>*Systematic study of PID control, time-domain and frequency-domain analysis & design.* |
| **Part 02** | **現代制御理論 / Modern Control Theory**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part02_modern/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part02_modern) | **状態空間表現**を基盤とし、**可制御性・可観測性**、**極配置**、**オブザーバ設計**を学ぶ。<br>*Covers state-space representation, controllability, observability, pole placement, observer design.* |
| **Part 03** | **適応制御・ロバスト制御 / Adaptive & Robust Control**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part03_adaptive/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part03_adaptive) | **MRAC**、**H∞制御**、**L1制御**など、パラメータ変動や外乱に強い制御を学ぶ。<br>*MRAC, H∞, L1 control for robustness against parameter variations and disturbances.* |
| **Part 04** | **デジタル制御と信号処理 / Digital Control & Signal Processing**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part04_digital/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part04_digital) | **Z変換**、**離散PID**、**デジタルフィルタ設計**など、デジタル実装向け制御技術を習得。<br>*Z-transform, discrete PID, digital filter design for implementation.* |
| **Part 05** | **実装・応用編 / Implementation & Applications**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part05_practical/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part05_practical) | **Python実装**、**ROS演習**、**FPGA制御**の実システム適用を学ぶ。<br>*Python, ROS practice, FPGA-based control.* [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) |

---

### 🤖 **AI制御系 / AI-based Control**

| **Chapter** | **Title** | **Summary** |
|-------------|-----------|-------------|
| **Part 06** | **ニューラルネットによる制御 / Neural Network Control**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part06_nn_control/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part06_nn_control) | **NN-PID設計**、**逆モデル制御**、ニューラルネットによる高度制御を学ぶ。<br>*NN-PID design, inverse model control using neural networks.* |
| **Part 07** | **強化学習による制御 / Reinforcement Learning Control**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part07_rl_control/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part07_rl_control) | **倒立振子や車両制御にRLを適用**、**DDPG**や**PPO**を実装。<br>*Applying RL to inverted pendulum & vehicle control; implementing DDPG, PPO.* |
| **Part 08** | **データ駆動型制御 / Data-Driven Control**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part08_data_driven/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part08_data_driven) | **Koopman演算子**、**システム同定**を用いたモデルフリー制御を実装。<br>*Model-free control using Koopman operator, system identification.* |

---

### 🧠 **統合・応用制御系 / Integrated Control**

| **Chapter** | **Title** | **Summary** |
|-------------|-----------|-------------|
| **Part 09** | **ハイブリッド制御とLLM統合 / Hybrid Control with LLM Integration**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part09_llm_hybrid) | **FSM×PID×LLM**による三層アーキテクチャで次世代制御設計を実装。<br>*Three-layer architecture (FSM×PID×LLM) for next-gen control.* [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) |
| **Part 10** | **倒立振子の総合制御 / Integrated Control of Inverted Pendulum**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/part10_pendulum/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/part10_pendulum) | **PID**、**LQR**、**RL**、**HDL実装**を統合した倒立振子制御。<br>*PID, LQR, RL, HDL implementation integrated for inverted pendulum control.* [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) |

---

### 🔩 **実装支援ツール / Implementation Toolkit**

| **ディレクトリ** | **概要 / Summary** |
|------------------|--------------------|
| **matlab_tools/**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/matlab_tools/)  [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/matlab_tools) | **Simulinkによる可視化**、**Cコード生成**、**HDL設計**への展開。<br>*Visualization in Simulink, C code generation, HDL design.* [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) |
| **SoC_DesignKit_by_ChatGPT/**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/) [![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/SoC_DesignKit_by_ChatGPT) | **FSM・PID・LLM制御テンプレート**、**Verilog生成**、**テストベンチ検証**。<br>*FSM, PID, LLM control templates, Verilog generation, testbench verification.* [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) |

---

## 🔗 **関連プロジェクト | Related Projects**

- 🎓 **Edusemi-v4x**  
  [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x)  
  **半導体設計・プロセス教育教材**（Python、sky130、OpenLane）  
  *Semiconductor design & process education (Python, sky130, OpenLane)*  
  [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

- 🤖 **AITL-H**  
  [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H)  
  **FSM×PID×LLMの三層制御フレームワーク**（Part09と連携）  
  *Three-layer control framework (FSM×PID×LLM)*  
  [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

- 🧠 **SamizoGPT**  
  [![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/SamizoGPT/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/SamizoGPT)  
  **ChatGPTのプロンプト設計支援テンプレート集**（設計支援と連携）  
  *Prompt design templates for ChatGPT (design assistance)*
  
---

## 👤 **執筆者情報 / Author**

| **📌 項目 / Item** | **内容 / Details** |
|--------------------|--------------------|
| **氏名 / Name** | **三溝 真一（Shinichi Samizo）**<br>*Shinichi Samizo* |
| **学歴 / Education** | **信州大学大学院 電気電子工学 修了**<br>*M.S. in Electrical and Electronic Engineering, Shinshu University* |
| **経歴 / Career** | **元 セイコーエプソン株式会社 技術者（1997年〜）**<br>*Former Engineer at Seiko Epson Corporation (since 1997)* |
| **経験領域 / Expertise** | **半導体デバイス**（ロジック・メモリ・高耐圧混載）<br>*Semiconductor devices (logic, memory, high-voltage mixed integration)*<br>**インクジェット薄膜ピエゾアクチュエータ**<br>*Inkjet thin-film piezo actuators*<br>**PrecisionCoreプリントヘッド製品化・BOM管理・ISO教育**<br>*Productization of PrecisionCore printheads, BOM management, and ISO training* |
| **連絡先 / Contact** | ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)<br>🐦 [https://x.com/shin3t72](https://x.com/shin3t72)<br>💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/) |

---

## 📄 **ライセンス | License**

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  

> **基本ライセンスは MIT** とし、以下の一部ディレクトリ・教材は **ハイブリッドライセンス** を採用します。  
> *The default license is MIT, but specific directories/materials use a Hybrid License.*

| **📌 項目 / Item** | **ライセンス / License** | **説明 / Description** |
|--------------------|--------------------------|------------------------|
| **基本 / Default** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布可能 |
| **ハイブリッド対象 / Hybrid Scope** | [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) <br>Part05, Part09, Part10, matlab_tools, SoC_DesignKit_by_ChatGPT, Edusemi-v4x, AITL-H | 教材・コード・図表の性質に応じて **MIT / CC BY / CC BY-SA / CC BY-NC** を適用 |

---

## 💬 **フィードバック | Feedback**

> 改善提案や議論は **GitHub Discussions** からお願いします。  
> *Propose improvements or start discussions via GitHub Discussions.*

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/EduController/discussions)
