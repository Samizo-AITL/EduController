---
layout: default
title: 🎯 FSM設計プロンプトテンプレート（SamizoGPT連携用）
permalink: /SoC_DesignKit_by_ChatGPT/prompts/fsm_prompt.html
---

---

# 🎯 FSM設計プロンプトテンプレート（SamizoGPT連携用）  
*FSM Design Prompt Template for ChatGPT Integration*

このテンプレートは、**有限状態機械（Finite State Machine: FSM）** の設計仕様を  
ChatGPT等の生成AIに指示し、**Verilog HDL記述**や**Mermaid.jsによる可視化**を  
自動生成させるためのプロンプト例です。

---

## 📌 基本テンプレート形式 / Basic Template Format

```markdown
# タスク: FSM制御の設計テンプレートを生成して
## 条件:
- 状態数: 4状態
- 出力制御: あり（状態ごとに異なる信号）
- HDL記述: Verilogベースでお願いします
- トリガ: start, clk, reset
- 設計思想をコメント付きで説明して
```

---

## 🔁 バリエーション例 / Variations

🧩 **YAMLベースのFSMを渡す場合**

```markdown
# タスク: このFSM定義をVerilogで実装して
## 入力形式: YAML
```yaml
fsm:
  name: counter_fsm
  states:
    - idle
    - count1
    - count2
    - done
  transitions:
    - from: idle
      to: count1
      trigger: start
    - from: count1
      to: count2
      trigger: clk
    - from: count2
      to: done
      trigger: clk
    - from: done
      to: idle
      trigger: reset
  outputs:
    - state: idle
      signal: 0b00
    - state: count1
      signal: 0b01
    - state: count2
      signal: 0b10
    - state: done
      signal: 0b11
```

条件:
- **クロック同期**の同期式FSMとして  
- 状態出力を `assign` 文で定義  
- 設計方針をコメント付きで説明

---

## ✅ ChatGPT出力例（概要） / Expected ChatGPT Output (Overview)

- `always @(posedge clk)` による状態遷移制御  
- `case (state)` 構文による状態処理分岐  
- 状態ごとの出力を `assign` 文で定義  
- 型宣言例：`reg [1:0] state;`  
- コメント例：`// idle状態では出力を00に設定`  

---

## 🔗 関連教材 / Related Resources

| リソース | 用途 |
|----------|------|
| [`fsm_example_counter.yaml`](../fsm_example_counter.yaml) | YAML構造のFSM定義例 |
| [`fsm_to_mermaid.py`](../fsm_to_mermaid.py) | YAML→Mermaid.js変換スクリプト |
| [`fsm_template.md`](../fsm_template.md) | FSM設計ガイドラインテンプレート |
| [`execution_logs/`](../execution_logs/) | プロンプト実行結果の記録用ディレクトリ |

---

## 📄 ライセンス / License
MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
本テンプレートは**教育・設計支援目的で自由に利用・改変可能**です。
