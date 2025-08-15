---
layout: default
title: EduController/README.md
---

# 🎛️ **EduController：制御理論とAI制御の教育フレームワーク**  
**EduController: Educational Framework for Control Theory and AI Control**

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/)  
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 🔗 **公式リンク | Official Links**

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 Japanese | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/EduController) |
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/en/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/en) |

---

## 📘 **概要 | Overview**

**JP:**  
EduController は、古典制御から現代制御、さらに AI ベースの次世代型制御までを体系的に学べる、段階的かつ実践的な教材プロジェクトです。Python による制御理論の直感的理解から HDL 記述、LLM 統合設計まで幅広くサポートします。  

**EN:**  
EduController is a step-by-step, practical educational project covering classical, modern, and AI-based next-generation control. It supports a wide range of learning, from intuitive understanding of control theory using Python to HDL coding and LLM-integrated design.

---

## 🧭 **構成概要 | Structure Overview**

| 系統 / Track | 内容（JP） | Overview (EN) |
|--------------|-----------|---------------|
| 🎛️ 制御理論系 (Part 01〜05) | 古典制御、状態空間、デジタル制御、実装演習 | Classical control, state-space, digital control, practical implementation |
| 🤖 AI制御系 (Part 06〜08) | ニューラルネット、強化学習、データ駆動制御 | Neural networks, reinforcement learning, data-driven control |
| 🧠 統合・応用制御系 (Part 09〜10) | LLM統合制御、倒立振子総合制御 | LLM-integrated control, inverted pendulum control |

---

## 📚 **章構成一覧 | Chapter Structure**

### 🎛️ 制御理論系 / Classical & Modern Control

| 章 / Chapter | ディレクトリ | 内容概要（JP） | Overview (EN) |
|--------------|-------------|----------------|---------------|
| **Part 01** | [part01_classical](./part01_classical/) | PID制御、ボード線図、安定性 | PID control, Bode plot, stability |
| **Part 02** | [part02_modern](./part02_modern/) | 状態空間、LQR、カルマンフィルタ | State-space, LQR, Kalman filter |
| **Part 03** | [part03_adaptive](./part03_adaptive/) | 適応・ロバスト制御（MRAC、H∞、L1） | Adaptive & robust control (MRAC, H∞, L1) |
| **Part 04** | [part04_digital](./part04_digital/) | デジタル制御、Z変換、DSP実装 | Digital control, Z-transform, DSP implementation |
| **Part 05** | [part05_practical](./part05_practical/) [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) | Python実装、ROS演習、FPGA制御 | Python, ROS practice, FPGA-based control |

---

### 🤖 AI制御系 / AI-based Control

| 章 / Chapter | ディレクトリ | 内容概要（JP） | Overview (EN) |
|--------------|-------------|----------------|---------------|
| **Part 06** | [part06_nn_control](./part06_nn_control/) | ニューラルネット制御（NN-PID、逆モデル） | Neural network control (NN-PID, inverse model) |
| **Part 07** | [part07_rl_control](./part07_rl_control/) | 強化学習制御（Q学習、DDPG、PPO） | Reinforcement learning control (Q-learning, DDPG, PPO) |
| **Part 08** | [part08_data_driven](./part08_data_driven/) | データ駆動制御（Koopman、行列識別） | Data-driven control (Koopman, system identification) |

---

### 🧠 統合・応用制御系 / Hybrid & Applied Control

| 章 / Chapter | ディレクトリ | 内容概要（JP） | Overview (EN) |
|--------------|-------------|----------------|---------------|
| **Part 09** | [part09_llm_hybrid](./part09_llm_hybrid/) [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) | LLM統合制御（FSM×PID×LLM） | LLM-integrated hybrid control (FSM×PID×LLM) |
| **Part 10** | [part10_pendulum](./part10_pendulum/) [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) | 倒立振子の総合制御（PID / LQR / DDPG / HDL） | Integrated control of inverted pendulum (PID / LQR / DDPG / HDL) |

---

## 🔩 **実装支援ツール | Implementation Toolkit**

| ディレクトリ | 内容概要（JP） | Overview (EN) |
|--------------|----------------|---------------|
| [**matlab_tools/**](./matlab_tools/) [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) | Simulink による PID・状態空間制御の可視化、Cコード生成、HDL設計への展開 | Visualization of PID/state-space control in Simulink, C code generation, HDL design |
| [**SoC_DesignKit_by_ChatGPT/**](./SoC_DesignKit_by_ChatGPT/) [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license) | FSM・PID・LLM制御のテンプレート、ChatGPTによる Verilog生成、テストベンチ検証 | Templates for FSM, PID, LLM control; Verilog generation via ChatGPT; testbench verification |

---

## 🔗 **関連プロジェクト | Related Projects**

| Project | JP（概要） | EN (Summary) |
|---|---|---|
| 🎓 **Edusemi-v4x** [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x) | 半導体設計・プロセス教育教材（Python、sky130、OpenLane） | Semiconductor design & process education (Python, sky130, OpenLane) |
| 🤖 **AITL-H** [![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H) | FSM×PID×LLMの三層制御フレームワーク（Part09と連携） | Three-layer control framework (FSM×PID×LLM) |
| 🧠 **SamizoGPT**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/SamizoGPT/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/SamizoGPT) | ChatGPTのプロンプト設計支援テンプレート集（設計支援と連携） | Prompt design templates for ChatGPT (design assistance) |

---

## 👤 **著者 / Author**

| 項目 / Item | 内容 / Details |
|-------------|----------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |

---

## 📄 **ライセンス | License**
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  

> 基本ライセンスは MIT とし、以下の一部ディレクトリ・教材は **ハイブリッドライセンス** を採用します。  
> *The default license is MIT, but specific directories/materials use a Hybrid License.*

| 📌 項目 / Item | ライセンス / License | 説明 / Description |
|------|------|------|
| **基本 / Default** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布可能 |
| **ハイブリッド対象 / Hybrid Scope** | Part05, Part09, Part10, matlab_tools, SoC_DesignKit_by_ChatGPT, Edusemi-v4x, AITL-H | 教材・コード・図表の性質に応じて MIT / CC BY / CC BY-SA / CC BY-NC を適用 |

---
