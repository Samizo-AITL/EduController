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

## 🧩 章構成（理論教材）

| ファイル | 内容 |
|---------|------|
| [`01_fsm_pid_llm.md`](theory/01_fsm_pid_llm.md) | FSM・PID・LLMの三層制御構造（AITL構想）概要 |
| [`02_scenario_control.md`](theory/02_scenario_control.md) | シナリオ制御とLLMによる判断の導入 |
| [`03_exception_handling.md`](theory/03_exception_handling.md) | 異常対応・例外処理と知識注入 |
| [`04_goal_reasoning.md`](theory/04_goal_reasoning.md) | 目的推論と対話型制御の導入 |

---

## 🧪 実装コードとNotebook

以下は、Part 09の理論内容に対応したシミュレーションスクリプトやエージェント実装です。  
Notebookでは、動作の可視化やユーザーとの対話が実行できます。

| ファイル | 役割 |
|---------|------|
| [`fsm_pid_llm_sim.py`](simulation/fsm_pid_llm_sim.py) | 三層統合制御のシミュレーションPoC |
| [`goal_reasoning_agent.py`](simulation/goal_reasoning_agent.py) | 目的推論エージェントのクラス実装 |
| [`hybrid_control_demo.ipynb`](notebooks/hybrid_control_demo.ipynb) | Notebook形式の統合デモ・可視化実行（予定） |

---

## 🧪 実装コード対応表

| 教材章 | 内容 | 実装ファイル | 説明 |
|--------|------|--------------|------|
| 第1章 | FSM・PID・LLM 三層構成の統合 | [`fsm_pid_llm_sim.py`](simulation/fsm_pid_llm_sim.py) | モード遷移・3軸PID制御・LLM判断を含む統合PoC |
| 第2章 | シナリオ制御の設計と実行 | 〃（上記に統合） | FSMによる状態モード切替の実装含む |
| 第3章 | 例外対応・異常状態の検知と処理 | 〃 or LLMログ出力部 | LLMによる状況判断・緊急切替ロジック含む |
| 第4章 | 目的推論と対話型制御 | [`goal_reasoning_agent.py`](simulation/goal_reasoning_agent.py) | GPTなどを活用した行動決定エージェント |

> 💡 **実装の特徴**  
> - 各スクリプトは、教育用に構成されたモジュール型実装です。  
> - センサシミュレーション、PID応答、FSM切替、LLM判断のログが出力されます。  
> - 学習者は部分的なコード改変から全体統合設計まで体験できます。

---

## 🔜 今後の展開（Next Steps）

- ChatGPT APIとのリアル連携による実機制御実験
- ロボット実装／GUI／音声対話制御への応用展開
- 自己適応・オンライン学習との統合（👉 Part 10: 自律型制御構想に続く予定）

---

## 📚 参考資料・リンク

- OpenAI ChatGPT: https://platform.openai.com/
- 教材本体：EduController プロジェクト
