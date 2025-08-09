---
layout: default
title: Part 2 現代制御理論 / Modern Control Theory
permalink: /part02_modern/README.html
---

---

# 🧠 Part 2: 現代制御理論 / Modern Control Theory

---

本章では、**状態空間表現**を基盤としたモダン制御理論を学びます。  
**可制御性・可観測性**を前提とし、**極配置**による状態フィードバック、**オブザーバ（状態推定器）**設計までを扱います。

This chapter introduces **modern control theory** based on **state-space representation**.  
It covers **controllability**, **observability**, **state feedback** via **pole placement**, and the design of **observers** (state estimators).

---

## 🧭 **章構成と教材一覧 / Chapter Breakdown**

| No | **章タイトル / Title** | **内容概要 / Description** |
|----|-------------------------|-----------------------------|
| 01 | [状態空間表現の基礎](https://samizo-aitl.github.io/EduController/part02_modern/theory/01_state_space.html) / Basics of State-Space | $Ax\!+\!Bu$, $Cx\!+\!Du$ の構造と意味、行列モデル化<br>Structure and meaning of $Ax\!+\!Bu$, $Cx\!+\!Du$ |
| 02 | [可制御性と可観測性](https://samizo-aitl.github.io/EduController/part02_modern/theory/02_controllability.html) / Controllability & Observability | Kalmanのランク条件、状態操作・推定の可否判定<br>Kalman rank condition for state control/observation |
| 03 | [状態フィードバックと極配置](https://samizo-aitl.github.io/EduController/part02_modern/theory/03_state_feedback.html) / State Feedback & Pole Placement | 極配置による閉ループ極の設計、可制御性の役割<br>Closed-loop pole design using pole placement |
| 04 | [オブザーバ設計と状態推定](https://samizo-aitl.github.io/EduController/part02_modern/theory/04_observer_design.html) / Observer Design & Estimation | $L$ゲイン設計と $A\!-\!LC$ の安定化、推定誤差の収束<br>Gain design for observer and estimation convergence |

---

## 💻 **実行スクリプト一覧 / Simulation Scripts**

| **スクリプト名 / Script** | **内容 / Description** |
|----------------------------|-------------------------|
| [state_feedback.py](https://samizo-aitl.github.io/EduController/part02_modern/simulation/state_feedback.py) | フィードバックゲイン $K$ の設計と応答可視化（予定）<br>Design of gain $K$ and response visualization |
| [observer_design.py](https://samizo-aitl.github.io/EduController/part02_modern/simulation/observer_design.py) | オブザーバゲイン $L$ 設計と拡張系の応答確認<br>Observer gain $L$ design and extended system simulation |

---

## 🧪 **Jupyterノートブック（予定）/ Notebooks (Planned)**

| **ノートブック名** | **内容 / Description** |
|--------------------|-------------------------|
| state_feedback_demo.ipynb | 状態フィードバックの対話可視化（未作成）<br>Interactive demo of state feedback (TBD) |
| observer_design_demo.ipynb | オブザーバの推定精度と制御応答（未作成）<br>Observer estimation accuracy and response (TBD) |

---

## 🖼️ **教材図・シミュレーション出力 / Figures**

| **図ファイル** | **内容 / Description** |
|----------------|-------------------------|
| observer_response.png | オブザーバ付き制御系のステップ応答グラフ<br>Step response of system with observer |
| その他 / Others | 状態空間モデル図、極配置概念図（今後追加予定）<br>State-space diagrams, pole placement illustrations (TBD) |

---

## ⚙️ **実行環境と依存ライブラリ / Environment & Dependencies**

```bash
pip install control matplotlib numpy
```

- **対応Pythonバージョン**：3.8〜3.12  
  Compatible with Python 3.8–3.12  
- **使用モジュール**：`control.place`, `control.ctrb`, `control.obsv` など  
  Includes `control.place`, `control.ctrb`, `control.obsv`  
- **推奨環境**：VSCode + Python または Jupyter Lab  
  Recommended: VSCode + Python, or Jupyter Lab

---

## 🧠 **学習の流れとポイント / Learning Flow & Key Concepts**

1. **状態空間表現**：行列で動的システムをモデル化  
   *Model systems using state-space matrices*  
2. **可制御性 / 可観測性**：制御・推定の可能性を数学的に判別  
   *Evaluate controllability and observability using rank tests*  
3. **状態フィードバック**：希望する閉ループ極配置のためのゲイン設計  
   *Design gain $K$ to place closed-loop poles*  
4. **オブザーバ設計**：観測できない状態を推定して制御に活用  
   *Estimate unmeasured states using observer gain $L$*

---

## 📚 **参考資料 / References**

- 「現代制御理論入門」森北出版  
  *Introduction to Modern Control Theory* – Morikita Publishing  
- *Modern Control Engineering* – K. Ogata  
- Pythonライブラリ：`control`, `numpy`, `matplotlib`

---

## 👤 **著者・ライセンス / Author & License**

| **項目 / Item** | **内容 / Details** |
|-----------------|--------------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

**⬅️ [前章 / Previous Chapter](https://samizo-aitl.github.io/EduController/part01_classical/README.html)**  
PID制御の基本、ボード線図による周波数応答解析、システムの安定性評価を解説します。  
Covers the basics of PID control, frequency response analysis using Bode plots, and system stability evaluation.

**[次章 / Next Chapter ➡️➡️](https://samizo-aitl.github.io/EduController/part03_adaptive/README.html)**  
適応制御（MRAC）、ロバスト制御（H∞、L1）など、パラメータ変動や外乱に強い制御法を扱います。  
Covers adaptive control (MRAC) and robust control methods (H∞, L1) designed to handle parameter variations and disturbances.

**🏠 [トップページ / Back to Home](https://samizo-aitl.github.io/EduController/README.html)**
