---
layout: default
title: 02. Z変換と離散時間制御系
permalink: /part04_digital/theory/02_z_transform/
---

---

# 🔁 02. Z変換と離散時間制御系  
**🔁 02. Z-Transform & Discrete Control Representation**

> ℹ️ 数式が正しく表示されない場合は [GitHub版 / GitHub version](https://github.com/Samizo-AITL/EduController/blob/main/part04_digital/theory/02_z_transform.md) をご確認ください

---

ディジタル制御では、連続系のラプラス変換に対応する離散時間の変換手法として  
**Z変換**を用います。これは**差分方程式を伝達関数的に表現**するための基本です。

In digital control, the **Z-transform** is the discrete-time counterpart to the Laplace transform in continuous systems,  
providing a fundamental way to represent **difference equations as transfer functions**.

---

## 🎯 学習目標 / Learning Objectives

- Z変換の基本的な定義と性質を理解する  
  Understand the basic definition and properties of the Z-transform  
- 離散系伝達関数 $G(z)$ の導出と意味を把握する  
  Derive and interpret discrete-time transfer functions $G(z)$  
- 極・零点・安定性の概念をZ領域で理解できる  
  Understand poles, zeros, and stability in the Z-domain  
- 離散系と連続系の比較ができる  
  Compare discrete-time and continuous-time systems

---

## 📐 Z変換の定義 / Definition

離散信号 $x[k]$ に対して、Z変換は以下のように定義されます：

$$
X(z) = \mathcal{Z}\{x[k]\} = \sum_{k=0}^\infty x[k] z^{-k}
$$

- $z$ は複素数変数（ $z = re^{j\omega}$ ）  
  $z$ is a complex variable ($z = re^{j\omega}$)  
- $z^{-1}$ は1ステップの遅れに相当： $x[k-1] = z^{-1}x[k]$  
  $z^{-1}$ corresponds to a one-step delay: $x[k-1] = z^{-1}x[k]$

---

## 🔁 Z変換の基本性質 / Basic Properties

| **性質 / Property** | **内容 / Description** |
|----------------------|------------------------|
| 線形性 / Linearity | $\mathcal{Z}\{ax[k] + by[k]\} = aX(z) + bY(z)$ |
| 時間シフト / Time shift | $\mathcal{Z}\{x[k-n]\} = z^{-n}X(z)$ |
| 畳み込み定理 / Convolution | $x[k] * h[k] \leftrightarrow X(z)H(z)$ |

---

## 🏗️ 離散時間伝達関数 / Discrete-Time Transfer Function

- 連続系 / Continuous: $G(s) = \frac{Y(s)}{U(s)}$  
- 離散系 / Discrete: $G(z) = \frac{Y(z)}{U(z)}$

$$
G(z) = \frac{b_0 + b_1 z^{-1} + \dots + b_m z^{-m}}{1 + a_1 z^{-1} + \dots + a_n z^{-n}}
$$

- 差分方程式のZ変換から得られる  
  Obtained by taking the Z-transform of the difference equation

---

## ⚙️ 離散化（Tustin法など） / Discretization Methods

### Tustin（双一次変換 / Bilinear Transform）

$$
s = \frac{2}{T_s} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}
$$

- 安定性・周波数特性の維持に優れる  
  Preserves stability and frequency characteristics well

### ゼロ次ホールド（ZOH）変換 / Zero-Order Hold

- ラプラス変換 $G(s)$ からZ変換 $G(z)$ を直接求める  
  Directly derives $G(z)$ from $G(s)$ using ZOH assumption  
- MATLABでは `c2d()` 関数で変換可能  
  Available in MATLAB via `c2d()` function

---

## 🧩 安定性判定（Z平面） / Stability in the Z-Plane

- **すべての極が単位円内にある**とき安定  
  Stable if **all poles lie inside the unit circle**:

$$
|z_i| < 1 \quad \text{for all } i
$$

- $|z|=1$：限界安定（振動） / marginally stable (oscillations)  
- $|z|>1$：不安定 / unstable

---

## 🧪 活用例 / Applications

- PID制御器をZ領域で表現  
  Represent PID controllers in the Z-domain  
- フィルタ設計（FIR/IIR）の伝達関数構築  
  Construct transfer functions for FIR/IIR filters  
- FFT解析など離散信号処理との融合  
  Integrate with FFT analysis and other DSP techniques

---

## 📚 参考資料 / References

- Ogata, *Discrete-Time Control Systems*  
- Kuo, *Digital Control Systems*  
- MATLAB `c2d()` / `d2c()` Documentation

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part04_digital/theory/01_sampling_theory.html)**  
Covers sampling theory and Zero-Order Hold.

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part04_digital/theory/03_digital_pid.html)**  
Covers the design and comparison of discrete PID controllers.

**🏠 [Part 04 トップ / Back to Part 04 Top](https://samizo-aitl.github.io/EduController/part04_digital/)**
