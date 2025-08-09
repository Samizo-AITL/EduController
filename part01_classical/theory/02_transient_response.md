---
layout: default
title: ⚡️ 過渡応答と定常偏差の基礎 / Transient Response & Steady-State Error
permalink: /part01_classical/theory/02_transient_response.html
---

---

# ⚡️ 02. 過渡応答と定常偏差の基礎  
**02. Fundamentals of Transient Response & Steady-State Error**

制御系の性能を評価する上で、「どれだけ速く」「どれだけ正確に」目標値に到達するかは重要な指標です。本節では、時間領域での応答特性を中心に、過渡応答と定常誤差について学びます。  
In control system performance evaluation, *how fast* and *how accurately* the system reaches its target are key indicators. This section focuses on transient response and steady-state error in the time domain.

---

## 🎯 本節の学習目標｜Learning Objectives

- **過渡応答の各評価指標を理解する**  
  Understand transient response metrics (rise time, overshoot, settling time)  
- **1次・2次系の典型応答を把握する**  
  Recognize typical step responses of first- and second-order systems  
- **定常偏差の計算方法を習得する**  
  Learn how to calculate steady-state error  
- **速さと精度のトレードオフを理解する**  
  Understand the trade-off between speed and accuracy

---

## ⏱️ 過渡応答とは？｜What is Transient Response?

---

**過渡応答（transient response）** とは、ステップ入力などに対して出力が定常状態に到達するまでの一時的な振る舞いを指します。  
Transient response refers to the short-term behavior before the output settles in steady state after an input, such as a step.

---

### ✅ 代表的な評価指標｜Typical Performance Metrics

| 指標 / Metric | 記号 / Symbol | 説明 / Description |
|---------------|--------------|--------------------|
| **立ち上がり時間 / Rise time** | $t_r$ | 応答が10%〜90%に達するまでの時間 / Time to rise from 10% to 90% |
| **オーバーシュート / Overshoot** | $M_p$ | 最大値が目標値を何％超えるか / % amount output exceeds target |
| **セトリング時間 / Settling time** | $t_s$ | 応答が±2%以内に収束する時間 / Time to settle within ±2% band |
| **定常偏差 / Steady-state error** | $e_{ss}$ | 長時間後に残る誤差 / Error remaining after a long time |

---

## 📉 1次遅れ系の応答｜First-Order Response

**システム / System:**

$$
G(s) = \frac{1}{\tau s + 1}
$$

**ステップ応答 / Step Response:**

$$
y(t) = 1 - e^{-t/\tau}
$$

- $\tau$: 時定数 / Time constant  
- 過渡応答は単調増加、振動なし  
- $t = \tau$ で出力は約63.2%到達 / Reaches ~63.2% at $t=\tau$

---

## 🎯 2次系の応答（減衰あり）｜Second-Order Response (Damped)

**システム / System:**

$$
G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}
$$

**減衰比 $\zeta$ による特徴 / Characteristics by damping ratio:**

- $0 < \zeta < 1$：アンダーダンプ（振動あり） / Underdamped (oscillatory)  
- $\zeta = 1$：臨界減衰（最速・無振動） / Critically damped (fastest no overshoot)  
- $\zeta > 1$：オーバーダンプ（遅い・無振動） / Overdamped (slow, no overshoot)

**オーバーシュートと減衰比の関係 / Overshoot vs Damping Ratio:**

$$
M_p = e^{\left( -\frac{\pi \zeta}{\sqrt{1 - \zeta^2}} \right)} \times 100[\%]
$$

---

## 🎯 定常偏差 $e_{ss}$ の計算｜Calculating Steady-State Error

閉ループ系:

$$
T(s) = \frac{G(s)C(s)}{1 + G(s)C(s)}
$$

単位ステップ入力 $R(s) = 1/s$ に対して:

$$
e_{ss} = \lim_{s \to 0} \left[ \frac{1}{1 + G(s)C(s)} \right]
$$

**代表例 / Examples:**

| 系の型 / System Type | 定常偏差（ステップ） / Steady-State Error |
|----------------------|-------------------------------------------|
| Type 0 | 非ゼロ / Non-zero |
| Type 1 | ゼロ / Zero |
| Type 2 | ゼロ / Zero |

---

## 🧪 Pythonによる可視化例｜Python Visualization Example

1次・2次遅れ系の応答比較例  
Example comparing first- and second-order system responses  

参照 / See: [`/simulation/transient_response.py`](../simulation/transient_response.py)  

使用ライブラリ: `control`, `matplotlib`, `numpy`  
Libraries: `control`, `matplotlib`, `numpy`

---

## 💬 実務的視点｜Practical Notes

- 速い応答は振動やオーバーシュートを招きやすい  
  Faster responses tend to cause oscillations and overshoot  
- PID設計では $M_p$, $t_s$ を設計仕様として用いる  
  In PID design, $M_p$ and $t_s$ are key design specs  
- 実機ではノイズ・センサ遅れも重要要因  
  In hardware, noise and sensor delays are important

---

## 📚 参考資料｜References

- 森北出版「制御工学」  
- Franklin et al., *Feedback Control of Dynamic Systems*  
- Python: `control`, `matplotlib`

---

**⬅️ [前節 / Previous Section](https://samizo-aitl.github.io/EduController/part01_classical/theory/01_pid_control.html)**  
PID制御の原理と各要素の役割を学びます。  
Covers principles and effects of PID control.

**➡️➡️ [次節 / Next Section](https://samizo-aitl.github.io/EduController/part01_classical/theory/03_stability_methods.html)**  
安定性の判別法（Routh表、根軌跡、ナイキスト法）を解説します。  
Explains stability criteria (Routh table, root locus, Nyquist method).

**📚 [この章のREADMEへ / Back to Part 1 README](https://samizo-aitl.github.io/EduController/part01_classical/)**  
古典制御理論の全体構成と教材一覧に戻ります。  
Return to the full Part 1 structure and materials list.
