# 🧠 conversion_prompt.md（C→Verilog変換プロンプト）

## 🎯 目的
C言語で記述された簡単な制御式やアルゴリズムを、Verilog HDL に変換するプロンプトテンプレートです。ChatGPT等と連携して、HDL初学者向けの構造設計演習を支援します。

---

## 📝 入力テンプレート（Cコード形式）

```c
// 例: PI制御の1ステップ演算
error = ref - meas;
integral = integral + error;
output = Kp * error + Ki * integral;
```

---

## 💬 プロンプト例（ChatGPT用）

```
以下のCコードを、固定小数点を考慮したVerilog HDLに変換してください。
- `ref`, `meas`, `output`, `integral`, `error` は16ビット幅
- `Kp`, `Ki` は定数（パラメータ）として定義
- 逐次処理用のalwaysブロック内で記述

[Cコード]
---
error = ref - meas;
integral = integral + error;
output = Kp * error + Ki * integral;
---
```

---

## ✅ 注意点
- HDLでは積和演算のビット幅拡張に注意
- `parameter` 定数の使い方、`always_ff` or `always @ (posedge clk)` の使い分け
- 初期化やリセット処理も必要に応じて付加

---

## 🧪 併用リソース
- [`testbench/`](../testbench/) にて出力波形の確認を行う
- 演習用FSMと組み合わせた `PID-FSM` アーキテクチャへの発展も可能
