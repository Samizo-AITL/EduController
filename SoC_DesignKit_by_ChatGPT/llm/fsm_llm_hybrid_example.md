# 🧠 FSM×LLM統合制御：構成例

本例は、FSM制御器が状態遷移の中で LLM に指令を依頼し、  
得られた自然言語 or 構造出力を制御信号として再帰的に取り込むハイブリッド制御構成です。

---

## 📘 状態構成

- `idle`：監視モード（一定周期で "check" をLLMに送信）
- `engage`：動作中。LLMが "continue" / "adjust" / "halt" を返す
- `recover`：異常対応。LLMに "analyze" を要求

---

## 💬 例：LLM出力想定

```text
[LLM応答例]
action = adjust
```

→ FSMは engage 状態中にこの出力を解析し、adjust に対応したサブFSMへ遷移。

## 🧩 実装イメージ（疑似コード）
```
if state == engage:
    send_to_llm("system status = hot")
    if llm_response == "action = halt":
        state = recover
```
        
---

## 🔗 関連教材

| 項目 | 内容 |
|------|------|
| `fsm/` | 状態機構の基盤定義 |
| `fsm_prompt.md` | FSM記述テンプレ（Verilog展開可能） |
| `part09_llm_hybrid/` | EduControllerのAI統合制御教材と連携 |
| `execution_logs/` | 対話プロンプトとLLM応答を記録可能（任意） |

---

## 🔖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)

