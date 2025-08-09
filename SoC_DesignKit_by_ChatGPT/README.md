# 🧩 SoC_DesignKit_by_ChatGPT

**JP:**  
**SoC_DesignKit_by_ChatGPT** は、[EduController](../) における制御実装演習のためのテンプレート集です。  
FSM、PID、LLM統合制御などの構成要素を、**HDL記述ベースで学ぶためのテンプレート・プロンプト・テストベンチ**を提供します。

**EN:**  
**SoC_DesignKit_by_ChatGPT** is a collection of design templates used in [EduController](../) to support hands-on control system implementation.  
It provides reusable HDL-based templates, prompt examples, and testbenches for FSM, PID, and LLM-integrated control structures.

本モジュールは、[**SamizoGPT**](https://github.com/Samizo-AITL/SamizoGPT) のプロンプト支援と連携し、ChatGPT等を用いた構造設計・コード生成・設計進化の記録（[`execution_logs/`](execution_logs/)）とも連動します。  
This module integrates with [**SamizoGPT**](https://github.com/Samizo-AITL/SamizoGPT), enabling prompt-based structured design, code generation, and logging of design evolution using ChatGPT.  

---

## 🎯 目的 / Purpose

- 📘 教材として学んだ制御理論を、**実装テンプレートとして具体化**  
  📘 Translate theoretical knowledge of control into practical implementation templates.

- ♻️ FSM / PID / LLMなどの**実装構造を再利用可能な形で提供**  
  ♻️ Provide reusable implementation templates for FSM, PID, and LLM-based control.

- 🤖 ChatGPTを活用した C → Verilog 変換や制御構造生成の**プロンプト演習に対応**  
  🤖 Support prompt-driven exercises such as converting C to Verilog using ChatGPT.

- 🔗 [EduController](../) の **Part05（実装編）・Part09（LLM制御）**と連動  
  🔗 Linked with **Part05 (Implementation)** and **Part09 (LLM-based Control)** in [EduController](../).

---

## 📁 ディレクトリ構成 / Directory Structure

| ディレクトリ / Directory | 内容 / Description |
|--------------------------|--------------------|
| [`fsm/`](fsm/) | 有限状態機械テンプレート（YAML記述・Mermaid.js変換支援）<br> FSM templates with YAML + Mermaid.js support |
| [`pid/`](pid/) | PID制御器のVerilog実装（固定小数点対応）<br> Verilog PID controller with fixed-point arithmetic |
| [`llm/`](llm/) | FSM×LLMの統合制御テンプレ<br> Templates for FSM × LLM hybrid control |
| [`c_to_hdl/`](c_to_hdl/) | C→Verilog変換支援テンプレ（プロンプト付き）<br> Prompt-based support for C to Verilog conversion |
| [`testbench/`](testbench/) | テストベンチ例、波形出力、RTLシミュレーション補助<br> Example testbenches for simulation and waveform viewing |

---

## 🧠 ChatGPT連携 / Prompt Integration with ChatGPT

以下のプロンプトテンプレート群と連携しています：  
The following prompt templates are integrated:

| テンプレート名 / Template | 対応ディレクトリ | 内容 / Description |
|---------------------------|------------------|---------------------|
| [`fsm_prompt.md`](./prompts/control_templates/fsm_prompt.md) | [`fsm/`](fsm/) | FSM構成を記述し、テンプレを自動生成 / Generate FSM templates from state & trigger descriptions |
| `conversion_prompt.md` ※近日追加予定 / coming soon | [`c_to_hdl/`](c_to_hdl/) | CコードをVerilogに変換 / Convert C control logic to Verilog |
| `choose_template_prompt.md` ※近日追加予定 / coming soon | 全体 / general | テンプレ選択を支援 / Recommend templates based on needs |
| `llm_control_prompt.md` ※近日追加予定 / coming soon | [`llm/`](llm/) | FSM×LLM制御の構造設計補助 / Support hybrid FSM × LLM control design |

💬 実行ログは [`execution_logs/`](execution_logs/) に記録可能です。  
💬 Execution results and prompt history can be saved under [`execution_logs/`](execution_logs/).

---

## 🔧 活用例 / Example Use Cases

### ✅ FSM制御の可視化 / FSM Visualization Example

```yaml
# fsm_example_counter.yaml
states:
  - idle
  - count
transitions:
  - from: idle
    to: count
    trigger: start
```

→ `fsm_to_mermaid.py` により状態遷移図を自動生成  
→ Visualize FSM transitions using `fsm_to_mermaid.py`

---

### ✅ PID式のC→HDL変換演習 / PID: C to HDL via ChatGPT

```c
// 入力式（C言語）
error = ref - meas;
output = Kp * error + Ki * integral;
```

→ `conversion_prompt.md` によるVerilog変換 → `testbench/` にてシミュレーション  
→ Use `conversion_prompt.md` to generate Verilog, simulate with `testbench/`

---

## 📎 連携教材 / Linked Materials

| 教材 / Material | 内容 / Details |
|----------------|----------------|
| [EduController](../) | 本体教材。Part05/09と連携 / Main curriculum (Part05/09) |
| [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT) | プロンプトテンプレート支援 / Prompt template generator |
| [`execution_logs/`](execution_logs/) | 実行記録や設計ログの保存先 / Logs of prompt execution and design outputs |

---

## 🛠️ 今後の拡張予定 / Future Extensions

- Simulink→C→HDL変換対応（[`matlab_tools/`](../matlab_tools/) との連携）  
  Simulink to C to Verilog support (via [`matlab_tools/`](../matlab_tools/))

- VHDLテンプレート対応  
  VHDL template generation

- Vivado等FPGAツールとの連携ドキュメント  
  Integration with FPGA tools like Vivado (documentation support)

---

## 👤 **著者・ライセンス / Author & License**

| **項目 / Item** | **内容 / Details** |
|-----------------|--------------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

**🏠 [トップページ / Back to Home](../README.md)**

