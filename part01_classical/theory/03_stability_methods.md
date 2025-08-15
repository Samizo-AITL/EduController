---
layout: clean
title: 🧮 安定性判別法 / Stability Determination Methods
permalink: /part01_classical/theory/03_stability_methods.html
---

---

# 🧮 03. 安定性判別法（Routh, 根軌跡, ナイキスト）  
**03. Stability Determination Methods (Routh, Root Locus, Nyquist)**

> **Note:** 数式が正しく表示されない場合は [GitHub版](https://github.com/Samizo-AITL/EduController/blob/main/part01_classical/theory/03_stability_methods.md) を参照してください。

---

制御系の最も基本的な要件は **「安定であること」** です。本節では、古典制御理論における安定性の定義と、主要な判別法である **Routh-Hurwitz判別法**, **根軌跡法（Root Locus）**, **ナイキスト法（Nyquist）** を学びます。  
The most fundamental requirement of a control system is **stability**. This section explains the definition of stability in classical control theory and the major determination methods: **Routh-Hurwitz criterion**, **Root Locus**, and **Nyquist method**.

---

## 🎯 本節の学習目標｜Learning Objectives

- 安定性の定義と必要条件を理解する  
  Understand the definition and conditions for stability  
- Routh表による安定性判別を手計算できる  
  Perform stability check using Routh table manually  
- 根軌跡法による安定判定と極配置を理解する  
  Understand stability check and pole placement via Root Locus  
- ナイキスト線図による周波数領域の安定性評価を習得する  
  Learn frequency-domain stability check using Nyquist plot

---

## 📌 安定性の定義｜Definition of Stability

制御系が安定であるとは、**すべての閉ループ極が左半平面にある**ことを意味します。  
A control system is stable if **all closed-loop poles lie in the left-half complex plane**.

- **連続系 / Continuous-time**: All poles have negative real parts  
- **離散系 / Discrete-time**: All poles lie inside the unit circle  

---

## 🔢 Routh-Hurwitz判別法｜Routh-Hurwitz Criterion

**伝達関数 / Transfer Function:**

$$
G(s) = \frac{N(s)}{D(s)} = \frac{b_ms^m + \cdots + b_0}{a_ns^n + \cdots + a_0}
$$

安定性は $D(s)$ の根（極）に依存します。  
Stability depends on the roots (poles) of $D(s)$.

**手順（例：4次系） / Procedure (Example: 4th order):**
1. 係数を使って1列目を作成 / Fill first column using coefficients  
2. 補間計算で表を構成 / Build table with interpolation calculations  
3. 1列目の符号変化回数 = 不安定極の数 / Number of sign changes = number of unstable poles  

✅ **すべて正 → 安定 / All positive → Stable**

---

## 📈 根軌跡法｜Root Locus Method

**開ループ伝達関数 / Open-loop transfer function:**

$$
G(s)H(s) = \frac{K \cdot N(s)}{D(s)}
$$

- ゲイン $K$ を変化させたときの**閉ループ極の軌跡**を描く  
  Plots **locus of closed-loop poles** as $K$ varies  
- 安定領域、減衰比、応答速度の変化を視覚的に把握可能  
  Visualizes stability region, damping ratio, and speed changes

---

## 🌀 ナイキスト判別法｜Nyquist Stability Criterion

**周波数応答を用いた安定性評価**  
Evaluates stability using frequency response.

- Nyquist線図が $-1+j0$ を囲む回数・方向を確認  
  Check how many times and in which direction Nyquist plot encircles $-1+j0$  

**判別ルール / Rule:**

$$
N = Z - P
$$

- $P$: 右半平面にある開ループ極の数 / # of open-loop poles in RHP  
- $Z$: 右半平面にある閉ループ極の数 / # of closed-loop poles in RHP  
- $N$: $-1$ 点を囲んだ回数（反時計回りを正） / Encirclements of $-1$ (CCW positive)  

✅ **$Z = 0$ → 安定 / Stable if $Z=0$**

---

## 🛠️ 各手法の比較｜Comparison

| 判別法 / Method | 利点 / Advantages | 注意点 / Limitations |
|----------------|-------------------|----------------------|
| Routh-Hurwitz  | 計算簡単・定量的 / Simple & quantitative | 高次で複雑化 / Complex for high-order |
| 根軌跡法       | 可視化容易 / Easy visualization | モデル依存 / Model-dependent |
| ナイキスト法   | 周波数応答ベース / Based on frequency response | 実測データ必要 / Requires measured data |

---

## 🧪 Python実装例｜Python Examples

- **Routh表**: `sympy` or custom Python function  
- **根軌跡法**: `control.root_locus()`  
- **ナイキスト線図**: `control.nyquist_plot()`  

📂 See: [`/simulation/stability_methods.py`](../simulation/stability_methods.py)

---

## 📚 参考資料｜References

- 森北出版「制御工学入門」  
- Franklin et al., *Feedback Control of Dynamic Systems*  
- Python: `control`, `sympy`, `matplotlib`

---

**⬅️ [前節 / Previous Section](https://samizo-aitl.github.io/EduController/part01_classical/theory/02_transient_response.html)**  
過渡応答と定常偏差の基礎を学びます。  
Covers fundamentals of transient response & steady-state error.

**➡️➡️ [次節 / Next Section](https://samizo-aitl.github.io/EduController/part01_classical/theory/04_frequency_response.html)**  
周波数応答とボード線図の解析手法を解説します。  
Explains frequency response and Bode plot analysis.

**📚 [この章のREADMEへ / Back to Part 1 README](https://samizo-aitl.github.io/EduController/part01_classical/)**  
古典制御理論の全体構成と教材一覧に戻ります。  
Return to the full Part 1 structure and materials list.
