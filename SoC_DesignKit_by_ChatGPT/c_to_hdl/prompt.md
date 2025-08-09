---
layout: default
title: conversion_prompt.md
permalink: /SoC_DesignKit_by_ChatGPT/c_to_hdl/prompt.html
---

---

# 🧠 conversion_prompt.md（C→Verilog変換プロンプト）

---

**JP:**  
このテンプレートは、**C言語で記述された制御式やアルゴリズム**を **Verilog HDL** に変換するためのプロンプト例を提供します。  
ChatGPTなどのLLMと組み合わせて利用し、**HDL初学者向けの実装演習**や**固定小数点処理の理解**を促進します。

**EN:**  
This template provides example prompts for converting **control expressions or algorithms written in C** into **Verilog HDL**.  
It is intended for use with LLMs such as ChatGPT to support **beginner-friendly HDL implementation exercises** and **understanding of fixed-point processing**.

---

## 🎯 目的 / Purpose

- CコードからVerilog HDLへの変換プロセスを学習  
  Learn the process of converting C code to Verilog HDL
- 固定小数点演算やビット幅管理の演習  
  Practice fixed-point arithmetic and bit-width handling
- FSMやPID制御器などの構造設計に展開可能  
  Expand to structural design such as FSM and PID controllers

---

## 📝 入力テンプレート（Cコード形式） / Input Template (C Code)

```c
// 例: PI制御の1ステップ演算
// Example: One-step PI control calculation
error = ref - meas;
integral = integral + error;
output = Kp * error + Ki * integral;
```

---

## 💬 ChatGPT用プロンプト例 / Example Prompt for ChatGPT

```
以下のCコードを、固定小数点を考慮したVerilog HDLに変換してください。
Please convert the following C code into Verilog HDL with fixed-point arithmetic.

条件 / Conditions:
- `ref`, `meas`, `output`, `integral`, `error` は16ビット幅
- `Kp`, `Ki` は定数（parameter）として定義
- 逐次処理用の always ブロック内で記述
- Use 16-bit width for `ref`, `meas`, `output`, `integral`, and `error`
- Define `Kp` and `Ki` as constants (parameter)
- Implement inside an always block for sequential logic

[Cコード / C Code]
---
error = ref - meas;
integral = integral + error;
output = Kp * error + Ki * integral;
---
```

---

## ✅ 注意点 / Notes

- 積和演算（multiply-accumulate）のビット幅拡張に注意  
  Pay attention to bit-width extension in multiply-accumulate operations
- `parameter` による係数定義と `always_ff` / `always @ (posedge clk)` の使い分け  
  Use `parameter` for coefficient definition and choose between `always_ff` or `always @ (posedge clk)`
- リセット処理や初期化コードを必要に応じて追加  
  Add reset or initialization logic as needed

---

## 🧪 関連リソース / Related Resources

- [📂 `testbench/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/testbench/) — 出力波形確認用テストベンチ  
  Testbench for waveform verification

- [📂 `fsm/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/fsm/) — FSMとの組み合わせ例  
  Example combination with FSM

- [📂 `pid/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/pid/) — PID制御器テンプレート  
  PID controller template

---

**🏠 [SoC_DesignKit_by_ChatGPTトップへ / Back to SoC_DesignKit_by_ChatGPT](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/)**
