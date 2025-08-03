# 👁️ 04. オブザーバ設計と状態推定

状態フィードバック制御を行うには、すべての状態 $x(t)$ を知る必要があります。  
しかし、実システムでは一部の状態しかセンサで取得できないことが多くあります。  
このようなとき、**出力 $y(t)$ から状態 $x(t)$ を推定**する仕組みが「**オブザーバ（Observer）**」です。

---

## 🎯 学習目標

- オブザーバ（状態推定器）の基本構造を理解する  
- フルオーダーオブザーバの設計式を説明できる  
- 極配置により推定誤差の収束を設計できる  
- Pythonでオブザーバを設計・検証できるようになる

---

## 👁️ オブザーバの基本構造

オブザーバ（推定器）の状態方程式：

$$
\dot{\hat{x}} = A \hat{x} + B u + L(y - \hat{y}) \\
\hat{y} = C \hat{x}
$$

- $\hat{x}$：推定状態ベクトル  
- $L$：オブザーバゲイン（補正項の強さ）  
- $y - \hat{y}$：出力誤差（＝推定誤差）

---

### ✅ 誤差系のダイナミクス

推定誤差 $e = x - \hat{x}$ とすると：

$$
\dot{e} = (A - LC)e
$$

したがって、**$A - LC$ の固有値を設計すれば、推定誤差の収束性が決まる**

---

## 📘 設計例

対象システム：

$$
A = \begin{bmatrix} 0 & 1 \\\\ -2 & -3 \end{bmatrix}, \quad
B = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}, \quad
C = \begin{bmatrix} 1 & 0 \end{bmatrix}
$$

目標：オブザーバの極を $s = -5$, $s = -6$ に配置

---

## 🧪 Pythonでのオブザーバ設計

```python
import numpy as np
import control

A = np.array([[0, 1], [-2, -3]])
C = np.array([[1, 0]])

# 目標極
observer_poles = [-5, -6]

# オブザーバゲイン L を計算
L = control.place(A.T, C.T, observer_poles).T
print("Observer Gain L:")
print(L)
```

---

## 🔄 オブザーバ＋制御器の統合構造

出力 $y(t)$ しか得られないとき：

$$
u(t) = -K \hat{x}(t) + r(t)
$$

- 実際に使うのは推定値 $\hat{x}$
- 推定精度が制御性能に直結
 
```
      +----------+     +----------+
r ───►│          │     │ Observer │
      │  -Kx̂ + r ├────►  A, B, C │
      └────┬─────┘     └────┬────┘
           │               │
           ▼               ▼
         [Plant] ◄─────── y = Cx
```

---

## ⚠️ 設計のポイント

- $A - LC$ の極は制御系よりも左側に速く収束するよう設計（例：制御の2～5倍速）
- 可観測性がないとオブザーバは設計できない（control.obsv(A, C) で検査）

---

## 📚 参考資料

- 「現代制御理論入門」森北出版
- Ogata, Modern Control Engineering
- Python: control.place(), control.obsv(), numpy.linalg

---


