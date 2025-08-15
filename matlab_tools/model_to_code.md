---
layout: clean
title: SimulinkモデルからCコードを生成する方法
permalink: /matlab_tools/model_to_code.html
---

---

# 🛠️ SimulinkモデルからCコードを生成する方法

本ガイドは、**Simulinkで設計した制御ブロックをCコードに自動変換**し、  
その出力を [`SoC_DesignKit_by_ChatGPT/c_to_hdl/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/) へ橋渡しするための手順を解説します。

---

## ✅ 使用ツール

| ツール / Tool | 用途 |
|---------------|------|
| **MATLAB / Simulink**（R2021以降推奨） | 制御モデル設計 |
| **Simulink Coder** | Cコード自動生成（必須） |
| **対象モデル** | [`pid_simulink_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/pid_simulink_example.slx) |

---

## 📘 手順概要

| **ステップ** | **操作内容** |
|--------------|--------------|
| ① | [`pid_simulink_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/pid_simulink_example.slx) を開く |
| ② | **[Simulink] メニュー → 「コード」 → 「Cコードの生成」** を選択 |
| ③ | `codegen` フォルダに `pid.c`, `pid.h` などが生成される |
| ④ | 生成Cコードから主要演算式を抽出（例：`output = Kp * error + Ki * integral;`） |
| ⑤ | [`c_to_hdl/conversion_prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/conversion_prompt.html) に貼り付けて、ChatGPTにVerilog化を依頼 |

---

## 💬 ChatGPT連携プロンプト例

# タスク: 以下のCコードをVerilogに変換
## 条件:
- 固定小数点（Q4.4形式）
- 毎クロック更新
- 出力は `ctrl_out`
```c
output = Kp * error + Ki * integral;
```

💡 HDL変換には [`c_to_hdl/conversion_prompt.md`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/conversion_prompt.html) を活用してください。

---

## 🧪 応用例

- **Simulinkで状態空間モデルを設計 → Cコード生成 → FSM構成に反映**
- **FSMの各状態で使用する計算式（例：LLM制御）をSimulinkで試作 → HDL展開**

---

## 🔗 関連ディレクトリ

| **パス** | **内容 / Description** |
|----------|------------------------|
| [`matlab_tools/`](https://samizo-aitl.github.io/EduController/matlab_tools/) | Simulinkモデル群（PID, 状態空間） |
| [`c_to_hdl/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/) | C→HDL変換テンプレとプロンプト |
| `execution_logs/` | ChatGPT応答ログ記録（任意） |

---

## 🔖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
この資料およびモデルは、教育・個人学習用途で自由に使用可能です。

---

**🏠 [トップページへ戻る](https://samizo-aitl.github.io/EduController/README.html)**
