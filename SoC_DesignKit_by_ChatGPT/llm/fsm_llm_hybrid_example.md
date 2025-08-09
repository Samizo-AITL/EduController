---
layout: default
title: FSM × LLM統合制御：構成例
permalink: /SoC_DesignKit_by_ChatGPT/llm/fsm_llm_hybrid_example.html
---

---

# 🧠 FSM × LLM統合制御：構成例

---

**JP:**  
本例は、**FSM（有限状態機械）** が状態遷移の中で **LLM（大規模言語モデル）** に指令を送信し、  
得られた自然言語または構造化出力を**制御信号として再帰的に取り込む**ハイブリッド制御構成です。

**EN:**  
This example demonstrates a **hybrid control architecture** where an **FSM (Finite State Machine)** sends commands to an **LLM (Large Language Model)** during state transitions,  
and incorporates the natural language or structured output as **control signals** back into the FSM.

---

## 📘 状態構成 / State Definitions

| 状態 / State | 説明 / Description |
|--------------|--------------------|
| `idle` | 監視モード。一定周期で `"check"` コマンドをLLMに送信 / Monitoring mode; periodically sends `"check"` to LLM |
| `engage` | 動作中。LLMから `"continue"` / `"adjust"` / `"halt"` のいずれかを受信 / Active mode; LLM returns `"continue"`, `"adjust"`, or `"halt"` |
| `recover` | 異常対応。LLMに `"analyze"` を要求 / Recovery mode; requests `"analyze"` from LLM |

---

## 💬 LLM出力例 / Example LLM Output

```text
[LLM Response Example]
action = adjust
```

- FSMは `engage` 状態中にこの出力を解析  
- `adjust` に対応した**サブFSM**や制御ロジックへ遷移  

FSM parses this during `engage` state and transitions to a **sub-FSM** or control logic corresponding to `adjust`.

---

## 🧩 実装イメージ（疑似コード） / Implementation Sketch (Pseudocode)

```python
if state == engage:
    send_to_llm("system status = hot")
    if llm_response == "action = halt":
        state = recover
```

---

## 🔗 関連教材 / Related Materials

| 項目 / Item | 説明 / Description |
|-------------|--------------------|
| [`fsm/`](../fsm/) | 状態機構の基盤定義 / Base FSM definitions |
| [`fsm_prompt.md`](../prompts/control_templates/fsm_prompt.md) | FSM記述テンプレート（Verilog展開可能） / FSM template for Verilog generation |
| [`part09_llm_hybrid/`](../../EduController/part09_llm_hybrid/) | EduControllerのAI統合制御教材 / AI hybrid control materials in EduController |
| [`execution_logs/`](../execution_logs/) | プロンプトとLLM応答を記録可能 / Optional logging of prompts and LLM responses |

---

## 🔖 ライセンス / License

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
Free to use, modify, and distribute for educational and personal purposes.

---

**🏠 [戻る / Back to LLM Directory](../)**
