---
layout: default
title: 📉 周波数応答とボード線図の基礎 / Frequency Response & Bode Plot Basics
permalink: /part01_classical/theory/04_frequency_response.html
---

---

# 📉 04. 周波数応答とボード線図の基礎  
**04. Basics of Frequency Response & Bode Plot**

---

**ボード線図（Bode plot）** は、制御系の周波数応答特性を視覚的に評価するための基本ツールです。本節では、ボード線図の読み方・描き方、ゲイン交差周波数・位相余裕の意味、安定性やロバスト性との関係を学びます。  
The **Bode plot** is a fundamental tool to visualize the frequency response of a control system. This section explains how to read and draw Bode plots, the meaning of gain crossover frequency and phase margin, and their relation to stability and robustness.

---

## 🎯 本節の学習目標｜Learning Objectives

- 周波数応答の定義を理解する  
  Understand the definition of frequency response  
- ボード線図の構成（ゲイン・位相）を把握する  
  Understand the structure of a Bode plot (gain & phase)  
- ゲイン交差周波数と位相余裕の意味を説明できる  
  Explain gain crossover frequency & phase margin  
- 安定性とロバスト性の観点から周波数特性を評価できる  
  Evaluate frequency response in terms of stability & robustness

---

## 🎧 周波数応答とは？｜What is Frequency Response?

システム $G(s)$ において $s = j\omega$ とすると、**周波数応答**が得られます：  
In a system $G(s)$, substituting $s = j\omega$ yields the **frequency response**:

$$
G(j\omega) = |G(j\omega)| \angle \arg(G(j\omega))
$$

- **振幅特性 / Magnitude**：入力に対する出力の大きさ  
- **位相特性 / Phase**：入力と出力の間の位相差（遅れ）

---

## 📊 ボード線図の構成｜Bode Plot Structure

- **横軸 / X-axis**：周波数（対数スケール, [rad/s]）  
- **縦軸（上段） / Upper Y-axis**：ゲイン（dB） → $20 \log_{10} |G(j\omega)|$  
- **縦軸（下段） / Lower Y-axis**：位相（deg） → $\arg G(j\omega)$  

ボード線図は、ゲイン特性と位相特性を上下2つのグラフで表示します。  
A Bode plot displays magnitude and phase characteristics in two separate graphs.

---

## 🧠 重要な周波数点｜Key Frequency Points

### ✅ ゲイン交差周波数 / Gain Crossover Frequency $\omega_g$
- ゲインが $|G(j\omega)| = 1$（0 dB）になる周波数  
- Frequency at which the magnitude is 1 (0 dB)

### ✅ 位相交差周波数 / Phase Crossover Frequency $\omega_p$
- 位相が $\angle G(j\omega) = -180^\circ$ となる周波数  
- Frequency at which the phase is $-180^\circ$

---

## 🛡️ 安定性とロバスト性｜Stability & Robustness

### 位相余裕 / Phase Margin (PM)

$$
\text{PM} = 180^\circ + \angle G(j\omega_g)
$$  

- ゲイン交差周波数における位相の余裕  
- Phase margin at gain crossover frequency

### ゲイン余裕 / Gain Margin (GM)

$$
\text{GM} = \frac{1}{|G(j\omega_p)|} \quad \text{or} \quad -20\log_{10}|G(j\omega_p)|
$$  

- 位相交差周波数におけるゲインの余裕  
- Gain margin at phase crossover frequency

**経験則 / Rules of Thumb**:  
- PM > 30°  
- GM > 6 dB

---

## 🔧 典型的な応答例｜Typical Responses

| 要素 / Element | ゲイン傾き / Gain Slope | 位相変化 / Phase Shift |
|----------------|------------------------|------------------------|
| 積分器 $1/s$ | -20 dB/dec | -90° |
| 微分器 $s$   | +20 dB/dec | +90° |
| 一次遅れ     | -20 dB/dec | -90° (asymptotic) |
| 二次遅れ     | -40 dB/dec | -180° (asymptotic) |

---

## 🧪 Python実装例｜Python Example

```python
import control
import matplotlib.pyplot as plt

# Example: Second-order system
G = control.tf([1], [1, 2, 1])
control.bode_plot(G, dB=True, Hz=False, deg=True)
plt.show()
```

- `control.bode_plot`: ゲイン・位相を一括描画  
  Plots gain and phase in one function  
- `matplotlib`で調整・保存可能  
  Adjustable and savable with matplotlib

📂 出力例: `/figures/bode_example.png`  
Example output: `/figures/bode_example.png`

---

## 📚 参考資料｜References
- 森北出版「制御工学」  
- Franklin et al., *Feedback Control of Dynamic Systems*  
- Python: `control`, `matplotlib`

---

**⬅️ [前節 / Previous Section](./03_stability_methods.html)**  
安定性判別法（Routh・根軌跡・ナイキスト）を学びます。  
Covers stability determination methods (Routh, Root Locus, Nyquist).

**➡️➡️ [次節 / Next Section](./05_pid_design.html)**  
PID設計のパラメータ調整と実装方法を解説します。  
Explains PID tuning methods and implementation.

**📚 [この章のREADMEへ / Back to Part 1 README](../README.md)**  
古典制御理論の全体構成と教材一覧に戻ります。  
Return to the full Part 1 structure and materials list.
