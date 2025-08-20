---
layout: clean
title: c_to_hdl/
permalink: /SoC_DesignKit_by_ChatGPT/c_to_hdl/
---

---

# 🧩 c_to_hdl/

[![GitHub](https://img.shields.io/badge/GitHub-Open%20Repo-black?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/SoC_DesignKit_by_ChatGPT/c_to_hdl)  
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

---

## 📖 概要 / Overview

**JP:**  
このディレクトリは、**Cコードで記述された制御式やアルゴリズム**を **Verilog HDL** に変換するためのプロンプトテンプレート集です。  
ChatGPTなどのLLMと連携し、**自動コード生成**や**実装演習**を効率的に行うための基盤を提供します。  

**EN:**  
This directory contains **prompt templates** for converting **control expressions or algorithms written in C** into **Verilog HDL**.  
It is designed to work with ChatGPT or similar LLMs, enabling efficient **automatic code generation** and **hands-on implementation exercises**.  

---

## 📄 内容 / Contents

| **ファイル名 / Filename** | **内容 / Description** |
|----------------------------|-------------------------|
| [`prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/prompt.md) | **C→Verilog変換プロンプト**（ChatGPT連携）<br>**Prompt template for C→Verilog conversion** (ChatGPT integration) |

---

## 🔧 使用例 / Usage Examples

- [EduController](https://samizo-aitl.github.io/EduController/) の **Part05（制御実装）**・**Part06（固定小数点化）**と連携  
  Integrated with **Part05 (Control Implementation)** and **Part06 (Fixed-Point Conversion)** in [EduController](https://samizo-aitl.github.io/EduController/)

- `PID` や `FSM` 設計と組み合わせた **統合制御演習**  
  Combined with `PID` and `FSM` design for **integrated control exercises**

**例 / Example (C code → Verilog):**

```c
// C言語での制御式
output = Kp * error + Ki * integral;
```

→ [`prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/prompt.md) に貼り付けて **Verilog変換を依頼**  
→ Paste into [`prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/prompt.md) and request **Verilog conversion**

---

## 🛠️ 今後の拡張 / Planned Extensions

- **高度なアルゴリズム対応**：状態機械（FSM）、離散フィルタ（FIR/IIR）変換支援  
  *Support for advanced algorithms such as FSM and discrete filters (FIR/IIR)*  

- **Python（NumPy）→HDL変換**：科学計算コードの直接変換テンプレート  
  *Support for converting Python (NumPy) code directly into HDL*  

- **Simulink→C→HDL連携**：[`matlab_tools/`](https://samizo-aitl.github.io/EduController/matlab_tools/) との統合  
  *Integration with [`matlab_tools/`](https://samizo-aitl.github.io/EduController/matlab_tools/) for Simulink → C → HDL workflows*  

---

## 📎 関連リンク / Related Links

- [SoC_DesignKit_by_ChatGPT](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/)  
- [`PID`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/pid/)  
- [`FSM`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/fsm/)  

---

## 📄 **ライセンス / License**

> 教材・コード・図表の性質に応じた **ハイブリッドライセンス** を採用  
> *Hybrid licensing based on the nature of materials, code, and diagrams.*  

| **項目 / Item** | **ライセンス / License** | **説明 / Description** |
|-----------------|--------------------------|-------------------------|
| **コード（Code）** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布可<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須<br>*Attribution required* |
| **図表・イラスト（Figures & diagrams）** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

**🏠 [トップページ / Back to Home](https://samizo-aitl.github.io/EduController/)**
