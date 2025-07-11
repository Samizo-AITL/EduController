# 🔄 05. データ駆動 vs モデルベース制御（統合と展望）

本節では、これまで学んできた**データ駆動型制御**と、  
伝統的な**モデルベース制御**との違いや統合の方向性について整理します。

---

## 🎯 基本的な違い

| 観点 | モデルベース制御 | データ駆動型制御 |
|------|------------------|------------------|
| 必要な情報 | 数式モデル（力学方程式など） | 観測データ |
| 建模の手法 | 理論ベース（物理法則） | 統計・学習・回帰 |
| 利点 | 理論的保証・解析的手法が可能 | 柔軟性・建模不要・実験的に強い |
| 欠点 | モデル誤差に弱い・開発コスト大 | 過学習・汎化性の確保が課題 |

---

## 🔁 統合的アプローチの例

| 統合方法 | 内容 |
|----------|------|
| モデル補完型 | 不完全なモデルをデータで補正（例：NN補正、リカレント残差） |
| モデル予測型 | データ同定モデルでMPCを構築 |
| 学習支援型 | 強化学習・DMDの結果をPIDなどに反映 |
| データ駆動H∞制御 | データに基づくロバスト制御器の設計（近年研究） |

---

## 🧪 実践上の選択戦略

- **モデルが既知 or 入手可能**な場合：
  → モデルベース制御＋簡易なフィードバック補正

- **モデル化が困難 or 現場対応重視**の場合：
  → データ駆動型制御（DMD, Koopman, NN）

- **ハイブリッド戦略**：
  → 初期設計にモデルを用い、運用段階でデータ補正を組み込む

---

## 🧠 AITL構想との関係

- FSM（本能層）：ルールベース制御
- PID（理性層）：モデルベース補償
- LLM（知性層）：データ駆動・文脈適応制御（Koopman, RL, NN）

> 本教材の最終章では、これらの融合として「知能制御アーキテクチャ」を扱います。

---

## 🔚 まとめ

- モデルベースとデータ駆動は対立概念ではなく、**補完的な技術**
- 現代の制御設計では、両者を適切に組み合わせる設計戦略が鍵となります

📁 次へ：[`README.md`](../README.md)

---
