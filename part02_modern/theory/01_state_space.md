---
layout: default
title: 🧮 状態空間表現の基礎 / Basics of State-Space Representation
permalink: /part02_modern/theory/01_state_space.html
---

---

# 🧮 01. 状態空間表現の基礎  
**01. Basics of State-Space Representation**

---

状態空間表現は、システムの動的挙動を**ベクトルと行列**で表すモダン制御理論の基礎です。本節では、状態方程式の構成、入出力との関係、伝達関数との対応、そしてPythonによる実装までを学びます。  
State-space representation expresses dynamics with **vectors and matrices**. This section covers the structure of state equations, the relation to inputs/outputs, the correspondence to transfer functions, and a short Python implementation.

---

## 🎯 学習目標｜Learning Objectives
- **状態空間の構造と意味を理解する**  
  Understand the structure and meaning of the state-space model  
- **$A,B,C,D$ 行列の役割を説明できる**  
  Explain the roles of the $A,B,C,D$ matrices  
- **伝達関数との対応関係を示せる**  
  Relate state-space to transfer functions  
- **Pythonで状態空間モデルを扱える**  
  Build and simulate state-space models in Python

---

## 📘 状態空間モデルとは？｜What is a State-Space Model?
連続時間の線形時不変（LTI）系は、次で表されます：  
An LTI continuous-time system is written as:

$$
\begin{aligned}
\dot{x}(t) &= A\,x(t) + B\,u(t) \\
y(t) &= C\,x(t) + D\,u(t)
\end{aligned}
$$

- **$x(t)$：状態ベクトル / state vector** — 系の内部記憶  
- **$u(t)$：入力 / input** — 制御信号  
- **$y(t)$：出力 / output** — 観測可能量

---

## 🧠 各行列の意味｜Meaning of Each Matrix

<table>
<tr><th>行列</th><th>次元 / Dimension</th><th>役割 / Role</th></tr>
<tr><td><b>$A$</b></td><td>$(n \times n)$</td><td>状態の自己遷移（システム行列） / State transition (system matrix)</td></tr>
<tr><td><b>$B$</b></td><td>$(n \times m)$</td><td>入力が状態に与える影響 / How inputs affect states</td></tr>
<tr><td><b>$C$</b></td><td>$(p \times n)$</td><td>状態が出力に与える影響 / How states affect outputs</td></tr>
<tr><td><b>$D$</b></td><td>$(p \times m)$</td><td>入力の直接通過（フィードスルー） / Direct feedthrough</td></tr>
</table>

---

## 📦 例：2次系の状態空間化｜Example: 2nd-Order System
伝達関数：

$$
G(s)=\frac{1}{s^2+3s+2}
$$

可制御正準形の一例：  
One possible controllable canonical form:

$$
\begin{aligned}
\dot{x}_1 &= x_2 \\
\dot{x}_2 &= -2x_1 - 3x_2 + u \\
y &= x_1
\end{aligned}
$$

行列表記：  
Matrix form:

$$
A = \begin{bmatrix}
0 & 1 \\
-2 & -3
\end{bmatrix}, \quad
B = \begin{bmatrix}
0 \\
1
\end{bmatrix}, \quad
C = \begin{bmatrix}
1 & 0
\end{bmatrix}, \quad
D = \begin{bmatrix}
0
\end{bmatrix}
$$

---

## 🔁 伝達関数との対応｜Relation to Transfer Function
状態空間 $\rightarrow$ 伝達関数：  
From state-space to transfer function:

$$
G(s)=C\,(sI-A)^{-1}B + D.
$$

---

## 🔧 Python実装例｜Python Example (`python-control`)
```python
import numpy as np
import control

A = np.array([[0, 1],
              [-2, -3]])
B = np.array([[0],
              [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# 状態空間モデル
sys = control.ss(A, B, C, D)
print(sys)

# 伝達関数へ変換
G = control.ss2tf(sys)
print(G)

# ステップ応答
T, y = control.step_response(sys)
import matplotlib.pyplot as plt
plt.plot(T, y)
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.title("Step Response (State-Space)")
plt.grid(True)
plt.show()
```

---

## 🔍 設計視点のメモ｜Design Notes
- **状態**は「必要最小限の内部記憶」。制御器はこの状態を**操作**（フィードバック）し、未観測成分は**推定**（オブザーバ）する。  
- 代表的な例：モータなら状態を **[位置, 速度]** とする、など。  
- 後続節で**可制御性・可観測性**を判定し、**極配置**や**オブザーバ設計**へ進む。

---

**➡️➡️ [次節 / Next Section](https://samizo-aitl.github.io/EduController/part02_modern/theory/02_controllability.html)**  
可制御性と可観測性、Kalmanランク条件を学びます。  
Learn controllability, observability, and the Kalman rank conditions.

**📚 [この章のREADMEへ / Back to Part 2 README](https://samizo-aitl.github.io/EduController/part02_modern/README.html)**  
章の概要・教材一覧に戻ります。  
Return to the Part 2 overview and materials list.
