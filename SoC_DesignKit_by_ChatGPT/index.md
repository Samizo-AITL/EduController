---
layout: default
title: SoC_DesignKit_by_ChatGPT/
permalink: /SoC_DesignKit_by_ChatGPT/
---

---

# 🧩 SoC_DesignKit_by_ChatGPT

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/Samizo-AITL/SoC_DesignKit_by_ChatGPT/actions/workflows/test.yml/badge.svg)](../../actions)

---

## 📖 概要 / Overview

**JP:**  
SoC_DesignKit_by_ChatGPT は、FSM・PID・LLM統合制御などの**HDL実装テンプレート**と、**ChatGPT用プロンプト**をまとめた教材・開発キットです。  
C→HDL変換や、FSM状態遷移の自動生成など、AI支援でSoC制御設計を加速します。

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

## 📦 主な内容 / Key Contents

| Category      | Description |
|---------------|-------------|
| FSM           | Verilog FSMテンプレート & YAML定義からの自動生成例 |
| PID           | 固定小数点対応のPID制御器 |
| LLM Control   | FSM × LLM統合制御のプロンプト例 |
| C→HDL         | C制御式からVerilog変換のプロンプト例 |
| Testbench     | シミュレーション・波形表示用テストベンチ |

---

## 🧠 ChatGPT連携 / Prompt Integration

テンプレートは[SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT)と連動し、  
以下のような用途で利用できます。

- FSM構造の自動生成
- PIDパラメータの自動チューニングコード作成
- C→HDL変換（固定小数点対応）
- LLMによる状態遷移トリガ生成

---

## 🔧 開発者向けコマンド / Dev Commands

```bash
# Run all tests
make test

# Clean generated files
make clean

# Generate FSM diagram from YAML
python3 scripts/fsm_to_mermaid.py examples/fsm_example.yaml
```

---

## 📚 関連リポジトリ / Related Repositories

- [EduController](https://github.com/Samizo-AITL/EduController) – 制御理論教材
- [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT) – プロンプト支援ツール

---

## 📄 ライセンス / License

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)

---

## 🏁 推奨ワークフロー / Recommended Workflow

1. **プロンプト選択** – `prompts/` から用途に合ったテンプレを選択  
2. **コード生成** – ChatGPT等でVerilogやテストベンチを生成  
3. **シミュレーション** – `make` または `iverilog` + `gtkwave`  
4. **改良・再実行** – 設計パラメータや遷移条件を調整

---

