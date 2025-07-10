# 🤖 Part 9: ハイブリッド制御とLLM統合（Hybrid Control with LLM Integration）

本章では、状態機械（FSM）、物理制御（PIDなど）、そして **大規模言語モデル（LLM）** を組み合わせた、  
柔軟かつ適応的な統合制御アーキテクチャを設計・検証します。

AITL構想（FSM × PID × LLM）に基づき、AI時代の制御システム構築を探求します。

---

## 🎯 学習目標

- FSM（状態遷移）とPID制御の連携方法を理解する
- ChatGPTやGPT-4などのLLMを制御判断に活用する方法を学ぶ
- 状況・環境に応じた**ルールベース／対話ベースの制御戦略**を設計する
- シナリオ制御、例外対応、目的推論などの知能制御設計を体験する
- AITL構想による三層型ハイブリッド制御を実装する

---

## 🧩 章構成

| ファイル | 内容 |
|---------|------|
| [`01_fsm_pid_llm.md`](theory/01_fsm_pid_llm.md) | FSM・PID・LLMの三層制御構造（AITL構想）概要 |
| [`02_scenario_control.md`](theory/02_scenario_control.md) | シナリオ制御とLLMによる判断の導入 |
| [`03_exception_handling.md`](theory/03_exception_handling.md) | 異常対応・例外処理と知識注入 |
| [`04_goal_reasoning.md`](theory/04_goal_reasoning.md) | 目的推論と対話型制御の導入 |

---

## 🧪 実装コードとNotebook

| ファイル | 役割 |
|---------|------|
| [`fsm_pid_llm_sim.py`](simulation/fsm_pid_llm_sim.py) | 三層統合制御のシミュレーションPoC |
| [`goal_reasoning_agent.py`](simulation/goal_reasoning_agent.py) | 目的推論エージェントのクラス実装 |
| [`hybrid_control_demo.ipynb`](notebooks/hybrid_control_demo.ipynb) | Notebook形式の統合デモ・可視化実行 |

---

## 🔜 今後の展開（Next Steps）

- ChatGPT APIとのリアル連携による実機制御実験
- ロボット実装／GUI／音声対話制御への応用展開
- 自己適応・オンライン学習との統合（Part10構想へ）

---

## 📚 参考資料・リンク

- OpenAI ChatGPT: https://platform.openai.com/
- 教材本体：EduController プロジェクト
