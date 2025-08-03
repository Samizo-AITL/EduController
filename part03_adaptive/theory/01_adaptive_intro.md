---
layout: default
title: 01. PID制御の基礎
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

# 🔄 01. 適応制御の概要（Introduction to Adaptive Control）

制御対象が**時間とともに変化**したり、**事前に正確なモデルが得られない**状況では、固定された制御器（PIDやLQRなど）では対応が困難です。  
そこで登場するのが「**適応制御（Adaptive Control）**」です。

---

## 🎯 学習目標

- 適応制御とは何かを理解する  
- なぜ適応制御が必要とされるのかを説明できる  
- 代表的な適応戦略（MRAC、L1、GS）の概要を把握する  
- AITL-Hにおける理性層との接続イメージを持つ

---

## ❓ なぜ適応制御が必要なのか？

### ✅ 制御対象の変化に対応したい

- 飛行機の重さが変わる
- モータに熱がこもって性能が変わる
- 作業物の質量や摩擦が毎回異なる

こうした**パラメータの時間的変動**に対し、制御器自体を**リアルタイムに調整**する必要があります。

---

## 🧠 適応制御の基本構造

適応制御は、以下のような構造を持ちます：
  +----------------+
  | 適応律（Updater）| ← パラメータ推定
  +----------------+
            ↓
  +----------------+
  | 制御器（Controller）|
  +----------------+
            ↓
       [ Plant ]
            ↑
          y(t)

  - 適応律が制御器のパラメータを調整する  
- 制御器はその都度更新されたパラメータで制御を実施

---

## 📘 代表的な適応制御の分類

| 名称 | 内容 | 利点 | 課題 |
|------|------|------|------|
| **MRAC** | モデル参照型適応制御<br>（Model Reference Adaptive Control） | 理論体系が確立 | 設計が複雑 |
| **L1適応制御** | 高速かつ安定にパラメータ適応 | 分離原理による設計の容易さ | 設定自由度が高すぎることも |
| **ゲインスケジューリング（GS）** | 状態に応じて制御ゲインを切替 | 実装が簡単 | 離散的変化で不連続になる可能性 |

---

## 📐 MRACのイメージ

- 基準モデル $M(s)$ を用意  
- 出力 $y(t)$ と基準モデルの出力 $y_m(t)$ の差を最小化  
- 誤差に基づいて制御ゲインを更新（MITルール、Lyapunov法など）

---

## 🧠 AITL-Hとの関係性（理性層）

| AITL層 | 対応制御 | 適応制御との関係 |
|--------|----------|------------------|
| 本能（FSM） | 状態遷移・ルール制御 | 状況識別により適応制御を切り替える |
| 理性（PID/モデル制御） | 汎用的な物理制御 | 適応制御がこの層の性能を動的に調整 |
| 知性（LLM） | 推論・戦略判断 | 適応律やモデル選択をLLMが補助可能 |

---

## 📚 参考資料

- Ioannou & Sun, *Robust Adaptive Control*  
- Åström & Wittenmark, *Adaptive Control*  
- Ogata, *Modern Control Engineering*  
- L1 Adaptive Control: Naira Hovakimyan (UIUC)

---
