---
layout: default
title: 固定小数点演算に関する注意点（Q4.4）
permalink: /SoC_DesignKit_by_ChatGPT/fixed_point/q4_4_notes.html
---

---

# 🧮 固定小数点演算に関する注意点（Q4.4）  
*Notes on Fixed-Point Arithmetic (Q4.4 Format)*

VerilogでPID制御器や信号処理ロジックを設計する際、  
**固定小数点（fixed-point）演算**を正しく扱うためのポイントを整理します。

---

## ✅ 採用フォーマット / Adopted Format

- 本テンプレートでは **Q4.4 形式** を使用  
  *(8bit: 符号1bit + 整数部3bit + 小数部4bit)*
- **値の範囲**：`-8.0` ～ `+7.9375`
- **分解能**：`1/16 ≒ 0.0625`

---

## 🔧 実装上の工夫 / Implementation Tips

| 項目 / Item | 内容 / Details |
|-------------|----------------|
| **乗算結果の桁数拡張** | `8bit × 8bit = 16bit` 演算を行い、**上位8bit**を抽出してQ4.4を保持 |
| **積分項の精度確保** | `reg [15:0] integral` として保持し、加算誤差や累積誤差に強い設計 |
| **スケーリング** | 出力時は `pid_raw[15:8]` を使用し、適切にQ4.4スケールへ変換 |

---

## 💬 注意点 / Cautions

- **オーバーフロー対策**：飽和演算や制限処理を組み込むこと  
  *Use saturation logic to prevent overflow*
- **桁落ち対策**：非常に小さな `Ki` では積分効果が無視される可能性あり  
  *Tiny `Ki` values may cause loss of effect due to truncation*

---

## 📘 関連教材 / Related Materials

| ファイル / File | 説明 / Description |
|-----------------|--------------------|
| [`pid_controller.v`](../pid_controller.v) | Verilog RTLテンプレート / PID Controller Template |
| [`c_to_hdl/`](../c_to_hdl/) | C→Verilog変換演習 / C-to-HDL Conversion Exercises |

---

## 🔖 ライセンス / License

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)
