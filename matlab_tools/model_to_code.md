# 🛠️ SimulinkモデルからCコードを生成する方法

本ガイドは、Simulinkで設計した制御ブロックを **Cコードに自動変換** し、  
その出力を `SoC_DesignKit_by_ChatGPT/c_to_hdl/` へ橋渡しするための手順を解説します。

---

## ✅ 使用するツール

- MATLAB / Simulink（R2021以降推奨）
- **Simulink Coder**（Cコード生成に必須）
- 対象モデル：`pid_simulink_example.slx`（本教材同梱）

---

## 📘 手順概要

| ステップ | 操作 |
|----------|------|
| ① | Simulinkモデルを開く（例：`pid_simulink_example.slx`） |
| ② | [Simulink] メニュー → 「コード」 → 「Cコードの生成」 |
| ③ | `codegen` フォルダ内に `pid.c`, `pid.h` などが生成される |
| ④ | 生成コードから主要演算式を抽出（例：`output = Kp * error + Ki * integral;`） |
| ⑤ | `c_to_hdl/` 配下の `conversion_prompt.md` に貼り付けて、ChatGPTにVerilog化を依頼 |

---

## 💬 ChatGPT連携プロンプト例

```markdown
# タスク: 以下のCコードをVerilogに変換して
## 条件:
- 固定小数点（Q4.4形式）で
- 毎クロック更新、出力は `ctrl_out`
```c
output = Kp * error + Ki * integral;

> 💡 HDL変換には `c_to_hdl/conversion_prompt.md` を活用してください。

---

## 🧪 応用例

- **Simulinkで状態空間モデルを設計 → Cコード生成 → FSM構成に反映**
- **FSMの各状態で使用する計算式（例：LLM制御）をSimulinkで試作 → HDL展開**

---

## 🔗 関連ディレクトリ

| パス | 内容 |
|------|------|
| `matlab_tools/` | Simulinkモデル群（PID, 状態空間） |
| `c_to_hdl/` | C→HDL変換テンプレとプロンプト |
| `execution_logs/` | ChatGPT応答ログを記録可能（任意） |

---

## 🔖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
この資料およびモデルは、教育・個人学習目的で自由に使用可能です。
