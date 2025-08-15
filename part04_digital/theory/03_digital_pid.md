---
layout: clean
title: 03. 離散PID制御の設計
permalink: /part04_digital/theory/03_digital_pid.html
---

---

# 🧮 03. 離散PID制御の設計  
**🧮 03. Digital PID Controller Design**

> ℹ️ 数式が正しく表示されない場合は [GitHub版 / GitHub version](https://github.com/Samizo-AITL/EduController/blob/main/part04_digital/theory/03_digital_pid.md) をご確認ください

---

PID制御器はディジタル制御においても依然として主流のアルゴリズムです。  
この章では、**連続時間のPIDをZ変換**により**離散時間制御器へ変換**する方法を扱います。

The PID controller remains a dominant algorithm in digital control.  
This section covers how to **convert a continuous-time PID into a discrete-time controller** using the **Z-transform**.

---

## 🎯 学習目標 / Learning Objectives

- PID制御器の離散化方法を理解する  
  Understand methods of discretizing PID controllers  
- 前進差分、後退差分、Tustin法の違いを比較できる  
  Compare forward difference, backward difference, and Tustin methods  
- Pythonで離散PIDを実装し、応答を観察できる  
  Implement a discrete PID in Python and observe responses  
- 離散化による遅延・量子化の影響を認識できる  
  Recognize the effects of discretization on delay and quantization

---

## 🔁 連続PID制御器の構造 / Continuous-Time PID Structure

$$
u(t) = K_p e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}
$$

- $K_p$：比例ゲイン / Proportional gain  
- $K_i$：積分ゲイン / Integral gain  
- $K_d$：微分ゲイン / Derivative gain  
- この制御則を**差分方程式に変換**して離散時間で実装する  
  This control law is **converted into a difference equation** for discrete-time implementation.

---

## 🔀 離散化手法の比較 / Discretization Methods

### ① 前進差分（Forward Euler）

- 微分 / Derivative: $\frac{de(t)}{dt} \approx \frac{e[k+1] - e[k]}{T_s}$  
- 積分 / Integral: $\int e(t)\,dt \approx \sum e[k] T_s$

### ② 後退差分（Backward Euler）

- 微分 / Derivative: $\frac{e[k] - e[k-1]}{T_s}$  
- 積分 / Integral: $I[k] = I[k-1] + e[k] T_s$

### ③ 双一次変換（Tustin法 / Bilinear Transform）

- 安定性・周波数応答を保つ変換  
  Maintains stability and frequency characteristics  
- ラプラス領域の $s$ を Z領域へ変換  
  Replace $s$ in Laplace domain with:

$$
s \approx \frac{2}{T_s} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}
$$

---

## 🧮 離散PIDの実装例（Tustin法） / Example (Tustin Method)

$$
G_c(z) = K_p + K_i \cdot \frac{T_s}{2} \cdot \frac{1 + z^{-1}}{1 - z^{-1}} + K_d \cdot \frac{2}{T_s} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}
$$

- 上記は Z 領域での PID 制御器  
  Above is the PID controller in the Z-domain  
- 差分方程式に変換し、逐次計算で実装可能  
  Can be implemented via sequential calculation in difference equation form

---

## 🧪 Pythonでの実験 / Python Simulation

- 同一プラント（1次系または2次系）に対し：  
  For the same plant (1st or 2nd order system):
  - 連続PID vs 離散PID（Tustin）  
    Continuous PID vs discrete PID (Tustin)  
- サンプリング周期やゲインによる挙動の違いを観察  
  Observe differences in behavior due to sampling time and gains  
- 離散化による遅れ、微分ノイズの影響を評価  
  Evaluate delay and derivative noise caused by discretization

---

## 🧠 実装上の注意点 / Implementation Notes

| **要素 / Element** | **注意事項 / Remarks** |
|---------------------|------------------------|
| 積分項 / Integral term | ワインドアップ防止が必要 / Anti-windup required |
| 微分項 / Derivative term | 雑音増幅防止に微分先行型やLPF併用 / Use derivative-on-measurement or LPF to avoid noise amplification |
| サンプリング周期 / Sampling period | 遅すぎると安定性低下、速すぎると計算負荷増 / Too slow → instability, too fast → high computational load |

---

## 📚 参考資料 / References

- Åström & Hägglund, *PID Controllers: Theory, Design, and Tuning*  
- Ogata, *Discrete-Time Control Systems*  
- MATLAB `pid()` / `pidTuner` Documentation

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part04_digital/theory/02_z_transform.html)**  
Z変換の定義・性質・安定性判定を解説し、離散時間制御の基礎数学を整理しています。  
Covers the Z-transform definition, properties, and stability criteria — the mathematical foundation for discrete-time control.

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part04_digital/theory/04_fir_iir_filter.html)**  
FIR/IIRフィルタの構造と設計法を学び、離散制御器や信号処理との接続に発展します。  
Covers FIR/IIR filter structures and design methods, extending toward discrete controllers and signal processing.

**🏠 [Part 04 トップ / Back to Part 04 Top](https://samizo-aitl.github.io/EduController/part04_digital/)**  
本章全体の目次と概要に戻ります。  
Returns to the table of contents and overview of Part 04.
