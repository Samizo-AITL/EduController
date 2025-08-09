---
layout: default
title: 04. オブザーバ設計と状態推定 / Observer Design & State Estimation
permalink: /part02_modern/theory/04_observer_design.html
---

---

# 👁️ 04. オブザーバ設計と状態推定 / Observer Design & State Estimation

---

**状態フィードバック制御**を行うには、すべての状態 $x(t)$ を把握する必要があります。  
しかし、実システムでは**一部の状態しか直接測定できない**場合が多くあります。  
そこで、**出力 $y(t)$ から状態 $x(t)$ を推定**する仕組みが「**オブザーバ（Observer）**」です。

To apply **state feedback control**, all states $x(t)$ must be known.  
In real systems, only part of the state may be directly measured.  
Thus, an **observer** estimates $x(t)$ from the output $y(t)$.

---

## 🎯 学習目標 / Learning Goals

| 日本語 / Japanese | English |
|-------------------|---------|
| オブザーバ（状態推定器）の構造を理解 | Understand observer structure |
| フルオーダーオブザーバの設計式を説明 | Explain full-order observer design |
| 極配置により推定誤差収束を設計 | Design estimation error convergence via pole placement |
| Pythonでオブザーバを設計・検証 | Design & verify observers in Python |

---

## 👁️ オブザーバの基本構造 / Basic Structure

オブザーバ（推定器）の状態方程式：  

$$
\dot{\hat{x}} = A \hat{x} + B u + L(y - \hat{y}), \quad \hat{y} = C \hat{x}
$$

| 項目 | 意味 / Meaning |
|------|---------------|
| $\hat{x}$ | 推定状態ベクトル / Estimated state vector |
| $L$ | オブザーバゲイン / Observer gain |
| $y - \hat{y}$ | 出力誤差（推定誤差）/ Output estimation error |

---

### ✅ 誤差系のダイナミクス / Error Dynamics

推定誤差 $e = x - \hat{x}$ とすると： 

$$
\dot{e} = (A - LC)e
$$

- **$A - LC$ の固有値配置**で、推定誤差の収束特性を決定  
- Designing the eigenvalues of **$A - LC$** controls error convergence

---

## 📘 設計例 / Design Example

対象システム / Target system:  

$$
A = \begin{bmatrix} 0 & 1 \\\\ -2 & -3 \end{bmatrix}, \quad
B = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}, \quad
C = \begin{bmatrix} 1 & 0 \end{bmatrix}
$$

目標極 / Desired poles: $s = -5$, $s = -6$

---

## 🧪 Pythonによるオブザーバ設計 / Observer Design in Python

```python
import numpy as np
import control

A = np.array([[0, 1], [-2, -3]])
C = np.array([[1, 0]])

# 目標極 / Desired poles
observer_poles = [-5, -6]

# オブザーバゲイン L 計算 / Compute observer gain L
L = control.place(A.T, C.T, observer_poles).T
print("Observer Gain L:")
print(L)
```

---

## 🔄 オブザーバ＋制御器の統合構造 / Combined Structure

**状態フィードバック**が推定値 $\hat{x}(t)$ を使用する場合：  

$$
u(t) = -K \hat{x}(t) + r(t)
$$

- 実際に使用するのは推定状態 $\hat{x}$  
- 推定精度が制御性能に直結

```
      +----------+     +----------+
r ───►│  -Kx̂ + r │     │ Observer │
      └────┬─────┘     └────┬────┘
           │               │
           ▼               ▼
         [Plant] ◄─────── y = Cx
```

---

## ⚠️ 設計のポイント / Design Notes

| 日本語 / Japanese | English |
|-------------------|---------|
| $A - LC$ の極は制御系より左側（高速収束）に配置 | Place $A - LC$ poles further left for faster convergence |
| 制御の2～5倍の速さが目安 | 2–5× faster than control loop |
| 可観測性がないと設計不可 | Not possible if system is not observable |
| `control.obsv(A, C)` で検査可能 | Check with `control.obsv(A, C)` |

---

## 📚 参考資料 / References

- 「現代制御理論入門」森北出版  
- *Modern Control Engineering* – K. Ogata  
- Python: `control.place()`, `control.obsv()`, `numpy.linalg`

---

**⬅️ [前節 / Previous Section](https://samizo-aitl.github.io/EduController/part02_modern/theory/03_state_feedback.html)**  
状態フィードバックと極配置の理論を解説します。  
Covers state feedback and pole placement theory.

**📚 [この章のREADMEへ / Back to Part 2 README](https://samizo-aitl.github.io/EduController/part02_modern/)**  
現代制御理論の全体構成と教材一覧に戻ります。  
Return to the full Part 2 structure and materials list.
