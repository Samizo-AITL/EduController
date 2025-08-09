---
layout: default
title: Part 03  適応制御・ロバスト制御 / Adaptive & Robust Control
permalink: /part03_adaptive/
---

---

# 🔄 Part 03: 適応制御・ロバスト制御 / Adaptive & Robust Control

---

本章では、制御対象のパラメータ変動・モデリング誤差に対応する  
**適応制御**と**ロバスト制御**について、**理論と実装の両面**から学びます。  
また、FSM×PID×LLMで構成される **AITL-H** における「**理性層**」の柔軟化技術としても位置づけられます。

In this chapter, we learn both the **theory and implementation** of **adaptive** and **robust** control techniques,  
which are essential for dealing with **system parameter variations and modeling uncertainties**.  
These are also positioned as flexible technologies for the "**rational layer**" in the **AITL-H** architecture (FSM × PID × LLM).

---

## 🎯 **学習目標 / Learning Objectives**

- モデル変動・外乱に強い制御器の設計方法を理解する  
  **Understand how to design controllers** that are robust to plant variations and disturbances  
- MRACやゲインスケジューリングなどの適応戦略を体験する  
  **Learn adaptive strategies** like MRAC and gain scheduling  
- H∞制御の基本概念と感度関数・補償関数を理解する  
  **Grasp the fundamentals of H-infinity control**, sensitivity and complementary functions  
- FSM/LLMと連携した適応的な制御判断の構造を設計できる  
  **Design adaptive decision-making structures** using FSM and LLM

---

## 🧩 **構成一覧 / Chapter Structure**

### 📘 [`theory/`](./theory/)

| **ファイル名 / File** | **内容 / Description** |
|------------------------|-------------------------|
| [`01_adaptive_intro.md`](./theory/01_adaptive_intro.md) | 適応制御の概要と必要性<br>Overview and necessity of adaptive control |
| [`02_mrac_design.md`](./theory/02_mrac_design.md) | MRAC（モデル参照型適応制御）の理論<br>Theory of Model Reference Adaptive Control |
| [`03_gain_scheduling.md`](./theory/03_gain_scheduling.md) | ゲインスケジューリング制御の仕組み<br>Gain scheduling mechanism |
| [`04_robust_control.md`](./theory/04_robust_control.md) | ロバスト制御とH∞制御の基礎<br>Robust control and H-infinity fundamentals |

---

### 🧪 [`simulation/`](./simulation/)

| **スクリプト名 / Script** | **内容 / Description** |
|----------------------------|-------------------------|
| [`mrac_simulation.py`](./simulation/mrac_simulation.py) | MITルールによるMRACのステップ追従<br>MRAC step tracking using MIT rule |
| [`gain_schedule_demo.py`](./simulation/gain_schedule_demo.py) | スケジューリングによる比例制御の補間<br>Gain scheduling for interpolated P control |
| [`hinf_synthesis_demo.py`](./simulation/hinf_synthesis_demo.py) | 感度・補償関数のボード解析によるH∞デモ<br>H-infinity demo using Bode plots of sensitivity functions |

---

### 🖼️ [`figures/`](./figures/)

| **図ファイル / Figure** | **内容 / Description** |
|---------------------------|-------------------------|
| [`mrac_response.png`](./figures/mrac_response.png) | MRAC応答曲線<br>MRAC response curve |
| [`gain_schedule_response.png`](./figures/gain_schedule_response.png) | GS制御の動的応答<br>Dynamic response with gain scheduling |
| [`hinf_sensitivity_response.png`](./figures/hinf_sensitivity_response.png) | H∞制御における $S$/$T$ の周波数応答<br>Sensitivity and complementary response in H∞ control |

---

## 🔗 **AITL-Hとの連携 / AITL-H Integration**

| **AITL層 / Layer** | **制御役割 / Role** | **本章との関係 / Relevance** |
|--------------------|---------------------|-------------------------------|
| **本能（FSM） / Instinct** | 状態遷移制御<br>Mode switching | モードごとのゲインスケジューリング<br>Gain scheduling per mode |
| **理性（PID） / Rational** | 汎用的物理制御<br>Generic control | MRACでチューニング、H∞で保証強化<br>MRAC for tuning, H∞ for robustness |
| **知性（LLM） / Intelligence** | 状況予測・判断<br>Context-aware decisions | 制御戦略選択・制御パラメータ提案支援<br>Strategy selection, parameter recommendation |

---

## 🚧 **今後の展開予定 / Future Extensions**

- [`05_l1_adaptive.md`](./theory/05_l1_adaptive.md)：**L1適応制御の設計原理（予定）**  
  *L1 adaptive control theory (planned)*  
- [`robust_block_diagram.png`](./figures/robust_block_diagram.png)：**H∞制御構成図のAI生成（予定）**  
  *H-infinity architecture diagram (to be generated)*  
- [`notebooks/`](./notebooks/)：**MRAC・GSのインタラクティブ実験ノート追加予定**  
  *Interactive notebooks for MRAC & GS (planned)*  
- [`AITL連携図`](../figures/aitl_structure.png)：**Part03を含むAITL全体構造図を統合更新予定**  
  *Update overall AITL-H diagram to include Part03*

---

## 📎 **関連リンク / Related Links**

- 🔁 [**Part 02: PID制御の基礎**](../part02_pid_control/README.md)  
- 🧠 [**AITL-H 概要**](../../aitl_h/README.md)  
- 📦 [**制御教材トップページ / Control Materials Top**](../../README.md)

---

## 👤 **著者・ライセンス / Author & License**

| **項目 / Item** | **内容 / Details** |
|-----------------|--------------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo）|
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

**⬅️ [前章 / Previous Chapter](../part02_modern/)**  
状態空間モデル、最適レギュレータ（LQR）、カルマンフィルタによる推定手法を扱います。  
Covers state-space modeling, optimal regulator (LQR), and estimation techniques using the Kalman filter.

**[次章 / Next Chapter ➡️➡️](../part04_digital/)**  
デジタル制御の基礎、Z変換、DSP実装など、離散時間系の制御と実装方法を学びます。  
Covers the basics of digital control, Z-transform, and DSP implementation for discrete-time systems.

**🏠 [トップページ / Back to Home](../README.md)**

---
