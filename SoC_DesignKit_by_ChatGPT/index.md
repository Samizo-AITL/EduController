---
layout: default
title: SoC_DesignKit_by_ChatGPT
permalink: /SoC_DesignKit_by_ChatGPT/
---

---

# 🧩 SoC_DesignKit_by_ChatGPT

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/Samizo-AITL/SoC_DesignKit_by_ChatGPT/actions/workflows/test.yml/badge.svg)](https://github.com/Samizo-AITL/SoC_DesignKit_by_ChatGPT/actions)

---

## 📖 概要 / Overview

**JP:**  
SoC_DesignKit_by_ChatGPT は、FSM・PID・LLM統合制御などの **HDL実装テンプレート** と、ChatGPT用プロンプト集です。  
**直接テンプレートにアクセスして利用できるリンク集** として構成されています。

**EN:**  
SoC_DesignKit_by_ChatGPT is a **link-based catalog** of HDL templates for FSM, PID, and LLM hybrid control, with prompt examples for ChatGPT.  
All templates are **directly accessible** for copy, modification, and integration.

---

## 🚀 クイックアクセス / Quick Access

### 🎯 制御テンプレート / Control Templates

| テンプレート | 説明 / Description |
|--------------|--------------------|
| [`fsm/`](fsm/) | 有限状態機械（FSM）テンプレート（YAML + Mermaid.js） |
| [`pid/`](pid/) | 固定小数点対応PID制御器（Verilog実装） |
| [`llm/`](llm/) | FSM × LLM統合制御テンプレート |
| [`c_to_hdl/`](c_to_hdl/) | C → Verilog変換支援テンプレート |
| [`testbench/`](testbench/) | テストベンチ例・波形出力補助 |

---

### 💬 プロンプトテンプレート / Prompt Templates

| プロンプトファイル | 用途 / Purpose |
|--------------------|---------------|
| [`fsm_prompt.md`](prompts/control_templates/fsm_prompt.md) | 状態遷移表からFSMテンプレ生成 |
| [`conversion_prompt.md`](prompts/control_templates/conversion_prompt.md) | CコードをVerilogに変換 |
| [`choose_template_prompt.md`](prompts/control_templates/choose_template_prompt.md) | 必要条件に合う制御テンプレ選定 |
| [`llm_control_prompt.md`](prompts/control_templates/llm_control_prompt.md) | FSM × LLM制御の設計補助 |

---

## 🧪 サンプル実行 / Example Run

```bash
# 1. Clone
git clone https://github.com/Samizo-AITL/SoC_DesignKit_by_ChatGPT.git
cd SoC_DesignKit_by_ChatGPT

# 2. Build & run example simulation
make run_example

# 3. View waveform
gtkwave wave.vcd
```

---

## 📘 関連リンク / Related Links

- [EduController](https://samizo-aitl.github.io/EduController/) — 本体教材（Part05/09連動）
- [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT) — プロンプト生成支援
- [`execution_logs/`](execution_logs/) — 実行ログ

---

## 👤 著者・ライセンス / Author & License

| 項目 / Item | 詳細 / Details |
|-------------|----------------|
| **Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **License** | MIT License（再配布・改変自由） |

---

🏠 [トップページに戻る](../README.md)
