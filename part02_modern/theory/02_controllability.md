# 🔍 02. 可制御性と可観測性の基礎

状態空間モデルを使って制御系を設計するためには、「その状態を操作できるか？」「状態を外部から観測できるか？」という2つの性質が極めて重要です。本節では、**可制御性（controllability）** と **可観測性（observability）** の定義・数学的検査法・物理的な意味を解説します。

---

## 🎯 学習目標

- 可制御性・可観測性の概念を理解する  
- Kalmanのランク条件による判別法を説明できる  
- Pythonでシステムの可制御性・可観測性を検査できる  
- 極配置設計やオブザーバ設計に向けた土台を築く

---

## ⚙️ 可制御性とは？

ある初期状態 $x(0)$ から、任意の状態 $x(t)$ に**有限時間内で到達できる**か？

### ✅ Kalman可制御性判定

可制御性行列：

$$
\mathcal{C} = \begin{bmatrix} B & AB & A^2B & \cdots & A^{n-1}B \end{bmatrix}
$$

- $\text{rank}(\mathcal{C}) = n$ → 完全可制御
- ランクが $< n$ → 一部状態に制御が届かない

---

## 👀 可観測性とは？

出力 $y(t)$ の履歴から、**内部状態 $x(t)$ を一意に推定できる**か？

### ✅ Kalman可観測性判定

可観測性行列：

$$
\mathcal{O} = \begin{bmatrix} C \\ CA \\ CA^2 \\ \vdots \\ CA^{n-1} \end{bmatrix}
$$

- $\text{rank}(\mathcal{O}) = n$ → 完全可観測
- ランクが $< n$ → 一部状態が出力に現れない

---

## 📘 例題システム

システム：

$$
A = \begin{bmatrix} 0 & 1 \\\\ -2 & -3 \end{bmatrix}, \quad
B = \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}, \quad
C = \begin{bmatrix} 1 & 0 \end{bmatrix}
$$

- 可制御性あり？可観測性あり？

---

## 🧪 Pythonによる検査（controlライブラリ）

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

## 💡 工学的な意味
- 可制御でない → 操作できない状態が存在（= 極配置できない）
- 可観測でない → 外部からわからない状態が存在（= オブザーバ不可）

---

## 🧠 実務上の注意点
- 数値誤差でランクが落ちることも → 特異値分解やしきい値で評価
- 制御系設計では、可制御かつ可観測 な系を前提とすることが多い
- 実システムでのセンサ設計と密接に関わる（観測可能性）

---

## 📚 参考資料
- 「現代制御理論入門」森北出版
- Ogata, Modern Control Engineering
- Python: control.ctrb(), control.obsv(), numpy.linalg.matrix_rank()

---
