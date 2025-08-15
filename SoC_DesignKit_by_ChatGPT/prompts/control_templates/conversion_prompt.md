---
layout: clean
title: conversion_prompt.md（C→Verilog変換プロンプト）
permalink: /SoC_DesignKit_by_ChatGPT/prompts/conversion_prompt.html
---

---

# 🧠 conversion_prompt.md（C→Verilog変換プロンプト）  
*C→Verilog Conversion Prompt Template*

---

## 🎯 目的 / Purpose
C言語で記述された**制御式やアルゴリズム**を、  
**Verilog HDL** に変換する際の **ChatGPT連携用プロンプトテンプレート**です。  
固定小数点や逐次処理など、FPGA/ASIC実装に必要な条件を明示できます。

---

## 📝 入力テンプレート例（Cコード） / Input Template Example (C Code)

```c
// PI制御の1ステップ演算例
error = ref - meas;
integral = integral + error;
output = Kp * error + Ki * integral;
```

---

## 💬 ChatGPT用プロンプト例 / Example Prompt for ChatGPT

```markdown
以下のCコードを、固定小数点演算（Q4.4形式）を考慮した Verilog HDL に変換してください。
条件:
- 信号幅は16ビット（符号付き）
- 同期式逐次処理（posedge clk）
- 定数はparameterで定義
- リセット時に内部レジスタをクリア

[Cコード]
---
error = ref - meas;
integral = integral + error;
output = Kp * error + Ki * integral;
---
```

---

## ✅ 注意点 / Notes
- **ビット幅拡張**：乗算結果は16bit以上で保持し、必要に応じて上位ビットを抽出  
- **オーバーフロー対策**：飽和演算（saturation logic）を必要に応じて追加  
- **固定小数点フォーマット**：Q形式の定義をコメント等で明記  
- **レジスタ初期化**：リセット処理で `error`, `integral`, `output` をゼロクリア  

---

## 📘 関連教材 / Related Materials

| ファイル / File | 説明 / Description |
|-----------------|--------------------|
| [`pid_controller.v`](../verilog_templates/pid_controller.v) | PID制御器Verilog RTLテンプレート |
| [`fixed_point_notes.md`](../notes/fixed_point_notes.md) | 固定小数点（Q4.4）実装の注意点 |
| [`c_to_hdl/`](../c_to_hdl/) | C→HDL変換用ディレクトリ（演習ファイル群） |

---

## 🔖 ライセンス / License
MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)
