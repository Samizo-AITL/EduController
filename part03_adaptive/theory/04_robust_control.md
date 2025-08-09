---
layout: default
title: 04. ロバスト制御 / Robust Control
permalink: /part03_adaptive/theory/04_robust_control.html
---

---

# 🛡️ 04. ロバスト制御 / Robust Control

> ℹ️ **数式が正しく表示されない場合はGitHub版をご確認ください**  
> If equations do not render properly, see the [GitHub version](https://github.com/Samizo-AITL/EduController/blob/main/part03_adaptive/theory/04_robust_control.md)

---

制御対象には**モデル誤差**や**外乱・ノイズ**が必ず存在します。  
こうした**不確かさに対して性能を保証する制御**が「ロバスト制御（Robust Control）」です。

Robust control ensures system performance even in the presence of uncertainties, disturbances, and noise.

---

## 🎯 学習目標 / Learning Goals

- **ロバスト制御の基本概念と必要性を理解する**  
  Understand the concept and necessity of robust control  
- **H∞制御の基本原理と数式構造を把握する**  
  Learn the principles and mathematical structure of H∞ control  
- **ゲイン余裕・位相余裕でのロバスト性評価を説明できる**  
  Explain robust stability via gain/phase margins  
- **μ解析など応用評価法を知る**  
  Get familiar with μ-analysis and advanced evaluation methods  

---

## ❓ なぜロバスト性が必要か？ / Why Robustness Matters

- **モデル化誤差 / Modeling errors**：実機とモデルは完全一致しない  
- **外乱・ノイズ / Disturbances & noise**：センサ雑音、遅延、環境変動  
- **パラメータばらつき / Parameter variations**：製品差、経年劣化  

ロバスト制御の目標は、**性能を保ちながら安定性を保証する**ことです。  
The goal is to **maintain performance while guaranteeing stability**.

---

## 📐 ロバスト性の定義 / Definition

- **内部安定性 (Internal Stability)**  
  全信号が有界入力で有界出力（BIBO）  
- **感度関数 $S(s)$**

$$
S(s) = \frac{1}{1 + G(s)K(s)}
$$

- **補償関数 $T(s)$**
    
$$
T(s) = \frac{G(s)K(s)}{1 + G(s)K(s)} = 1 - S(s)
$$

---

## 🎯 H∞制御の目的 / Objective of H∞ Control

最大ゲイン（無限ノルム）を**最小化**し、最悪誤差に備える  
Minimize the infinity norm to prepare for the worst-case error.

**目的関数 / Objective function**:

$$
\| T_{zw}(s) \|_\infty < \gamma
$$

- $T_{zw}(s)$：外乱 $w$ から性能出力 $z$ への伝達関数  
- $\| \cdot \|_\infty$：全周波数帯での最大ゲイン  

---

## 🧩 H∞制御と感度関数 / H∞ & Sensitivity

- $S(s)$ ↑ → 外乱に弱い  
- $T(s)$ ↑ → センサノイズに弱い  
- 周波数帯ごとに重視項目を決定  
  Decide trade-off per frequency band.

---

## 📈 ロバスト性評価指標 / Robustness Metrics

| 指標 / Metric | 内容 / Description | 目安 / Guideline | ロバスト性 / Robustness |
|---------------|--------------------|------------------|--------------------------|
| ゲイン余裕 GM  | 増幅許容量 / Gain tolerance | > 6 dB | ○ |
| 位相余裕 PM    | 遅延許容量 / Phase tolerance | > 30° | ○ |
| S/N ノルム     | $S(j\omega)$ ピーク値 | < 2.0 | ◎ |

---

## ⚙️ 実装ツール例 / Tools

| ツール / Tool | 機能例 / Features |
|---------------|-------------------|
| MATLAB Robust Control Toolbox | hinfsyn, musyn, robstab |
| Python slycot, robustcontrol  | H∞制御（制限あり） |
| Octave control.matlab.hinfsyn | 非公式対応 |

---

## 🧠 AITL-Hとの接続 / Connection to AITL-H

| AITL層 / Layer | 対応 / Role | 関係 / Relation |
|----------------|------------|-----------------|
| 理性 / Reason (PID/Model) | 直接制御 / Direct control | 設計時にH∞安定性保証 / Guarantee H∞ stability at design |
| 知性 / Intelligence (LLM) | 制約補完 / Constraint support | 状況に応じH∞制御へ切替 / Switch to H∞ control when needed |

---

## 📚 参考文献 / References

- Zhou & Doyle, *Essentials of Robust Control*  
- Skogestad & Postlethwaite, *Multivariable Feedback Control*  
- MATLAB Robust Control Toolbox Docs  
- Farshad Khorrami, *Robust Control Theory*  

---

**⬅️ 前節 / Previous:** [03. ゲインスケジューリング制御](https://samizo-aitl.github.io/EduController/part03_adaptive/theory/03_gain_scheduling.html)  
状態に応じたゲイン切替・補間の設計手法 / Gain switching & interpolation

**📚 第3章 README / Chapter Top:** [適応制御とロバスト制御](https://samizo-aitl.github.io/EduController/part03_adaptive/)  
第3章全体構成と教材一覧 / Overview & chapter contents
