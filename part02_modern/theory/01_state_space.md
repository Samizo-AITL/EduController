---
layout: default
title: 01. 状態空間表現の基礎
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

# 🧮 01. 状態空間表現の基礎

状態空間表現は、システムの動的挙動を**ベクトルと行列**で表すモダン制御理論の基礎です。本節では、状態方程式の構成、入出力との関係、連立微分方程式との対応を学びます。

---

## 🎯 学習目標

- 状態空間表現の構造と意味を理解する
- $A$, $B$, $C$, $D$ 行列の役割を説明できる
- 古典制御（伝達関数）との対応関係を理解する
- Pythonで状態空間モデルを扱えるようになる

---

## 📘 状態空間モデルとは？

状態空間表現は、以下のように記述されます：

$$
\\begin{aligned}
\\dot{x}(t) &= A x(t) + B u(t) \\\\
y(t) &= C x(t) + D u(t)
\\end{aligned}
$$

- $x(t)$：状態ベクトル（系の内部状態）
- $u(t)$：入力（制御信号）
- $y(t)$：出力（観測可能な量）

---

## 🧠 各行列の意味

| 行列 | 次元 | 役割 |
|------|------|------|
| $A$ | $(n \\times n)$ | 状態の自己遷移（システム行列） |
| $B$ | $(n \\times m)$ | 入力が状態に与える影響（入力行列） |
| $C$ | $(p \\times n)$ | 状態が出力に与える影響（出力行列） |
| $D$ | $(p \\times m)$ | 入力が出力に直接与える影響（フィードスルー） |

---

## 📦 例：2次系の状態空間化

システム：

$$
G(s) = \\frac{1}{s^2 + 3s + 2}
$$

状態空間形式に変換すると：

$$
\\begin{aligned}
\\dot{x}_1 &= x_2 \\\\
\\dot{x}_2 &= -2x_1 -3x_2 + u \\\\
y &= x_1
\\end{aligned}
$$

行列表記：

$$
A = \\begin{bmatrix} 0 & 1 \\\\ -2 & -3 \\end{bmatrix}, \quad
B = \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}, \quad
C = \\begin{bmatrix} 1 & 0 \\end{bmatrix}, \quad
D = 0
$$

---

## 🔧 Pythonでの実装例（`control` ライブラリ）

```python
import numpy as np
import control

A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

sys = control.ss(A, B, C, D)
print(sys)
```

---

## 🔁 状態空間と伝達関数の対応

状態空間 $\rightarrow$ 伝達関数：

$$
G(s) = C (sI - A)^{-1} B + D
$$

Pythonでは control.ss2tf() を使って変換できます。

---

## 📈 ステップ応答の例
```
import matplotlib.pyplot as plt
T, y = control.step_response(sys)
plt.plot(T, y)
plt.title("Step Response of State-Space System")
plt.grid(True)
plt.show()
```

---

## 🔍 状態の意味と設計視点
- 状態とは「システムの内部の記憶（履歴）」を最小限に保持する変数群
- 制御器設計では、この状態を操作・推定することが目的となる
- 例：モータ回転数→[位置, 速度] を状態とみなす

---

## 📚 参考資料
- 「現代制御理論入門」森北出版
- Franklin et al., Feedback Control of Dynamic Systems
- Python: control.ss, ss2tf, step_response

---
