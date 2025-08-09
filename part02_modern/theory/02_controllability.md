---
layout: default
title: 02. 可制御性と可観測性の基本 / Controllability & Observability
permalink: /part02_modern/theory/02_controllability.html
---

# 🔍 02. 可制御性と可観測性の基本 / Basics of Controllability & Observability

---

**状態空間モデル**を使って制御系を設計する際には、  
「**その状態を操作できるか？**」と「**外部から推定できるか？**」という2つの性質が極めて重要です。  
本節では、**可制御性（Controllability）** と **可観測性（Observability）** の定義、数学的検査法、工学的意味を解説します。

When designing control systems with **state-space models**,  
two key properties are: **Can we control the states?** and **Can we observe them externally?**  
This section explains the **definitions**, **mathematical tests**, and **engineering implications** of **controllability** and **observability**.

---

## 🎯 学習目標 / Learning Goals

| 日本語 / Japanese | English |
|-------------------|---------|
| 可制御性・可観測性の概念を理解する | Understand the concepts of controllability & observability |
| Kalmanのランク条件による判別法を説明できる | Explain Kalman's rank condition |
| Pythonで可制御性・可観測性を検査できる | Test these properties in Python |
| 極配置・オブザーバ設計の土台を築く | Build the foundation for pole placement & observer design |

---

## ⚙️ 可制御性とは？ / What is Controllability?

**定義 / Definition**  
ある初期状態 $x(0)$ から任意の状態 $x(t)$ に、**有限時間で到達できる**性質。  
The property that any initial state $x(0)$ can be driven to any desired state $x(t)$ in **finite time**.

**Kalman 可制御性行列 / Controllability Matrix**  

$$
\mathcal{C} =
\begin{bmatrix}
B & AB & A^2B & \cdots & A^{n-1}B
\end{bmatrix}
$$

- **$\mathrm{rank}(\mathcal{C}) = n$** → 完全可制御 / Fully controllable  
- **$\mathrm{rank}(\mathcal{C}) < n$** → 不可制御状態あり / Not all states controllable

---

## 👀 可観測性とは？ / What is Observability?

**定義 / Definition**  
出力 $y(t)$ の履歴から、**内部状態 $x(t)$ を一意に推定できる**性質。  
The property that the entire state vector $x(t)$ can be uniquely determined from the history of $y(t)$.

**Kalman 可観測性行列 / Observability Matrix**  

$$
\mathcal{O} =
\begin{bmatrix}
C \\
CA \\
CA^2 \\
\vdots \\
CA^{n-1}
\end{bmatrix}
$$

- **$\mathrm{rank}(\mathcal{O}) = n$** → 完全可観測 / Fully observable  
- **$\mathrm{rank}(\mathcal{O}) < n$** → 不可観測状態あり / Not all states observable

---

## 📘 例題システム / Example System

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
\end{bmatrix}
$$

- **可制御性あり？** / Is it controllable?  
- **可観測性あり？** / Is it observable?

---

## 🧪 Pythonによる検査 / Testing in Python (`control` library)

```python
import numpy as np
import control

A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])

# 可制御性
Ctrb = control.ctrb(A, B)
print("Controllability Matrix:")
print(Ctrb)
print("Rank:", np.linalg.matrix_rank(Ctrb))

# 可観測性
Obsv = control.obsv(A, C)
print("Observability Matrix:")
print(Obsv)
print("Rank:", np.linalg.matrix_rank(Obsv))
```

---

## 💡 工学的意味 / Engineering Implications

| 日本語 / Japanese | English |
|-------------------|---------|
| **可制御でない** → 操作できない状態が存在（極配置不可） | **Not controllable** → Some states cannot be influenced (pole placement impossible) |
| **可観測でない** → 推定できない状態が存在（オブザーバ不可） | **Not observable** → Some states cannot be estimated (observer design impossible) |

---

## 🧠 実務上の注意点 / Practical Notes

- 数値誤差でランクが落ちる場合あり → **特異値分解（SVD）やしきい値**で評価  
  Numerical errors may cause rank reduction → Use **SVD or tolerance thresholds**
- 設計では**可制御かつ可観測**な系を前提にすることが多い  
  Design usually assumes **both controllable and observable**
- 実システムではセンサ配置と密接に関連  
  Closely related to sensor placement in real systems

---

## 📚 参考資料 / References

- 「現代制御理論入門」森北出版  
- *Modern Control Engineering* – K. Ogata  
- Python: `control.ctrb()`, `control.obsv()`, `numpy.linalg.matrix_rank()`

---

**⬅️ [前節 / Previous Section](/part02_modern/theory/01_state_space.html)**  
状態空間表現の基礎を解説します。  
Covers the basics of state-space representation.

**➡️ [次節 / Next Section](/part02_modern/theory/03_state_feedback.html)**  
状態フィードバックと極配置を解説します。  
Covers state feedback and pole placement.

**📚 [この章のREADMEへ / Back to Part 2 README](/part02_modern/theory/)**  
現代制御理論の全体構成と教材一覧に戻ります。  
Return to the full Part 2 structure and materials list.
