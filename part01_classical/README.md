---
layout: default
title: Part 1 古典制御理論 / Classical Control Theory 
permalink: /part01_classical/
---

---

# ⚙️ Part 1: 古典制御理論 / Classical Control Theory

---

本章では、**PID制御**を中心とした古典制御理論を扱い、**時間領域および周波数領域**での応答解析・設計法を体系的に学びます。  
制御の基本構造から、**安定性・ロバスト性**までを段階的に理解し、**Pythonによる可視化・シミュレーション**を通じて実装感覚も身につけます。

This chapter covers classical control theory centered on **PID control**, systematically addressing **response analysis and design** in both time and frequency domains.  
It builds a step-by-step understanding from **control structure to robustness**, with implementation experience through **Python-based simulations**.

---

## 🧭 **構成（章別教材） / Chapter Breakdown** [`theory/`](theory/)

| No | **章タイトル / Chapter** | **内容概要 / Description** |
|----|---------------------------|-----------------------------|
| 01 | [`PID制御の基礎`](theory/01_pid_control.md) / PID Basics | PID各成分の働き、ブロック線図、伝達関数の理解<br>Function of each term, block diagrams, transfer functions |
| 02 | [`過渡応答と定常偏差`](theory/02_transient_response.md) / Transient Response & Steady-State Error | ステップ応答、時間定数、定常偏差の評価法<br>Step response, time constant, steady-state error |
| 03 | [`安定性判別法`](theory/03_stability_methods.md) / Stability Criteria | Routh表、根軌跡、ナイキスト法による安定判定<br>Routh table, root locus, Nyquist criterion |
| 04 | [`周波数応答とボード線図`](theory/04_freq_analysis.md) / Frequency Response & Bode Plot | ゲイン・位相プロット、交差周波数、周波数特性<br>Gain/phase plots, crossover frequency |
| 05 | [`安定余裕とロバスト性`](theory/05_gain_margin.md) / Stability Margin & Robustness | ゲイン余裕・位相余裕によるロバスト性評価<br>PM/GM based robustness assessment |

---

## 🧪 **実行スクリプト / Simulation Scripts** [`simulation/`](simulation/)

| **ファイル / Script** | **内容 / Description** |
|------------------------|-------------------------|
| [`pid_simulation.py`](simulation/pid_simulation.py) | PID制御とステップ応答の比較<br>Step response comparison for various PID settings |
| [`transient_response.py`](simulation/transient_response.py) | 1次・2次遅れ系の応答描画<br>Plotting first/second-order system responses |
| [`stability_methods.py`](simulation/stability_methods.py) | Routh表, 根軌跡, ナイキスト線図の描画<br>Routh table, root locus, Nyquist plot |
| [`bode_plot.py`](simulation/bode_plot.py) | ボード線図の自動描画<br>Automated Bode plot generation |
| [`gain_margin.py`](simulation/gain_margin.py) | PM/GMの自動計算と可視化<br>Automated calculation and visualization of PM/GM |

---

## 📓 **Jupyterノートブック / Notebooks** [`notebooks/`](notebooks/)

| **ノートブック** | **内容 / Description** |
|------------------|-------------------------|
| [`pm_gm_analysis.ipynb`](notebooks/pm_gm_analysis.ipynb) | PM/GMの計算とボード線図描画（対話形式）<br>Interactive Bode plot and stability margin analysis |
| [`pid_design.ipynb`](notebooks/pid_design.ipynb) | PIDゲインと応答の関係（予定）<br>Planned: Relationship between PID gains and response |

---

## 🖼️ **教材図・グラフ / Figures** [`figures/`](figures/)

| **図ファイル** | **内容 / Description** |
|----------------|-------------------------|
| `pid_block_diagram.png` | PID制御のブロック線図<br>Block diagram of PID control |
| `step_response.png` | 各PID構成による応答比較<br>Step response comparison |
| `bode_example.png` | 周波数応答のボード線図<br>Example of Bode plot |
| `nyquist_example.png` | ナイキスト線図例<br>Example of Nyquist plot |
| `phase_gain_margin_example.png` | PM/GMの可視化付きボード線図<br>Bode plot with phase/gain margins |

---

## ⚙️ **実行環境・依存ライブラリ / Environment & Dependencies**

```bash
pip install control matplotlib numpy
```

- **対応Pythonバージョン**：3.8〜3.12  
  Compatible with Python 3.8–3.12  
- **推奨エディタ**：VSCode / Jupyter Lab / Google Colab  
  Recommended editors: VSCode, Jupyter Lab, Google Colab

---

## 🧠 **学習目標のまとめ / Summary of Learning Goals**

- **PID制御の動作理解とゲイン調整**  
  Understand PID behavior and gain tuning  
- **過渡応答・定常偏差の評価**  
  Analyze transient and steady-state response  
- **安定性判定（Routh / Root Locus / Nyquist）**  
  Assess stability using classical methods  
- **周波数応答とPM/GMによるロバスト設計**  
  Design for robustness using frequency response and stability margins

---

## 📚 **参考資料 / References**

- 「制御工学入門」森北出版  
  *Introduction to Control Engineering* – Morikita Publishing  
- *Feedback Control of Dynamic Systems* – Franklin, Powell, Emami-Naeini  
- 使用ライブラリ / Libraries: `control`, `matplotlib`, `numpy`

---

## 👤 **著者・ライセンス / Author & License**

| **項目 / Item** | **内容 / Details** |
|-----------------|--------------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo）<br>Shinshu University / Ex-Epson |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

📎 **[トップに戻る / Back to Home](../README.md)**
