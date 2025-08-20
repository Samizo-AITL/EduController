---
layout: clean
title: FSM設計テンプレート（YAML形式）
permalink: /SoC_DesignKit_by_ChatGPT/fsm/fsm_template.html
---

---

# 🧭 FSM設計テンプレート（YAML形式）  
**FSM Design Template (YAML Format)**

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

| **キー / Key** | **説明 / Description** |
|----------------|-------------------------|
| `name` | FSMの名称（任意） / FSM name (optional) |
| `states` | 状態のリスト / List of states |
| `transitions` | 状態遷移の定義（from → to + trigger） / State transitions (from → to + trigger) |
| `outputs` *(optional)* | 各状態で出力する信号 / State-dependent output values |

---

## 🧪 使用方法 / How to Use

1. **テンプレートを基にFSM定義ファイル作成**（例：`fsm_example_counter.yaml`）  
   Create your FSM definition file (e.g., `fsm_example_counter.yaml`) based on this template.  

2. **Mermaid図に変換** — [`fsm_to_mermaid.py`](../fsm_to_mermaid.py) を用いて可視化  
   Convert to Mermaid.js diagram using [`fsm_to_mermaid.py`](../fsm_to_mermaid.py).  

3. **Verilogコードへ展開** — [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT) の `fsm_prompt.md` を利用  
   Use `fsm_prompt.md` in [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT) to generate Verilog code.  

---

## 📘 関連ファイル / Related Files

| **ファイル / File** | **説明 / Description** |
|----------------------|-------------------------|
| [`fsm_example_counter.yaml`](./fsm_example_counter.yaml) | カウンタ用の簡易FSMサンプル / Sample FSM for counter logic |
| [`fsm_to_mermaid.py`](../fsm_to_mermaid.py) | YAML→Mermaid.js変換スクリプト / YAML to Mermaid.js converter |
| [`fsm_prompt.md`](../prompts/control_templates/fsm_prompt.md) | SamizoGPT用FSM生成プロンプト / Prompt for FSM code generation |

---

## 🔖 YAML作法の注意点 / YAML Syntax Notes

- **インデントは半角スペース2つ**（Tab禁止）  
  Use **two spaces** for indentation (tabs not allowed).  
- 文字列は基本クォート不要（特殊文字含む場合は `""` 推奨）  
  Strings can be unquoted unless they contain special characters.  

---

## 📄 **ライセンス / License**

> 教材・コード・図表の性質に応じた **ハイブリッドライセンス** を採用  
> *Hybrid licensing based on the nature of the materials, code, and diagrams.*

| **項目 / Item** | **ライセンス / License** | **説明 / Description** |
|-----------------|--------------------------|-------------------------|
| **コード（Code）** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布可<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須<br>*Attribution required* |
| **図表・イラスト（Figures & diagrams）** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

👤 MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  

---

**🏠 [戻る / Back to FSM Directory](../)**
