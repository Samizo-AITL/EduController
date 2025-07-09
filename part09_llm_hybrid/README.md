# 🤖 Part 9: ハイブリッド制御とLLM統合（Hybrid Control with LLM Integration）

本章では、状態機械（FSM）、物理制御（PIDなど）、そして**大規模言語モデル（LLM）**を組み合わせた、  
柔軟かつ適応的な統合制御アーキテクチャを設計・検証します。  
AITL構想（FSM×PID×LLM）に基づき、AI時代の制御システム構築を探求します。

---

## 🎯 学習目標 / Learning Objectives

- FSM（状態遷移）とPID制御の連携方法を理解する
- ChatGPTやGPT-4などのLLMを制御判断に活用する方法を学ぶ
- 状況・環境に応じた**ルールベース／対話ベースの制御戦略**を設計する
- シナリオ制御、例外対応、目的推論などの知能制御設計を体験する
- AITL構想による三層制御構造の概念とPoC例を学ぶ

---

## 🧩 主なトピック / Key Topics

| トピック | 内容 |
|----------|------|
| FSM×PID×LLM | 本能（FSM）＋ 理性（PID）＋ 知性（LLM）の三層構造 |
| 状態機械制御 | 状況に応じた制御戦略の切替（例：姿勢 → 回避 → 省電力） |
| LLM判断の導入 | LLMによる意図解釈・対話式指令生成・例外処理 |
| ChatGPT API活用 | LLMと制御ロジックの接続（プロンプト設計・モード選択） |
| AITL構想 | AITL-H（Hybrid）構造と制御階層の役割分担設計

---

## 📂 サブフォルダ構成
```
part09_llm_hybrid/
├── theory/          # FSM・PID・LLMの統合構成理論
├── prompts/         # ChatGPT用プロンプトテンプレート
├── python/          # 制御統合例（FSM+PID+LLM実装）
├── notebooks/       # 実験ノートブック（対話制御、状態遷移ログ等）
├── figures/         # アーキテクチャ図、状態遷移図、LLM判断構造
└── README.md
```
---

## 🛠️ 推奨ツール / Tools

- Python: `transitions`, `control`, `openai`, `numpy`, `matplotlib`
- LLM連携: ChatGPT API（GPT-4o推奨）、System Prompt設計
- 状態遷移可視化: `graphviz`, `diagrams`

---

## 🔗 関連資料

- AITL構想（All-in-Theory Logic）：https://github.com/Samizo-AITL/AITL-H
- OpenAI ChatGPT API: https://platform.openai.com/docs/
- FSMライブラリ：https://github.com/pytransitions/transitions
- ハイブリッド制御文献：Branicky et al. "Hybrid Dynamical Systems"

---

## 📌 備考

本章は EduController の集大成的な位置づけです。  
制御理論、AI制御、LLM知能判断の**三層連携による構造設計**を通じて、  
次世代の制御系統のあり方を探索します。

---
