---
layout: clean
title: 🛡️ 安定余裕とロバスト性の評価 / Stability Margins & Robustness Evaluation
permalink: /part01_classical/theory/05_stability_margins.html
---

---

# 🛡️ 05. 安定余裕とロバスト性の評価  
**05. Stability Margins & Robustness Evaluation**

> **Note:** 数式が正しく表示されない場合は [GitHub版](https://github.com/Samizo-AITL/EduController/blob/main/part01_classical/theory/05_stability_margins.md) を参照してください。

---

現実の制御系は、モデル誤差・外乱・遅延などによる不確かさを常に抱えています。安定性を保証しつつ、こうした変動に耐える性能 ― それが「ロバスト性」です。本節では、**ゲイン余裕（Gain Margin）**・**位相余裕（Phase Margin）** による定量評価法と、その設計指針を学びます。  
Real-world control systems always face uncertainties such as modeling errors, disturbances, and delays. Ensuring stability under such variations is called **robustness**. This section covers quantitative evaluation using **gain margin (GM)** and **phase margin (PM)**, and related design guidelines.

---

## 🎯 本節の学習目標｜Learning Objectives

- 安定余裕（GM・PM）の定義と算出法を理解する  
  Understand the definition and calculation of GM and PM  
- 安定余裕が実システムに与える意味を把握する  
  Understand the practical significance of stability margins  
- ロバスト性と安定余裕の関係性を説明できる  
  Explain the relationship between robustness and stability margins  
- 仕様に基づいた設計改善の方向性を見出せる  
  Identify design improvement strategies based on specifications

---

## ⚖️ 安定余裕とは？｜What are Stability Margins?

### ✅ 位相余裕 / Phase Margin (PM)

ゲイン交差周波数 $\omega_g$ における位相の余裕：  
Phase margin at gain crossover frequency $\omega_g$:

$$
\text{PM} = 180^\circ + \angle G(j\omega_g)
$$

---

### ✅ ゲイン余裕 / Gain Margin (GM)

位相交差周波数 $\omega_p$ におけるゲインの余裕：  
Gain margin at phase crossover frequency $\omega_p$:

$$
\text{GM} = \frac{1}{|G(j\omega_p)|} 
\quad \text{or} \quad 
-20 \log_{10} |G(j\omega_p)| \; [\mathrm{dB}]
$$

---

## 🧠 なぜ必要か？｜Why Do We Need Them?

- **モデルのズレや外乱**があっても安定を保つため  
  Maintain stability despite model mismatches or disturbances  
- 位相の予期せぬ回転やゲインの増減が不安定化を招く  
  Unexpected phase shifts or gain changes can destabilize the system  
- **十分な余裕があるとノイズやパラメータ変動に強い**  
  Adequate margins improve tolerance to noise and parameter variations

---

## 🎛️ 設計目安と実務値｜Design Guidelines

| 指標 / Metric | 安定の目安 / Stability Criterion | 備考 / Notes |
|---------------|----------------------------------|--------------|
| PM            | $> 30^\circ$                     | 45～60°が望ましい場合も / 45–60° often preferred |
| GM            | $> 6$ dB                         | 10～20 dBが好まれる場合も / 10–20 dB often preferred |

---

## 🧪 周波数応答からの読み取り｜Reading from Frequency Response

### 手順（ボード線図）｜Procedure (Bode Plot)

1. ゲインプロットが 0 dB になる点 $\omega_g$ を見つける  
   Find $\omega_g$ where gain = 0 dB  
2. その周波数における位相から PM を計算  
   Compute PM at that frequency  
3. 位相が $-180^\circ$ になる点 $\omega_p$ を見つける  
   Find $\omega_p$ where phase = $-180^\circ$  
4. その周波数におけるゲインから GM を計算  
   Compute GM at that frequency  

---

### Python例｜Python Example

```python
import control
from control.freqplot import margin

# Example: Second-order system
G = control.tf([1], [1, 2, 1])
gm, pm, wg, wp = margin(G)
print(f"Gain Margin: {gm}, Phase Margin: {pm}")
```

---

## 🔍 ロバスト性との関係｜Relation to Robustness

### ✅ ロバスト性とは？ / What is Robustness?
- 不確かさや変動に対する安定性・性能維持の能力  
  Ability to maintain stability and performance under uncertainties  
- モデル誤差、パラメータ変動、外乱などへの耐性  
  Tolerance to modeling errors, parameter variations, and disturbances

---

### 安定余裕がロバスト性を担保する理由  
**Why Stability Margins Ensure Robustness**
- 大きな PM/GM → 安定の「バッファ」あり  
  Large PM/GM = stability "buffer"  
- ノイズ・遅延・位相ずれがあっても発散しにくい  
  Less prone to divergence under noise, delay, or phase shift

---

## 💡 設計改善のヒント｜Design Improvement Tips

- PM が小さい → 位相補償器（リード補償）を追加  
  Low PM → add phase lead compensation  
- GM が小さい → ゲインを抑える or フィルタ追加  
  Low GM → reduce gain or add filter  
- 両者が小さい → 制御器の構造見直し（PI → PID など）  
  Both small → reconsider controller structure (e.g., PI → PID)

---

## 📚 参考資料｜References
- 森北出版「制御工学」  
- Franklin et al., *Feedback Control of Dynamic Systems*  
- Python: `control.margin`, `bode_plot`

---

**⬅️ [前節 / Previous Section](https://samizo-aitl.github.io/EduController/part01_classical/theory/04_frequency_response.html)**  
周波数応答とボード線図の基礎を学びます。  
Covers basics of frequency response and Bode plots.

**📚 [この章のREADMEへ / Back to Part 1 README](https://samizo-aitl.github.io/EduController/part01_classical/)**  
古典制御理論の全体構成と教材一覧に戻ります。  
Return to the full Part 1 structure and materials list.
