---
layout: clean
title: FSM×LLM制御プロンプト
permalink: /SoC_DesignKit_by_ChatGPT/llm/llm_control_prompt/
---

---

# 🧠 FSM×LLM統合制御：構成例  
*Hybrid Control Structure: FSM with LLM Integration*

[![GitHub](https://img.shields.io/badge/GitHub-Open%20Repo-black?logo=github)](https://github.com/Samizo-AITL/EduController)  
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

---

## 📘 状態構成 / State Configuration

- **`idle`**：監視モード（一定周期で "check" をLLMに送信）  
  *Monitoring mode, periodically sends "check" to LLM*
- **`engage`**：動作中。LLMが "continue" / "adjust" / "halt" を返す  
  *Active mode; LLM returns "continue", "adjust", or "halt"*
- **`recover`**：異常対応。LLMに "analyze" を要求  
  *Recovery mode, requests "analyze" from LLM*

---

## 💬 例：LLM出力想定 / Example LLM Output

```text
[LLM応答例 / Example Response]
action = adjust
```

→ FSMは **engage** 状態中にこの出力を解析し、`adjust` に対応したサブFSMへ遷移。  
→ FSM parses output during **engage** and transitions to a sub-FSM for `adjust`.

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
        L --> P[Parse action = xxx]
    end

    FSM_Controller -- 状態遷移時に呼び出し --> LLM_Module
    LLM_Module -- 制御信号 --> FSM_Controller
```

---

## 🧩 実装イメージ（擬似コード） / Implementation Example (Pseudocode)

```
if state == engage:
    send_to_llm("system status = hot")
    if llm_response == "action = halt":
        state = recover
```

---

## 🔗 関連教材 / Related Materials

| **項目 / Item** | **説明 / Description** |
|-----------------|-------------------------|
| [`fsm/`](../fsm/) | 状態機構の基盤定義 / Base FSM definitions |
| [`fsm_llm_hybrid_example.md`](../fsm_llm_hybrid_example.md) | FSM×LLM制御の構成例 / Example of FSM × LLM control |
| [`execution_logs/`](../execution_logs/) | LLM応答ログを保存可能 / Optional logging of LLM responses |

---

## 📄 **ライセンス / License**

> 教材・コード・図表の性質に応じた **ハイブリッドライセンス** を採用  
> *Hybrid licensing based on the nature of materials, code, and diagrams.*

| **項目 / Item** | **ライセンス / License** | **説明 / Description** |
|-----------------|--------------------------|-------------------------|
| **コード（Code）** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布可<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須<br>*Attribution required* |
| **図表・イラスト（Figures & diagrams）** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

🏠 [戻る / Back](../)
