---
layout: default
title: choose_template_prompt.md（テンプレ選択支援プロンプト）
permalink: /SoC_DesignKit_by_ChatGPT/prompts/choose_template_prompt.html
---

---

# 🎛️ choose_template_prompt.md（テンプレ選択支援プロンプト）  
*Template Selection Support Prompt*

---

## 🎯 目的 / Purpose
Verilogや制御設計を学び始めた初学者が、  
**FSM / PID / LLM / C→HDL などのテンプレート**から  
適切なものを選べるように支援するプロンプト例です。

---

## 💬 プロンプト例 / Example Prompt

```markdown
私はVerilogを初めて学習しています。  
状態遷移制御（スタート→実行→完了）を実装したいのですが、  
どのテンプレートを使えばよいですか？

目的：
- ボタン押下で処理開始
- 一連の手順を経て完了する処理を記述
```

---

## 🔍 提案出力例（ChatGPT想定） / Example AI Output

| テンプレート / Template | 推奨理由 / When to Use |
|-------------------------|------------------------|
| **FSMテンプレート** | 状態数が少なく、明確な遷移条件がある処理に最適 |
| **PIDテンプレート** | 連続制御やアナログ的な応答が必要な場合に有効 |
| **C→HDLテンプレート** | 制御式を既にC言語で記述しており、Verilog化したい場合に使用 |
| **LLM統合テンプレート** | 状態遷移の判断や外部知能との連携が必要な高度制御に適用 |

---

## 📘 関連ファイル / Related Files

| ファイル名 / File | 説明 / Description |
|-------------------|--------------------|
| [`fsm_template.md`](../fsm_template.md) | FSM制御構成テンプレート |
| [`pid_template.md`](../pid_template.md) | PID制御構成テンプレート |
| [`conversion_prompt.md`](../c_to_hdl/conversion_prompt.md) | C→Verilog変換プロンプト |
| [`fsm_llm_hybrid_example.md`](../fsm_llm_hybrid_example.md) | FSM×LLM統合制御例 |

---

## 🔖 ライセンス / License

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)
