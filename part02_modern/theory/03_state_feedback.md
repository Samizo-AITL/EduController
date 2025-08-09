---
layout: default
title: 03. 状態フィードバックと極配置 / State Feedback & Pole Placement
permalink: /part02_modern/theory/03_state_feedback.html
---

---

# 🎛️ 03. 状態フィードバックと極配置 / State Feedback & Pole Placement

> **Note:** 数式が正しく表示されない場合は [GitHub版](https://github.com/Samizo-AITL/EduController/blob/main/part02_modern/theory/03_state_feedback.md) を参照してください。

---

**状態空間モデル**を使うことで、システムの応答特性（安定性・速度・減衰など）を**極の配置**で設計できます。  
本節では、**状態フィードバック制御**と**極配置法（Pole Placement）**の理論・設計手法を解説します。

Using a **state-space model**, you can design system dynamics (stability, speed, damping) by **placing poles**.  
This section covers the theory and methods of **state feedback control** and **pole placement**.

---

## 🎯 学習目標 / Learning Goals

| 日本語 / Japanese | English |
|-------------------|---------|
| 状態フィードバック制御の構造を理解する | Understand the structure of state feedback control |
| 極配置による応答設計を理解する | Learn to design response by pole placement |
| 可制御性が極配置の前提条件であることを説明できる | Explain controllability as a prerequisite |
| Pythonで極配置制御器を設計できる | Implement pole placement controller in Python |

---

## 📐 状態フィードバックとは？ / What is State Feedback?

**構造 / Structure**  

$$
u(t) = -K x(t) + r(t)
$$

- **$K$**: 状態フィードバックゲイン  
- **$r(t)$**: 参照入力  
- これにより**閉ループ極**を任意に設定可能  

---

### ✅ 閉ループ系の方程式 / Closed-loop Equation

オリジナル系：  

$$
\dot{x} = A x + B u
$$

フィードバック $u = -Kx + r$ を代入： 

$$
\dot{x} = (A - BK) x + Br
$$

- 状態行列が **$A - BK$** に変わる  
- 極配置はこの固有値を設計すること

---

## 🧠 極配置の目的 / Purpose of Pole Placement

| 日本語 / Japanese | English |
|-------------------|---------|
| 極は安定性・応答速度・減衰を決定 | Poles determine stability, speed, damping |
| 左半平面にあれば安定 | Stable if in the left-half plane |
| 原点近い → 遅い応答 | Near origin → slow response |
| 左に遠い → 高速応答（ただしゲイン大） | Far left → fast response (high gain risk) |
| 複素極の虚部 → 振動特性 | Imaginary part of complex poles → oscillations |

---

## ✅ 極配置可能な条件 / Condition for Pole Placement

- **完全可制御（Fully Controllable）** が必要  
- 可制御でない場合、**一部の極は動かせない**

---

## 📘 設計例 / Example

2次系： 

$$
A = \begin{bmatrix}
0 & 1 \\
-2 & -3
\end{bmatrix}, \quad
B = \begin{bmatrix}
0 \\
1
\end{bmatrix}
$$

目標極（例）： $s = -2$, $s = -5$

---

## 🧪 Pythonでの極配置 / Pole Placement in Python

```python
import numpy as np
import control

A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])

# 目標極 / Desired poles
desired_poles = [-2, -5]

# フィードバックゲイン計算 / Compute feedback gain
K = control.place(A, B, desired_poles)
print("Gain K:", K)

# 閉ループ系の確認 / Check closed-loop poles
A_cl = A - B @ K
print("Closed-loop eigenvalues:", np.linalg.eigvals(A_cl))
```

---

## 📈 ステップ応答で確認 / Step Response Check

```python
C = np.array([[1, 0]])
D = np.array([[0]])
sys_cl = control.ss(A_cl, B, C, D)

import matplotlib.pyplot as plt
T, y = control.step_response(sys_cl)
plt.plot(T, y)
plt.title("Step Response of Closed-Loop System")
plt.grid(True)
plt.show()
```

---

## 💡 設計のヒント / Design Tips

| 日本語 / Japanese | English |
|-------------------|---------|
| 極を左に配置しすぎる → 高速だがゲイン大・ノイズ感度増加 | Far left → fast but high gain & noise sensitivity |
| PID設計同様、速度・振動・安定性のバランス重要 | Balance speed, oscillation, stability like PID |
| モデル精度・可制御性・最小位相性を確認 | Verify model accuracy, controllability, minimum-phase |

---

## 📚 参考資料 / References

- 「現代制御理論入門」森北出版  
- *Modern Control Engineering* – K. Ogata  
- Python: `control.place()`, `control.ss()`, `step_response()`

---

**⬅️ [前節 / Previous Section](https://samizo-aitl.github.io/EduController/part02_modern/theory/02_controllability.html)**  
可制御性と可観測性の基礎を解説します。  
Covers the basics of controllability & observability.

**➡️ [次節 / Next Section](https://samizo-aitl.github.io/EduController/part02_modern/theory/04_observer_design.html)**  
オブザーバ設計と推定器の理論を解説します。  
Covers observer design and estimation theory.

**📚 [この章のREADMEへ / Back to Part 2 README](https://samizo-aitl.github.io/EduController/part02_modern/README.html)**  
現代制御理論の全体構成と教材一覧に戻ります。  
Return to the full Part 2 structure and materials list.
