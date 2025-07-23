# 🤖 llm_control_prompt.md（FSM×LLM統合制御プロンプト）

## 🎯 目的
有限状態機械（FSM）に基づいた制御構造に、ChatGPTや他のLLMによるトリガ生成・アドバイスを組み合わせる設計支援テンプレートです。

---

## 🧠 典型構成

- FSM：従来の状態遷移制御を記述
- LLM：状況に応じたイベント判断や目標選択
- インタフェース：LLMの出力をFSMのトリガに変換（`trigger = llm_decision`）

---

## 💬 プロンプト例（構造提案）

```
FSM構造を以下のように定義し、ChatGPTから与えられる文字列出力に応じて状態遷移する設計を提案してください。

States: idle → analyze → act
Triggers: "start", "suggest_action", "apply"

FSMのトリガをLLMの出力と連携するには、どのように設計すべきか、Verilog記述例を含めて説明してください。
```
