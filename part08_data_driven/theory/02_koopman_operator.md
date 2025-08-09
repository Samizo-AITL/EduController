---
layout: default
title: 02. Koopman演算子と線形化
permalink: /part08_data_driven/theory/02_koopman_operator.html
---

---

# 📈 02. Koopman演算子と線形化 / Koopman Operator & Linearization

> 💡 **Note:** 数式や図が正しく表示されない場合は、[GitHub版はこちら](https://github.com/Samizo-AITL/EduController/blob/main/part08_data_driven/theory/02_koopman_operator.md) をご覧ください。

---

本節では、非線形力学系を**高次元空間上で線形系として扱う**という発想に基づく  
**Koopman演算子理論**と、その制御応用について解説します。  
This section introduces the **Koopman operator theory**, which enables treating nonlinear dynamical systems as **linear systems in higher-dimensional spaces**, and discusses its control applications.

---

## 📚 背景：非線形系の困難さ / Background: The Challenge of Nonlinear Systems

多くの実システムは非線形であり、伝統的な線形制御手法では扱いにくいです。  
Most real-world systems are nonlinear, making them difficult to handle with traditional linear control methods.  

Koopman理論は、非線形系を**関数空間上の線形作用素**として捉えることで、  
**非線形 → 線形制御**への橋渡しを行います。  
Koopman theory interprets nonlinear systems as **linear operators on function spaces**, bridging **nonlinear dynamics to linear control**.

---

## 🧠 基本アイデア / Core Concept

- **元の力学系 / Original System**:
  $$x_{t+1} = f(x_t)$$

- **観測関数 / Observable Function** $\psi(x)$ を定義し、  
  Define an observable function $\psi(x)$, and let the Koopman operator $\mathcal{K}$ satisfy:
  $$\psi(x_{t+1}) = \mathcal{K} \, \psi(x_t)$$

つまり、**非線形な状態遷移 $f$ を、$\psi$ を介して線形作用素 $\mathcal{K}$ で記述**します。  
In other words, **nonlinear state transitions $f$ can be represented linearly** via $\psi$.

---

## 🛠️ 制御応用の流れ（Koopman制御） / Control Workflow

1. 系の観測データ $(x_t, x_{t+1})$ を多数取得  
   Collect system observation data $(x_t, x_{t+1})$  
2. 観測関数 $\psi(x)$ を適用し、線形近似 $\mathcal{K}$ を構築（線形回帰など）  
   Apply $\psi(x)$ and estimate a linear approximation $\mathcal{K}$ (e.g., linear regression)  
3. 得られた線形系上で LQR や MPC を設計  
   Design LQR or MPC on the resulting linear system  
4. 元の状態空間に逆変換して制御入力を適用  
   Transform back to the original state space and apply control inputs

---

## 📈 Koopman制御の数式モデル（例） / Example Mathematical Model

1. **状態変換 / State Transformation**:  
   $$z_t = \psi(x_t)$$
2. **線形モデル / Linear Model**:  
   $$z_{t+1} = A z_t + B u_t$$
3. **出力変換 / Output Transformation**:  
   $$x_t = C z_t$$

---

## 📎 応用のポイント / Practical Considerations

- $\psi(x)$ の選び方が極めて重要（多項式、RBF、Autoencoder等）  
  Choosing $\psi(x)$ is critical (polynomials, RBF, autoencoders, etc.)  
- 非線形系をグローバルに線形化する試み  
  Attempts to globally linearize nonlinear systems  
- 動的モード分解（DMD）はKoopmanの特別なケース  
  Dynamic Mode Decomposition (DMD) is a special case of Koopman theory

---

## 🧪 本教材での実装 / Implementations in This Chapter

- **Pythonスクリプト / Python Script**:  
  [`koopman_linearization.py`](https://samizo-aitl.github.io/EduController/part08_data_driven/simulation/koopman_linearization.py)  
- **可視化Notebook / Visualization Notebook**:  
  [`koopman_vs_dmd_visual.ipynb`](https://samizo-aitl.github.io/EduController/part08_data_driven/notebooks/koopman_vs_dmd_visual.ipynb)

> ⚠️ Koopman行列 $A, B, C$ の推定は、回帰やSVDなどを用いて行われます。  
> Estimation of Koopman matrices $A, B, C$ often uses regression or SVD.

---

## 🔚 まとめ / Summary

Koopman理論は、**非線形 → 線形制御**の橋渡しを行う革新的な枠組みです。  
Koopman theory is an innovative framework for bridging **nonlinear dynamics to linear control**.  

次節では、この理論の出発点とも言える**動的モード分解（DMD）**を詳しく見ていきます。  
In the next section, we will explore **Dynamic Mode Decomposition (DMD)**, a special case of Koopman theory.

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/01_model_free_control.html)**  
モデルフリー制御の基本概念を解説します。  
Covers the basics of model-free control.

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/03_dmd.html)**  
動的モード分解（DMD）の理論と実装を説明します。  
Covers the theory and implementation of DMD.

**🏠 [Part 08 トップ / Back to Part 08 Top](https://samizo-aitl.github.io/EduController/part08_data_driven/)**
