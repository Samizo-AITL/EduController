---
layout: default
title: FSM × LLM ハイブリッド制御設計補助プロンプト
permalink: /SoC_DesignKit_by_ChatGPT/llm/llm_control_prompt/
---

---

# 🧠 FSM × LLM ハイブリッド制御設計補助プロンプト

---

**JP:**  
本プロンプトは、**FSM（有限状態機械）** に **LLM（大規模言語モデル）** を組み合わせ、  
状態遷移時にLLMを呼び出して次の制御信号を指示させる**ハイブリッド制御構成**を設計するための補助ツールです。  

**EN:**  
This prompt helps design a **hybrid control system** where an **FSM (Finite State Machine)** integrates with an **LLM (Large Language Model)**,  
calling the LLM during state transitions to generate the next control command.

---

## 🎯 前提条件 / Design Requirements

| 要件 / Requirement | 詳細 / Details |
|--------------------|----------------|
| FSM状態 / FSM States | `idle` → `engage` → `recover` |
| LLMの役割 / LLM Role | 制御文生成・外部判断支援 / Control command generation & external decision support |
| 呼び出しタイミング / Call Timing | FSMの状態遷移時（`idle`→`engage`、`engage`→`recover`など） |
| LLM出力形式 / LLM Output Format | `"action = [xxx]"` 形式（例: `action = adjust`） |
| FSMでの評価 / FSM Evaluation | LLM出力を解析し、次状態またはサブFSMに遷移 |

---

## 💬 ChatGPT連携用プロンプト例 / Example Prompt for ChatGPT

```markdown
# タスク: FSM構成にLLMを組み合わせたハイブリッド制御の設計補助をして
## 条件:
- FSM：3状態（idle / engage / recover）
- LLM：制御文生成・外部判断支援を担当
- FSMが状態遷移時にLLMを呼び出し、次の制御信号を指示させる構成
- LLMの返答は "action = [xxx]" の形式とし、それをFSMが評価
- HDL構成図または擬似コードで説明して
```

---

## 🧩 実装イメージ（擬似コード） / Implementation Sketch (Pseudocode)

```python
if state == idle:
    if start_signal:
        llm_cmd = call_llm("status = standby")
        state = engage

elif state == engage:
    llm_cmd = call_llm("status = active")
    if llm_cmd == "action = adjust":
        state = engage  # adjust logic
    elif llm_cmd == "action = halt":
        state = recover

elif state == recover:
    llm_cmd = call_llm("status = error")
    if llm_cmd == "action = reset":
        state = idle
```

---

## 📊 HDL構成図イメージ / HDL Structure Diagram

```mermaid
flowchart LR
    subgraph FSM_Controller [FSM Controller]
        I[idle] -->|start| E[engage]
        E -->|halt| R[recover]
        R -->|reset| I
    end

    subgraph LLM_Module [LLM Interface]
        Q[Query Generator] --> L[LLM Engine]
        L --> P[Parse "action = xxx"]
    end

    FSM_Controller -- 状態遷移時に呼び出し --> LLM_Module
    LLM_Module -- 制御信号 --> FSM_Controller
```

---

## 🔗 関連教材 / Related Materials

| 項目 / Item | 説明 / Description |
|-------------|--------------------|
| [`fsm/`](../fsm/) | 状態機構の基盤定義 / Base FSM definitions |
| [`fsm_llm_hybrid_example.md`](./fsm_llm_hybrid_example.md) | FSM×LLM制御の構成例 / Example of FSM × LLM control |
| [`execution_logs/`](../execution_logs/) | LLM応答ログを保存可能 / Optional logging of LLM responses |

---

## 🔖 ライセンス / License

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
Free to use, modify, and distribute for educational and personal purposes.

---

**🏠 [戻る / Back to LLM Directory](../)**
