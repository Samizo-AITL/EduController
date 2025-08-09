---
layout: default
title: 倒立振子の状態空間モデル（線形化）
permalink: /pendulum/state_space_linearization/
---

# 📘 倒立振子の状態空間モデル（線形化）  
Linearized State-Space Model of the Inverted Pendulum

> **Web数式が表示されない場合**はこちらのGitHub版をご覧ください：  
> [📄 GitHubで数式表示を確認](https://github.com/Samizo-AITL/EduController/blob/main/pendulum/state_space_linearization.md)

---

## ✅ モデル概要 / Model Overview

- **状態変数 / State Variables**  
  $x$: カート位置 (cart position)  
  $\dot{x}$: カート速度 (cart velocity)  
  $\theta$: 振子角度（鉛直からのずれ）(pendulum angle from vertical)  
  $\dot{\theta}$: 角速度 (angular velocity)

- **入力 / Input**  
  $u$: カートに加える力 (applied force to the cart)

---

## 📐 状態空間表現（線形化後） / Linearized State-Space Representation

平衡点（equilibrium point）： $\theta = 0$（鉛直上向き / upright position）

**A行列 / A Matrix**

$$
A =
\begin{bmatrix}
0 & 1 & 0 & 0 \\
0 & 0 & -\frac{mg}{M} & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & \frac{(M + m)g}{Ml} & 0
\end{bmatrix}
$$

**B行列 / B Matrix**

$$
B =
\begin{bmatrix}
0 \\
\frac{1}{M} \\
0 \\
-\frac{1}{Ml}
\end{bmatrix}
$$

---

## 🧮 数値代入（例） / Numerical Example

- $M = 1.0 \, \mathrm{kg}$  
- $m = 0.1 \, \mathrm{kg}$  
- $l = 0.5 \, \mathrm{m}$  
- $g = 9.81 \, \mathrm{m/s^2}$  

**A（数値）:**

```python
[[0, 1.0,     0,   0],
 [0, 0,  -0.981,   0],
 [0, 0,     0,  1.0],
 [0, 0, 21.582,   0]]
```

**B（数値）:**

```python
[[ 0.0 ],
 [ 1.0 ],
 [ 0.0 ],
 [-2.0 ]]
```

---

## 📉 ステップ応答（概形） / Step Response (Example)

ここでは、単純な1次遅れ近似応答例を示します（時定数 $\tau = 1.0$）。  

**モデル式 / Model Equation**:  
$$
x(t) = 1 - e^{-t/\tau}
$$

**Python例 / Python Example**:

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 100)
tau = 1.0
x = 1 - np.exp(-t/tau)

plt.plot(t, x)
plt.xlabel("Time [s]")
plt.ylabel("Response x(t)")
plt.title("Step Response (τ = 1.0)")
plt.grid(True)
plt.show()
```

---

## 🔗 関連リンク / Related Links

- [📄 倒立振子モデル（非線形版）](../state_space_nonlinear/)  
- [📄 LQR制御による安定化](../lqr_control/)  

---

**🏠 [ホームへ戻る / Back to Home](../../README.md)**
