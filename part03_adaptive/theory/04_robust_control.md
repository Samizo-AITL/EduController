---
layout: default
title: 04. ロバスト制御（Robust Control）
---

<!-- MathJax support for both inline and block math -->
<script type="text/javascript">
  window.MathJax = {
    tex: { inlineMath: [['$', '$'], ['\\(', '\\)']] },
    svg: { fontCache: 'global' }
  };
</script>
<script type="text/javascript"
  async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

# 🛡️ 04. ロバスト制御（Robust Control）

制御対象には、**モデル誤差**や**外乱・ノイズ**が必ず存在します。  
こうした**不確かさに対して性能を保証する制御**が「ロバスト制御（Robust Control）」です。

---

## 🎯 学習目標

- ロバスト制御の基本概念と必要性を理解する  
- H∞制御の基本原理と数式構造を把握する  
- ゲイン余裕・位相余裕によるロバスト性評価を説明できる  
- μ（ミュー）解析などの応用的評価法に触れる

---

## ❓ なぜロバスト性が必要か？

- **モデル化誤差**：実機と数式モデルが完全一致することは稀  
- **外乱・ノイズ**：センサ雑音、入力遅延、外部環境の変動など  
- **パラメータのばらつき**：量産品の性能差、経年劣化

これらに対応し、**「性能を保ちながら安定性を保証する」**のがロバスト制御の目標です。

---

## 📐 ロバスト性の定義

- **内部安定性（Internal Stability）**  
    → 全信号が有界入力で有界（Bounded Input - Bounded Output）になる  
- **感度関数 $S(s)$**
  $S(s) = \frac{1}{1 + G(s)K(s)}$

- **補償関数 $T(s)$（Complementary Sensitivity）**  
　　$T(s) = \frac{G(s)K(s)}{1 + G(s)K(s)} = 1 - S(s)$

---

## 🎯 H∞制御の目的

- 最大ゲイン（無限ノルム）を**最小化**することで最悪誤差に備える

### 目的関数（例）：

$$
\| T_{zw}(s) \|_\infty < \gamma
$$

- $T_{zw}(s)$：外乱 $w$ から性能出力 $z$ への伝達関数  
- $\| \cdot \|_\infty$：最大ゲイン（周波数全体での最大）

---

## 🧩 H∞制御と感度関数の関係

- $S(s)$ が大きい → 入力外乱に弱い  
- $T(s)$ が大きい → センサノイズに弱い  
- 周波数帯ごとにどちらを重視するか設計する

---

## 📈 ゲイン余裕・位相余裕との関係

| 指標 | 内容 | 目安 | ロバスト性 |
|------|------|------|-------------|
| ゲイン余裕 GM | 増幅しても安定な範囲 | > 6 dB | ○ |
| 位相余裕 PM | 遅れても安定な範囲 | > 30 deg | ○ |
| S/N ノルム | $S(j\omega)$ のピーク値 | < 2.0 | ◎ |

---

## ⚙️ 実装ツール例（MATLAB, Python）

| ツール | 機能例 |
|--------|--------|
| MATLAB Robust Control Toolbox | hinfsyn, musyn, robstab |
| Python slycot, robustcontrol | H∞制御（制限あり）対応 |
| control.matlab.hinfsyn（Octave）| 非公式対応あり |

---

## 🧠 AITL-Hとの接続（理性層・LLM補完）

| AITL層 | 対応 | ロバスト制御との接続 |
|--------|------|------------------------|
| 理性（PID/モデル制御） | 制御対象への直接制御 | 設計時にH∞的安定性を保証 |
| 知性（LLM） | 状況・設計制約の補完 | 制御対象の変動に応じてH∞制御へ切替も |

---

## 📚 参考文献

- Zhou & Doyle, *Essentials of Robust Control*  
- Skogestad & Postlethwaite, *Multivariable Feedback Control*  
- MATLAB Robust Control Toolbox ドキュメント  
- Farshad Khorrami, *Robust Control Theory*

---
