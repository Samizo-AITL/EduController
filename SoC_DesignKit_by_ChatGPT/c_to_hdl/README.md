---
layout: clean
title: c_to_hdl/
permalink: /SoC_DesignKit_by_ChatGPT/c_to_hdl/README.html 
---

---

# 🧩 c_to_hdl/

---

**JP:**  
このディレクトリは、**Cコードで記述された制御式やアルゴリズム**を **Verilog HDL** に変換するためのプロンプトテンプレート集です。  
ChatGPTなどのLLMと連携し、**自動コード生成**や**実装演習**を効率的に行うための基盤を提供します。

**EN:**  
This directory contains **prompt templates** for converting **control expressions or algorithms written in C** into **Verilog HDL**.  
It is designed to work with ChatGPT or similar LLMs, enabling efficient **automatic code generation** and **hands-on implementation exercises**.

---

## 📄 内容 / Contents

| ファイル名 / Filename | 内容 / Description |
|-----------------------|--------------------|
| [`prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/prompt.md) | C→Verilog変換のためのプロンプトテンプレート（ChatGPT連携）<br>Prompt template for converting C to Verilog (ChatGPT integration) |

---

## 🔧 使用例 / Usage Examples

- [EduController](https://samizo-aitl.github.io/EduController/) の **Part05（制御実装）**・**Part06（固定小数点化）**と連携  
  Integrated with **Part05 (Control Implementation)** and **Part06 (Fixed-Point Conversion)** in [EduController](https://samizo-aitl.github.io/EduController/)

- `PID` や `FSM` 設計と組み合わせた **統合制御演習**  
  Combined with `PID` and `FSM` design for **integrated control exercises**

**例 / Example:**

```c
// C言語での制御式
output = Kp * error + Ki * integral;
```

→ [`prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/prompt.md) に貼り付けてVerilog変換を依頼  
→ Paste into [`prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/prompt.md) and request Verilog conversion

---

## 🛠️ 今後の拡張 / Planned Extensions

- **高度なアルゴリズム対応**：状態機械（FSM）、離散フィルタ（FIR/IIR）変換支援  
  Support for more complex algorithms: FSM and discrete filters (FIR/IIR)

- **Python（NumPy）→HDL変換**：科学計算コードの直接変換テンプレート  
  Support for converting Python (NumPy) code directly to HDL

- **Simulink→C→HDL連携**：[`matlab_tools/`](https://samizo-aitl.github.io/EduController/matlab_tools/) との統合  
  Integration with [`matlab_tools/`](https://samizo-aitl.github.io/EduController/matlab_tools/) for Simulink → C → HDL workflows

---

## 📎 関連リンク / Related Links

- [SoC_DesignKit_by_ChatGPT](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/)  
- [`PID`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/pid/)  
- [`FSM`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/fsm/)  

---

**🏠 [トップページ / Back to Home](https://samizo-aitl.github.io/EduController/)**
