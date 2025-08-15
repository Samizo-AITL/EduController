---
layout: default
title: SoC_DesignKit_by_ChatGPT
permalink: /SoC_DesignKit_by_ChatGPT/
---

---

# 🧩 SoC_DesignKit_by_ChatGPT  
[![GitHub](https://img.shields.io/badge/GitHub-Open%20Repo-black?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/SoC_DesignKit_by_ChatGPT)  
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

💡 **このページは概要です。詳細なコードやテンプレートは [GitHubリポジトリ](https://github.com/Samizo-AITL/EduController/tree/main/SoC_DesignKit_by_ChatGPT) を参照してください。**  
ブラウザ上で直接ファイル閲覧・ダウンロード・履歴確認が可能です。

---

## 📖 概要 / Overview
**JP:** FSM・PID・LLM統合制御の **HDL実装テンプレート** と、ChatGPT用プロンプト集をまとめた教材・開発キットです。  
C→HDL変換やFSM状態遷移の自動生成など、AI支援によるSoC制御設計を加速します。

**EN:** A development kit of **HDL templates** for FSM, PID, and LLM hybrid control, plus ChatGPT prompt collections.  
Includes tools for C→HDL conversion, FSM auto-generation, and AI-assisted SoC control design.

---

## 🚀 クイックアクセス / Quick Access

### 🎯 制御テンプレート / Control Templates
| ディレクトリ | 説明 / Description |
|--------------|--------------------|
| [`fsm/`](fsm/) | 有限状態機械（FSM）テンプレート（YAML + Mermaid.js） |
| [`pid/`](pid/) | 固定小数点対応PID制御器（Verilog実装） |
| [`llm/`](llm/) | FSM × LLM統合制御テンプレート |
| [`c_to_hdl/`](c_to_hdl/) | C → Verilog変換支援テンプレート |
| [`testbench/`](testbench/) | テストベンチ例・波形出力補助 |

### 💬 プロンプトテンプレート / Prompt Templates
| ファイル | 用途 / Purpose |
|----------|---------------|
| [`fsm_prompt.md`](prompts/control_templates/fsm_prompt.md) | 状態遷移表からFSMテンプレ生成 |
| [`conversion_prompt.md`](prompts/control_templates/conversion_prompt.md) | CコードをVerilogに変換 |
| [`choose_template_prompt.md`](prompts/control_templates/choose_template_prompt.md) | 条件に合う制御テンプレ選定 |
| [`llm_control_prompt.md`](prompts/control_templates/llm_control_prompt.md) | FSM × LLM制御設計補助 |

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
- [SamizoGPT](https://samizo-aitl.github.io/SamizoGPT/) — プロンプト生成支援
- [`execution_logs/`](execution_logs/) — 実行ログ

---

## 👤 **著者 / Author**
| 項目 / Item | 詳細 / Details |
|-------------|----------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |

---

## 📄 **ライセンス / License**
> 教材・コード・図表の性質に応じたハイブリッドライセンスを採用  
> *Hybrid licensing based on the nature of the materials, code, and diagrams.*

| 項目 / Item | ライセンス / License | 説明 / Description |
|-------------|----------------------|--------------------|
| **コード（Code）** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布可<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須<br>*Attribution required* |
| **図表・イラスト（Figures & diagrams）** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

🏠 [トップページに戻る](https://samizo-aitl.github.io/EduController/)
