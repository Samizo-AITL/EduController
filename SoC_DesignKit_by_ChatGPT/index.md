---
layout: clean
title: SoC_DesignKit
permalink: /SoC_DesignKit_by_ChatGPT/
---

---

# 🧩 **SoC_DesignKit**

---

## 🔗 公式リンク | *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/SoC_DesignKit_by_ChatGPT)

---

## 📖 **概要 / Overview**

**JP:** FSM・PID・LLM統合制御の **HDL実装テンプレート** と、ChatGPT用プロンプト集をまとめた教材・開発キットです。  
C→HDL変換やFSM状態遷移の自動生成など、**AI支援によるSoC制御設計を加速**します。  

**EN:** A development kit of **HDL templates** for FSM, PID, and LLM hybrid control, plus **prompt collections** for ChatGPT.  
Includes tools for **C→HDL conversion**, **FSM auto-generation**, and **AI-assisted SoC control design**.

---

## 🚀 **クイックアクセス / Quick Access**

### 🎯 **制御テンプレート / Control Templates**

| **ディレクトリ / Directory** | **説明 / Description** |
|------------------------------|-------------------------|
| [`fsm/`](fsm/) | 有限状態機械（FSM）テンプレート（YAML + Mermaid.js）<br>*FSM templates (YAML + Mermaid.js)* |
| [`pid/`](pid/) | 固定小数点対応PID制御器（Verilog実装）<br>*Fixed-point PID controller (Verilog)* |
| [`llm/`](llm/) | FSM × LLM統合制御テンプレート<br>*FSM × LLM hybrid control templates* |
| [`c_to_hdl/`](c_to_hdl/) | C → Verilog変換支援テンプレート<br>*C → Verilog conversion templates* |
| [`testbench/`](testbench/) | テストベンチ例・波形出力補助<br>*Example testbenches & waveform tools* |

### 💬 **プロンプトテンプレート / Prompt Templates**

| **ファイル / File** | **用途 / Purpose** |
|----------------------|---------------------|
| [`fsm_prompt.md`](prompts/control_templates/fsm_prompt.md) | 状態遷移表からFSMテンプレ生成<br>*Generate FSM templates from state tables* |
| [`conversion_prompt.md`](prompts/control_templates/conversion_prompt.md) | CコードをVerilogに変換<br>*Convert C code to Verilog* |
| [`choose_template_prompt.md`](prompts/control_templates/choose_template_prompt.md) | 条件に合う制御テンプレ選定<br>*Select control templates by conditions* |
| [`llm_control_prompt.md`](prompts/control_templates/llm_control_prompt.md) | FSM × LLM制御設計補助<br>*Assist in FSM × LLM control design* |

---

## 🧪 **サンプル実行 / Example Run**

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

## 📘 **関連リンク / Related Links**

- [EduController](https://samizo-aitl.github.io/EduController/) — 本体教材（Part05/09連動）<br>*Main materials (linked with Part05/09)*  
- [`execution_logs/`](execution_logs/) — 実行ログ<br>*Execution logs*  

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** | [![Hybrid License](https://img.shields.io/badge/License-Hybrid-blueviolet?style=for-the-badge)](https://samizo-aitl.github.io/EduController/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

🏠 [**トップページに戻る / Back to Top**](https://samizo-aitl.github.io/EduController/)
