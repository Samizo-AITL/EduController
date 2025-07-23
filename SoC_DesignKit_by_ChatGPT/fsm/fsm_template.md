# 🧭 FSM設計テンプレート（YAML形式）

このテンプレートは、**有限状態機械（Finite State Machine: FSM）** をYAML形式で記述するための基本構造です。  
設計したYAMLは、ChatGPTプロンプト補助（SamizoGPT）や `fsm_to_mermaid.py` を使った可視化に活用できます。

---

## ✅ 記述フォーマット

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

## 🧩 各項目の説明

| キー | 内容 |
|------|------|
| `name` | FSMの名称（任意） |
| `states` | 状態のリスト（状態名の列挙） |
| `transitions` | 状態遷移の定義（from → to + trigger） |
| `outputs`（任意） | 各状態で出力する信号など（状態依存出力） |

---

## 🧪 使用方法（例）

- このテンプレートをベースに `fsm_example_counter.yaml` などのFSMを定義
- `fsm_to_mermaid.py` を使用し、Mermaid.jsに変換
- ChatGPT（SamizoGPT）にプロンプトとして渡し、Verilog記述へ展開も可能

---

## 📘 関連ファイル

| ファイル名 | 内容 |
|------------|------|
| `fsm_example_counter.yaml` | カウント用の簡易FSMサンプル |
| `fsm_to_mermaid.py` | YAML→Mermaid.js変換スクリプト |
| `fsm_prompt.md`（`prompts/`） | SamizoGPT用プロンプトテンプレート（FSM生成） |

---

## 🔖 補足：YAML作法の注意点

- インデントはスペース2つで統一（Tab不可）
- 文字列はクォート無しでもOK（ただし記号含む場合は `""` 推奨）

---

## 📝 著作・ライセンス

本テンプレートは [Samizo-AITL/SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT) に準拠して提供され、MITライセンスのもとで自由に利用可能です。

---
