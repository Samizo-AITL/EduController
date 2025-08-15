---
layout: clean
title: FSM設計テンプレート（YAML形式）
permalink: /SoC_DesignKit_by_ChatGPT/fsm/fsm_template.html
---

---

# 🧭 FSM設計テンプレート（YAML形式）

---

**JP:**  
このテンプレートは、**有限状態機械（Finite State Machine: FSM）** をYAML形式で記述するための基本構造です。  
設計したYAMLは、ChatGPTプロンプト補助（[SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT)）や [`fsm_to_mermaid.py`](../fsm_to_mermaid.py) を使った**状態遷移図可視化**に活用できます。

**EN:**  
This template defines the basic structure for describing a **Finite State Machine (FSM)** in YAML format.  
Designed YAML files can be used with ChatGPT prompt assistance ([SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT)) or [`fsm_to_mermaid.py`](../fsm_to_mermaid.py) for **state diagram visualization**.

---

## ✅ 記述フォーマット / Format

```yaml
fsm:
  name: example_fsm
  states:
    - idle
    - processing
    - done
  transitions:
    - from: idle
      to: processing
      trigger: start
    - from: processing
      to: done
      trigger: complete
    - from: done
      to: idle
      trigger: reset
  outputs:
    - state: idle
      signal: 0
    - state: processing
      signal: 1
    - state: done
      signal: 2
```

---

## 🧩 各項目の説明 / Field Descriptions

| キー / Key | 説明 / Description |
|------------|--------------------|
| `name` | FSMの名称（任意） / FSM name (optional) |
| `states` | 状態のリスト / List of states |
| `transitions` | 状態遷移の定義（from → to + trigger） / State transitions (from → to + trigger) |
| `outputs` *(optional)* | 各状態で出力する信号 / State-dependent output values |

---

## 🧪 使用方法 / How to Use

1. このテンプレートを基に、例：`fsm_example_counter.yaml` を作成  
   Create your FSM definition file (e.g., `fsm_example_counter.yaml`) based on this template.
2. [`fsm_to_mermaid.py`](../fsm_to_mermaid.py) でMermaid.jsコードへ変換  
   Convert it to Mermaid.js code using [`fsm_to_mermaid.py`](../fsm_to_mermaid.py).
3. [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT) の `fsm_prompt.md` を利用してVerilogコードへ展開  
   Use `fsm_prompt.md` in [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT) to generate Verilog code.

---

## 📘 関連ファイル / Related Files

| ファイル / File | 説明 / Description |
|-----------------|--------------------|
| [`fsm_example_counter.yaml`](./fsm_example_counter.yaml) | カウンタ用の簡易FSMサンプル / Sample FSM for counter logic |
| [`fsm_to_mermaid.py`](../fsm_to_mermaid.py) | YAML→Mermaid.js変換スクリプト / YAML to Mermaid.js converter |
| [`fsm_prompt.md`](../prompts/control_templates/fsm_prompt.md) | SamizoGPT用FSM生成プロンプト / Prompt for FSM code generation |

---

## 🔖 YAML作法の注意点 / YAML Syntax Notes

- **インデントは半角スペース2つ**（Tabは使用不可）  
  Use two spaces for indentation (no tabs).
- 文字列はクォート不要（特殊文字含む場合は `""` 推奨）  
  Strings can be unquoted unless they contain special characters.

---

## 📝 著作・ライセンス / Author & License

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
This template is provided under the MIT License for educational and personal use.

---

**🏠 [戻る / Back to FSM Directory](../)**
