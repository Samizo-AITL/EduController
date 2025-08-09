---
layout: default
title: SoC_DesignKit_by_ChatGPT
permalink: /SoC_DesignKit_by_ChatGPT/ 
---

---

# 🧩 SoC_DesignKit_by_ChatGPT

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/Samizo-AITL/SoC_DesignKit_by_ChatGPT/actions/workflows/test.yml/badge.svg)](../../actions)

---

## 📖 概要 / Overview

**JP:**  
SoC_DesignKit_by_ChatGPT は、FSM・PID・LLM統合制御などの **HDL実装テンプレート** と、ChatGPT用プロンプトをまとめた教材・開発キットです。  
C→HDL変換やFSM状態遷移の自動生成など、AI支援でSoC制御設計を加速します。

**EN:**  
SoC_DesignKit_by_ChatGPT is a design kit containing **HDL templates** for FSM, PID, and LLM hybrid control, along with **prompt examples** for ChatGPT-assisted development.  
It supports AI-driven workflows for C-to-HDL conversion and automatic FSM generation.

---

## 🚀 クイックスタート / Quick Start

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

## 🎯 目的 / Purpose

- 📘 教材として学んだ制御理論を、**実装テンプレートとして具体化**  
  📘 Translate theoretical knowledge of control into practical implementation templates.

- ♻️ FSM / PID / LLMなどの**実装構造を再利用可能な形で提供**  
  ♻️ Provide reusable implementation templates for FSM, PID, and LLM-based control.

- 🤖 ChatGPTを活用した C → Verilog 変換や制御構造生成の**プロンプト演習に対応**  
  🤖 Support prompt-driven exercises such as converting C to Verilog using ChatGPT.

---

## 📁 主な構成 / Main Contents

- `fsm/` — 有限状態機械テンプレート（YAML＋Mermaid.js変換）  
- `pid/` — 固定小数点対応PID制御器（Verilog実装）  
- `llm/` — FSM×LLM統合制御テンプレート  
- `c_to_hdl/` — C→Verilog変換支援テンプレート  
- `testbench/` — テストベンチ例、波形出力補助

---

## 🧠 ChatGPT連携 / Prompt Integration

| テンプレート | 用途 |
|--------------|------|
| `fsm_prompt.md` | 状態遷移表からFSMテンプレ生成 |
| `conversion_prompt.md` | CコードをVerilogに変換 |
| `llm_control_prompt.md` | FSM×LLM制御の設計補助 |

---

## 📘 関連リンク / Related Links

- [EduController](https://samizo-aitl.github.io/EduController/) — 本体教材（Part05/09連動）
- [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT) — プロンプト支援
- [`execution_logs/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/execution_logs/) — 実行ログ

---

## 👤 著者・ライセンス / Author & License

| 項目 / Item | 詳細 / Details |
|-------------|----------------|
| **Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **License** | MIT License（再配布・改変自由） |

---

🏠 [トップページに戻る](https://samizo-aitl.github.io/EduController/)

