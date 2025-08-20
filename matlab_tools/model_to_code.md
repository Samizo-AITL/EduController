---
layout: clean
title: SimulinkモデルからCコードを生成する方法 / How to Generate C Code from Simulink Models
permalink: /matlab_tools/model_to_code.html
---

---

# 🛠️ SimulinkモデルからCコードを生成する方法  
**🛠️ How to Generate C Code from Simulink Models**

---

本ガイドは、**Simulinkで設計した制御ブロックをCコードに自動変換**し、  
その出力を [`SoC_DesignKit_by_ChatGPT/c_to_hdl/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/) へ橋渡しするための手順を解説します。  

This guide explains how to **automatically convert control blocks designed in Simulink into C code**,  
and how to bridge the output to [`SoC_DesignKit_by_ChatGPT/c_to_hdl/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/) for further processing.

---

## ✅ 使用ツール / Required Tools

| ツール / Tool | 用途 / Purpose |
|---------------|----------------|
| **MATLAB / Simulink**（R2021以降推奨 / R2021 or later recommended） | 制御モデル設計 / Control model design |
| **Simulink Coder** | Cコード自動生成（必須） / Automatic C code generation (required) |
| **対象モデル / Target Model** | [`pid_simulink_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/pid_simulink_example.slx) |

---

## 📘 手順概要 / Procedure Overview

| **ステップ / Step** | **操作内容 / Operation** |
|----------------------|--------------------------|
| ① | [`pid_simulink_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/pid_simulink_example.slx) を開く / Open the model |
| ② | **[Simulink] メニュー → 「コード」 → 「Cコードの生成」** / Select **[Simulink] → Code → Generate C Code** |
| ③ | `codegen` フォルダに `pid.c`, `pid.h` などが生成される / Files such as `pid.c`, `pid.h` will be generated in `codegen` |
| ④ | 生成Cコードから主要演算式を抽出（例：`output = Kp * error + Ki * integral;`） / Extract key equations from the generated C code (e.g., `output = Kp * error + Ki * integral;`) |
| ⑤ | [`c_to_hdl/conversion_prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/conversion_prompt.html) に貼り付けて、ChatGPTにVerilog化を依頼 / Paste into [`c_to_hdl/conversion_prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/conversion_prompt.html) and request Verilog conversion via ChatGPT |

---

## 💬 ChatGPT連携プロンプト例 / Example Prompt for ChatGPT

### タスク / Task  
以下のCコードをVerilogに変換してください  
Convert the following C code to Verilog.

### 条件 / Conditions  
- 固定小数点（Q4.4形式） / Fixed-point (Q4.4 format)  
- 毎クロック更新 / Update every clock cycle  
- 出力は `ctrl_out` / Output signal is `ctrl_out`

```c
output = Kp * error + Ki * integral;
```

💡 HDL変換には [`c_to_hdl/conversion_prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/conversion_prompt.html) を活用してください。  
💡 Use [`c_to_hdl/conversion_prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/conversion_prompt.html) for HDL conversion.

---

## 🧪 応用例 / Applications

- **Simulinkで状態空間モデルを設計 → Cコード生成 → FSM構成に反映**  
  Design a state-space model in Simulink → Generate C code → Apply to FSM structure  

- **FSMの各状態で使用する計算式（例：LLM制御）をSimulinkで試作 → HDL展開**  
  Prototype calculation formulas for each FSM state (e.g., LLM control) in Simulink → Expand into HDL  

---

## 🔗 関連ディレクトリ / Related Directories

| **パス / Path** | **内容 / Description** |
|-----------------|-------------------------|
| [`matlab_tools/`](https://samizo-aitl.github.io/EduController/matlab_tools/) | Simulinkモデル群（PID, 状態空間） / Simulink models (PID, State-space) |
| [`c_to_hdl/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/) | C→HDL変換テンプレとプロンプト / Templates & prompts for C→HDL conversion |
| `execution_logs/` | ChatGPT応答ログ記録（任意） / Logs of ChatGPT responses (optional) |

---

## 🔖 ライセンス / License

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
この資料およびモデルは、教育・個人学習用途で自由に使用可能です。  
This material and models are freely available for educational and personal learning purposes.

---

**🏠 [トップページへ戻る / Back to Top](https://samizo-aitl.github.io/EduController/README.html)**
