---
layout: default
title: 3.1 適応制御の概要 / Introduction to Adaptive Control
permalink: /part03_adaptive/theory/01_adaptive_intro/
---

---

# 🔄 3.1 適応制御の概要 / Introduction to Adaptive Control

> ℹ️ **数式が正しく表示されない場合**は、[GitHub版はこちら](https://github.com/Samizo-AITL/EduController/blob/main/part03_adaptive/theory/01_adaptive_intro.md) をご参照ください。

---

制御対象が**時間とともに変化**したり、**事前に正確なモデルが得られない**場合、固定ゲインの制御器（PIDやLQRなど）では性能低下や不安定化が起こります。  
こうした状況に対応するのが **適応制御（Adaptive Control）** です。

When the plant characteristics **change over time** or an **accurate model is unavailable**, fixed-gain controllers (PID, LQR, etc.) may lose performance or become unstable.  
**Adaptive control** addresses this challenge.

---

## 🎯 **学習目標 / Learning Objectives**

| 🎯 **目標 / Objective** | 📖 **説明 / Description** |
|------------------------|---------------------------|
| **適応制御の定義を理解する**<br>Understand the definition of adaptive control | 制御対象や外乱の変動に応じて制御器パラメータを動的に調整する手法<br>Method that dynamically adjusts controller parameters based on plant or disturbance variations |
| **必要性を説明できる**<br>Explain its necessity | モデル誤差やパラメータ変化に対応し安定性と性能を維持<br>Maintains stability and performance under model errors or parameter changes |
| **代表的な適応戦略を把握する**<br>Understand major strategies | MRAC, L1適応制御, ゲインスケジューリング<br>MRAC, L1 adaptive control, gain scheduling |
| **AITL-H理性層との接続を理解する**<br>Understand AITL-H connection | 理性層制御性能を動的に最適化する仕組み<br>Mechanism to dynamically optimize rational-layer control performance |

---

## ❓ **なぜ適応制御が必要か / Why is Adaptive Control Needed?**

### ✅ **制御対象の変化への対応 / Handling Plant Changes**
- 飛行機の重量が燃料消費で変化  
- モータ加熱によるトルク特性変化  
- 作業物の質量や摩擦が作業ごとに異なる  

パラメータが時間的に変動する場合、**制御器のパラメータをリアルタイムに更新**する必要があります。

When parameters vary over time, **controller parameters must be updated in real time**.

---

## 🧩 **基本構造 / Basic Structure**

```text
  +----------------+
  | 適応律 (Updater)| ← パラメータ推定 / Parameter estimation
  +----------------+
            ↓
  +----------------+
  | 制御器 (Controller) |
  +----------------+
            ↓
       [ Plant ]
            ↑
          y(t)
```

- 適応律が制御器パラメータを計算・更新  
- 更新された制御器が制御入力を生成

The **adaptive law** computes and updates controller parameters, which the updated controller then uses to generate the control input.

---

## 📘 **代表的な適応制御の分類 / Major Types of Adaptive Control**

| **方式 / Method** | **概要 / Overview** | **利点 / Advantage** | **課題 / Challenge** |
|--------------------|---------------------|----------------------|----------------------|
| **MRAC**<br>(Model Reference Adaptive Control) | 基準モデル $M(s)$ に出力を一致させる | 理論体系が確立 | 設計が複雑 |
| **L1適応制御**<br>(L1 Adaptive Control) | 高速かつ安定な適応、分離原理適用可能 | 安定性保証と設計容易性 | パラメータ設定が多く調整が必要 |
| **ゲインスケジューリング**<br>(Gain Scheduling) | 状態変数に応じゲイン切替 | 実装が容易 | 切替時に不連続性が生じる可能性 |

---

## 📐 **MRACのイメージ / MRAC Concept**

- 基準モデル $M(s)$ を用意し、出力 $y(t)$ を $y_m(t)$ に一致させる  
- 誤差 $e(t) = y(t) - y_m(t)$ に基づきパラメータ更新  
- MITルールやLyapunov法で安定性を保証  

Prepare a reference model $M(s)$ and make $y(t)$ follow $y_m(t)$.  
Update parameters based on error $e(t)$, using MIT rule or Lyapunov methods for stability.

---

## 🧠 **AITL-Hとの関係 / Relation to AITL-H**

| **AITL層 / Layer** | **制御手法 / Method** | **適応制御の役割 / Role in Adaptive Control** |
|--------------------|-----------------------|-----------------------------------------------|
| 本能層 (FSM) | 状態遷移制御 | 状況認識で適応制御モードを切替 |
| 理性層 (PID/モデル制御) | 汎用物理制御 | 適応律がパラメータを動的に最適化 |
| 知性層 (LLM) | 推論・戦略 | 適応戦略選択やモデル切替を支援 |

---

## 📚 **参考文献 / References**

- Ioannou & Sun, *Robust Adaptive Control*  
- Åström & Wittenmark, *Adaptive Control*  
- Ogata, *Modern Control Engineering*  
- N. Hovakimyan, *L1 Adaptive Control Theory*

---

**⬅️ [前節 / Previous Section](https://samizo-aitl.github.io/EduController/part02_modern/)**  
現代制御理論の基礎、状態空間モデル、可制御性・可観測性を解説。  
Covers basics of modern control theory, state-space models, controllability, observability.

**[次節 / Next Section ➡️➡️](https://samizo-aitl.github.io/EduController/part03_adaptive/theory/02_mrac_design/)**  
MRAC（モデル参照適応制御）の設計方法を学ぶ。  
Learn how to design Model Reference Adaptive Control.

**🏠 [Part 03 トップ / Back to Part 03 Top](https://samizo-aitl.github.io/EduController/part03_adaptive/)**
