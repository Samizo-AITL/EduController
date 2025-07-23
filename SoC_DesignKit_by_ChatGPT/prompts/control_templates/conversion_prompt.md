# 🧠 conversion_prompt.md（C→Verilog変換プロンプト）

## 🎯 目的
C言語で記述された制御式やアルゴリズムを、Verilog HDL に変換するプロンプトテンプレートです。

---

## 📝 入力テンプレート例（Cコード）

```c
error = ref - meas;
integral = integral + error;
output = Kp * error + Ki * integral;
```

---

## 💬 ChatGPT用プロンプト例

```
以下のCコードを、固定小数点演算を考慮した Verilog HDL に変換してください。
- 16ビット幅、逐次処理、parameterによる定数指定を想定

[Cコード]
---
error = ref - meas;
integral = integral + error;
output = Kp * error + Ki * integral;
---
```
