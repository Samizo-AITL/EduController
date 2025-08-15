---
layout: default
title: SoC_DesignKit_by_ChatGPT
permalink: /SoC_DesignKit_by_ChatGPT/
---

---

# 🧩 SoC_DesignKit_by_ChatGPT

[![GitHub](https://img.shields.io/badge/GitHub-Open%20Repo-black?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/SoC_DesignKit_by_ChatGPT)
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

💡 **このページは概要です。実際のコードやテンプレートは [GitHubリポジトリ](https://github.com/Samizo-AITL/EduController/tree/main/SoC_DesignKit_by_ChatGPT) 上で直接操作できます。**  
ブラウザでファイルを開く／ダウンロードする／更新履歴を確認するなどの操作が可能です。

SoC_DesignKit_by_ChatGPT は、FSM・PID・LLM統合制御などの **HDL実装テンプレート** と、ChatGPT用プロンプトをまとめた教材・開発キットです。  
C→HDL変換やFSM状態遷移の自動生成など、AI支援でSoC制御設計を加速します。

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

## 👤 **著者 / Author**

| **項目 / Item** | **内容 / Details** |
|------------------|---------------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |

---

## 📄 **ライセンス / License**
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)  

> 教材・コード・図表の性質に応じたハイブリッドライセンスを採用。  
> *Hybrid licensing based on the nature of the materials, code, and diagrams.*

| 📌 項目 / Item | ライセンス / License | 説明 / Description |
|------|------|------|
| **コード（Code）** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布が可能<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須<br>*Attribution required* |
| **図表・イラスト（Figures & diagrams）** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ許可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

🏠 [トップページに戻る](../README.md)

