---
layout: default
title: 03. 動的モード分解（DMD）
permalink: /part08_data_driven/theory/03_dmd.html
---

---

# 🔍 03. 動的モード分解（DMD: Dynamic Mode Decomposition）

> 💡 **Note:** 数式や図が正しく表示されない場合は、[GitHub版はこちら](https://github.com/Samizo-AITL/EduController/blob/main/part08_data_driven/theory/03_dmd.md) をご覧ください。

---

本節では、観測データに基づいて力学系の振る舞いを抽出する手法である  
**動的モード分解（DMD）** について解説します。これは**Koopman理論の特別なケース**としても位置づけられます。  
This section explains **Dynamic Mode Decomposition (DMD)**, a method for extracting system dynamics directly from observation data, considered a **special case of Koopman theory**.

---

## 🎯 DMDの概要 / Overview

- 非線形・未知の力学系に対して、**観測データから線形近似モデルを構築**  
  For nonlinear or unknown systems, construct a **linear approximation model from observation data**  
- 多自由度システムや時系列信号の「モード成分」を抽出可能  
  Extract **modal components** of multi-DOF systems or time-series signals  
- モデル構築不要で、**データ駆動型の予測・解析**が可能  
  Enables **data-driven prediction and analysis** without explicit modeling

---

## 🧠 数理モデル / Mathematical Formulation

観測系列 $\{x_1, x_2, \dots, x_m\}$ を以下のように構成：  
Given a time series $\{x_1, x_2, \dots, x_m\}$, form:

$$
X = [x_1, x_2, \dots, x_{m-1}], \quad X' = [x_2, x_3, \dots, x_m]
$$

DMDの目標は、$X'$ を $X$ によって最もよく近似する線形写像 $A$ を求めること：  
The goal of DMD is to find a linear map $A$ such that:

$$
X' \approx A X
$$

この $A$ の固有分解（またはSVD）によって、**動的モード** を抽出します。  
The eigen-decomposition (or SVD) of $A$ yields the **dynamic modes**.

---

## 📐 DMDの計算ステップ / Computational Steps

1. 入力データ系列を $X$, $X'$ に分解  
   Split the data sequence into $X$ and $X'$  
2. SVD分解：  
   Perform SVD:
   $$
   X = U \Sigma V^T
   $$
3. 低次元DMD行列：  
   Reduced DMD matrix:
   $$
   \tilde{A} = U^T X' V \Sigma^{-1}
   $$
4. 固有値・固有ベクトルを解析して、**モード・成長率・振動数**を抽出  
   Analyze eigenvalues and eigenvectors to extract **modes, growth rates, and frequencies**

---

## 📊 応用例 / Applications

- 流体シミュレーションのモード解析  
  Modal analysis in fluid simulations  
- 建物振動の状態推定  
  Structural vibration state estimation  
- 複雑システムの次元削減と予測  
  Dimensionality reduction and prediction of complex systems

---

## 🛠️ 本教材での実装 / Implementations in This Chapter

- **Pythonスクリプト / Python Script**:  
  [`dmd_analysis.py`](https://samizo-aitl.github.io/EduController/part08_data_driven/simulation/dmd_analysis.py)  
- **可視化Notebook / Visualization Notebook**:  
  [`koopman_vs_dmd_visual.ipynb`](https://samizo-aitl.github.io/EduController/part08_data_driven/notebooks/koopman_vs_dmd_visual.ipynb)

---

## 💡 DMDとKoopmanの関係 / Relation to Koopman Theory

| 観点 / Aspect | DMD | Koopman |
|--------------|-----|---------|
| アプローチ / Approach | データから近似線形写像 | 関数空間の線形作用素 |
| 必要データ / Required Data | 状態系列 $x_t$ | 状態・入力・出力などの関数空間 |
| 制御との統合 / Control Integration | 制限的（予測用） | 制御設計が可能（線形系に変換） |

---

## 🔚 まとめ / Summary

DMDは、「モデルレスで予測可能な線形系」を観測から得る代表的な手法です。  
DMD is a representative **model-free method** for obtaining a **predictable linear system** from observations.  

次節では、より制御指向なモデル構築手法である**サブスペース同定法**を学びます。  
In the next section, we will study **subspace identification**, a more control-oriented modeling approach.

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/02_koopman_operator.html)**  
Koopman演算子とその線形化手法を解説します。  
Covers the Koopman operator and its linearization approach.

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/04_subspace_id.html)**  
サブスペース同定法の理論と実装を説明します。  
Covers the theory and implementation of subspace identification.

**🏠 [Part 08 トップ / Back to Part 08 Top](https://samizo-aitl.github.io/EduController/part08_data_driven/)**
