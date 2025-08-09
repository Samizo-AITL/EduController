---
layout: default
title: 04. サブスペース同定法（Subspace Identification）
permalink: /part08_data_driven/theory/04_subspace_id.html
---

---

# 📘 04. サブスペース同定法（Subspace Identification）

> 💡 **Note:** 数式が正しく表示されない場合は、[GitHub版はこちら](https://github.com/Samizo-AITL/EduController/blob/main/part08_data_driven/theory/04_subspace_id.md) をご覧ください。

---

本節では、**入力–出力データに基づいて状態空間モデルを推定**する手法、  
サブスペース同定法（Subspace Identification）について解説します。  
This section explains **subspace identification**, a method to estimate state-space models directly from **input–output data**.

---

## 🎯 サブスペース同定とは？ / What is Subspace Identification?

- 入力–出力時系列から状態空間モデル $A, B, C, D$ を直接構築  
  Directly constructs state-space models $A, B, C, D$ from input–output time series  
- ノイズに強く、SVD（特異値分解）を用いた安定な推定が可能  
  Robust to noise, uses Singular Value Decomposition (SVD) for stable estimation  
- 多変数系（MIMO）やブラックボックス系にも有効  
  Effective for multi-variable (MIMO) and black-box systems

---

## 🧠 数学的背景（簡略） / Mathematical Background (Simplified)

状態空間モデル / State-space model:

$$
\begin{aligned}
x_{k+1} &= A x_k + B u_k \\
y_k &= C x_k + D u_k
\end{aligned}
$$

入力 $u_k$、出力 $y_k$ の系列から、**回帰行列やハンケル行列**を構成し、  
SVD を通じて内部状態の次元とモデル行列を抽出します。  
From sequences of $u_k$ and $y_k$, construct **regression or Hankel matrices**,  
then extract system order and model matrices via SVD.

---

## 🔧 主なステップ（N4SIDアルゴリズム例） / Main Steps (N4SID Example)

1. データ系列 $\{u_k, y_k\}$ を収集  
   Collect data sequences $\{u_k, y_k\}$  
2. ハンケル行列（時系列の履歴）を構成  
   Construct Hankel matrices (history of time series)  
3. SVDにより系の次数（状態次元）を推定  
   Estimate system order (state dimension) via SVD  
4. 観測行列・状態遷移行列 $A, B, C, D$ を推定  
   Estimate observation and state-transition matrices $A, B, C, D$  
5. 得られたモデルの予測精度や再現性を検証  
   Validate prediction accuracy and reproducibility

---

## 📈 特徴と利点 / Features and Advantages

| 項目 / Item | 内容 / Description |
|-------------|--------------------|
| 必要データ / Required Data | 入力–出力系列 / Input–output sequences |
| ノイズ耐性 / Noise Robustness | 高い（SVDにより安定） / High (stable via SVD) |
| 系の次数選定 / Order Selection | 自動・半自動で可能 / Automatic or semi-automatic |
| 拡張性 / Extensibility | MIMO, 時不変・時変系にも対応 / Supports MIMO, LTI & LTV systems |

---

## 🧪 本教材での実装例 / Implementations in This Chapter

- **Pythonスクリプト / Python Script**:  
  [`subspace_identification.py`](https://samizo-aitl.github.io/EduController/part08_data_driven/simulation/subspace_identification.py)

> 実験では、Python + NumPy + SciPy により小規模系の識別を行います。  
> Experiments identify small-scale systems using Python + NumPy + SciPy.

---

## 💡 備考 / Notes

- MATLABの `n4sid()` 関数で広く利用される  
  Widely available as `n4sid()` in MATLAB  
- Pythonでは `pyN4SID` や `control.matlab` 相当の実装が必要  
  Requires equivalents like `pyN4SID` or `control.matlab` in Python  
- KoopmanやDMDと異なり、**状態ベースの再構築が主目的**  
  Unlike Koopman or DMD, the main goal is **state-based reconstruction**

---

## 🔚 まとめ / Summary

サブスペース同定法は、**モデルベース制御への橋渡し**として有効な識別法です。  
Subspace identification is an effective method for **bridging to model-based control**.

次節では、こうしたデータ駆動手法と従来モデルの統合について考察します。  
In the next section, we discuss integrating these data-driven methods with traditional models.

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/03_dmd.html)**  
動的モード分解（DMD）の理論と応用を解説します。  
Covers the theory and applications of Dynamic Mode Decomposition (DMD).

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/05_data_vs_model.html)**  
データ駆動とモデルベース制御の統合戦略を説明します。  
Explains integration strategies for data-driven and model-based control.

**🏠 [Part 08 トップ / Back to Part 08 Top](https://samizo-aitl.github.io/EduController/part08_data_driven/)**
