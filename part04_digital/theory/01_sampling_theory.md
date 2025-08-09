---
layout: default
title: 01. サンプリングとディジタル制御の基礎
permalink: /part04_digital/theory/01_sampling_theory/
---

---

# ⏱️ 01. サンプリングとディジタル制御の基礎  
**⏱️ 01. Sampling Theory for Digital Control**

> ℹ️ 数式が正しく表示されない場合は [GitHub版](https://github.com/Samizo-AITL/EduController/blob/main/part04_digital/theory/01_sampling_theory.md) をご確認ください / If equations don’t render, see.

---

現代の制御系は、マイコン・DSP・FPGAなどの**ディジタル装置**を通じて実装されます。  
この章では、連続時間制御から**離散時間制御**への橋渡しとなる**サンプリング理論**を学びます。

In modern control systems, implementation is often realized using **digital devices** such as microcontrollers, DSPs, or FPGAs.  
This section introduces **sampling theory** as the bridge from **continuous-time control** to **discrete-time control**.

---

## 🎯 学習目標 / Learning Objectives

- サンプリングとゼロ次ホールド（ZOH）の概念を理解する  
  Understand the concept of sampling and Zero-Order Hold (ZOH)  
- ナイキスト定理とエイリアシングの危険性を説明できる  
  Explain the Nyquist theorem and the risks of aliasing  
- サンプリング周期 $T_s$ の設計指針を知る  
  Learn guidelines for selecting sampling periods $T_s$  
- 離散化における情報損失や遅延を意識できる  
  Recognize information loss and delays in discretization

---

## 📏 アナログとディジタルの違い / Analog vs. Digital

| **項目 / Item** | **アナログ系（連続時間） / Analog (Continuous)** | **ディジタル系（離散時間） / Digital (Discrete)** |
|------|-----------------------------------|-------------------------------------|
| 時間 / Time | 連続 $t$ | 離散 $kT_s$ |
| 処理 / Processing | 微分方程式 | 差分方程式 |
| 実装 / Implementation | 回路、アナログ演算 | マイコン、DSP、FPGAなど |

---

## 📐 サンプリングとは？ / What is Sampling?

- 時間的に連続な信号 $x(t)$ を、周期 $T_s$ で離散化する処理  
  Sampling converts a continuous-time signal $x(t)$ into discrete values at period $T_s$.  
- 離散信号： $x[k] = x(kT_s)$

### ゼロ次ホールド（ZOH） / Zero-Order Hold

- 離散信号を連続系に戻す際、**前の値を保持する**方式  
  Converts discrete signals back to continuous by **holding the previous value**.  
- 実機マイコンのD/A変換器の多くがこの方式を採用  
  Commonly used in DACs of microcontrollers.

---

## 📈 ナイキスト定理 / Nyquist Theorem

- **正確に再現するには $f_s > 2f_{\text{max}}$**  
  To perfectly reconstruct, the sampling frequency must satisfy:  
  $f_s > 2f_{\text{max}}$  
- $f_{\text{max}}$：信号中の最大周波数 / maximum frequency in the signal  
- $f_s$：サンプリング周波数 / sampling frequency  
- $T_s = 1/f_s$

### エイリアシング / Aliasing

- サンプリング不足で高周波成分が**誤って低周波に見える**現象  
  High-frequency components appear as false low frequencies when under-sampled.  
- 対策 / Prevention:
  - サンプリング前に**ローパスフィルタ（アンチエイリアス）**  
    Low-pass filtering before sampling (anti-alias filter)  
  - 十分高いサンプリング周波数を選定  
    Choose sufficiently high $f_s$

---

## 🧠 サンプリング周期の設計指針 / Guidelines for $T_s$

- 一般に「**閉ループ帯域の10倍以上**」が目安  
  A rule of thumb: at least **10× the closed-loop bandwidth**  
  - 閉ループ立ち上がり時間 $T_r$ に対し、 $T_s < T_r / 10$
- 遅すぎると / Too slow:
  - 応答遅延、振動、安定性悪化  
    Response delays, oscillations, degraded stability  
- 速すぎると / Too fast:
  - 実装負荷、演算量・通信量の増加  
    Higher computational load and communication demand

---

## 🧪 実験例 / Example Simulation

- 同じ1次系に対し、 $T_s = 0.01, 0.1, 0.5$ で応答比較  
  Compare responses of a first-order system for different $T_s$ values.  
- サンプリング遅延の影響:
  - 応答遅延 / Response delay  
  - 量子化による階段状波形 / Step-like output from quantization  
  - 発散・不安定化（極端な場合）/ Divergence or instability in extreme cases

---

## 📚 参考資料 / References

- Ogata, *Discrete-Time Control Systems*  
- Franklin et al., *Digital Control of Dynamic Systems*  
- 岡部洋一『ディジタル制御入門』 (*Introduction to Digital Control*)

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part04_digital/)**  
Part 04 の概要と学習目標を説明します。  
Overview and learning objectives of Part 04.

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part04_digital/theory/02_z_transform.html)**  
Z変換と離散時間伝達関数を学びます。  
Covers Z-transform and discrete-time transfer functions.

**🏠 [Part 04 トップ / Back to Part 04 Top](https://samizo-aitl.github.io/EduController/part04_digital/)**
