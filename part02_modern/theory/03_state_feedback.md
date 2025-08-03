---
layout: default
title: 01. PID制御の基礎
---

<!-- MathJax support for both inline and block math -->
<script type="text/javascript">
  window.MathJax = {
    tex: { inlineMath: [['$', '$'], ['\\(', '\\)']] },
    svg: { fontCache: 'global' }
  };
</script>
<script type="text/javascript"
  async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

# 🎛️ 03. 状態フィードバックと極配置（Pole Placement）

状態空間モデルを使うことで、システムの応答特性（安定性、速度、減衰など）を**極の配置によって設計**できます。本節では、**状態フィードバック制御**と**極配置法（pole placement）**の理論と設計手法を学びます。

---

## 🎯 学習目標

- 状態フィードバック制御の構造を理解する  
- 極配置により応答の極を設計できることを理解する  
- 可制御性が極配置の前提条件であることを説明できる  
- Pythonで極配置制御器を設計できるようになる

---

## 📐 状態フィードバックとは？

制御入力を状態に基づいてフィードバックする構造：

$$
u(t) = -K x(t) + r(t)
$$

これにより、**閉ループ系の極（固有値）を任意に配置**することが可能になります。

---

### ✅ 閉ループ系の方程式

オリジナル系：

$$
\dot{x} = A x + B u
$$

制御入力 $u = -Kx + r$ を代入すると：

$$
\dot{x} = (A - BK) x + Br
$$

- 状態行列が $A - BK$ に置き換わる
- これにより**極配置が実現**

---

## 🧠 極配置の目的

- 極はシステムの**安定性・応答速度・減衰**を決める  
- 例：
  - 極が左半平面にあれば安定
  - 極が原点に近ければ遅い、遠ければ速い
  - 複素極の虚部は振動を生む

---

## ✅ 極配置可能な条件

- **完全可制御（Controllable）** が必要条件  
- 可制御性がないと、極の一部しか動かせない

---

## 📘 設計例

2次系：

$$
A = \begin{bmatrix} 0 & 1 \\\\ -2 & -3 \end{bmatrix}, \quad
B = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}
$$

目標極（例）： $s = -2$, $s = -5$

---

## 🧪 Pythonでの極配置（`control.place()`）

```python
import numpy as np
import control

A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])

# 目標極
desired_poles = [-2, -5]

# フィードバックゲイン計算
K = control.place(A, B, desired_poles)
print("Gain K:", K)

# 閉ループ系の確認
A_cl = A - B @ K
print("Closed-loop eigenvalues:", np.linalg.eigvals(A_cl))
```

---

## 📈 ステップ応答で確認
```
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

## 💡 設計のヒント
- 極を左に配置しすぎると速くなるが、過大ゲインやノイズ感度上昇のリスク
- PID設計と同様、速度・振動・安定性のトレードオフを意識
- 最小位相系・可制御性・モデル精度が重要

---

## 📚 参考資料
- 「現代制御理論入門」森北出版
- Ogata, Modern Control Engineering
- Python: control.place(), control.ss(), step_response()

---


