# 🧰 MATLAB / Simulink：導入と活用ガイド

本資料は、EduController教材において **Simulink を使った制御ブロックの可視化・設計・Cコード生成** を行うための導入ガイドです。  
制御理論の学習に加え、**モデルベース設計（Model-Based Design）**の視点も養うことを目的としています。

---

## ✅ 本教材でのSimulinkの役割

| 用途 | 対象章 | 目的 |
|------|--------|------|
| PID設計と可視化 | Part01, Part05 | ブロック図で構造と応答を直感的に理解 |
| 状態空間モデル構成 | Part02 | 行列ベースの制御設計（A,B,C,D）を視覚化 |
| Cコード生成 | Part05 | Simulink CoderによるHDL前段階のコード出力 |
| FSM構造モデリング | Part09 | Stateflow連携によるFSM構成も可能（応用） |

---

## 🛠️ 環境準備

### 必要ソフトウェア

- **MATLAB**：R2021以降推奨
- **Simulink**（必須）
- **Simulink Coder**（Cコード出力に必要）
- （オプション）Stateflow、Embedded Coder

### 教育版・学生版の利用

MATLABは教育機関を通じて**学生版ライセンス**や**オンキャンパスライセンス**が提供されています。  
詳細は [MathWorks公式](https://www.mathworks.com/academia/) をご参照ください。

---

## 📂 同梱モデル一覧

| ファイル名 | 内容 |
|------------|------|
| `pid_simulink_example.slx` | 比例積分制御のモデル（応答確認付き） |
| `state_space_example.slx` | 状態空間モデル（A,B,C,D構成）とステップ応答 |
| `model_to_code.md` | Simulink CoderでCコードを出力・展開する方法 |

---

## 📘 操作手順：PID制御モデル例

1. `pid_simulink_example.slx` を開く
2. ブロック図上で `Kp` や `Ki` を調整
3. スコープでステップ応答を観察
4. 必要であれば「シミュレーション→コード生成」へ（要 Simulink Coder）

---

## 🔄 HDL連携構想（参考）

Simulink Coder により生成したCコードは、`SoC_DesignKit_by_ChatGPT/c_to_hdl/` に渡すことで  
ChatGPTを使った C→Verilog 変換に活用可能です。

> 例：`conversion_prompt.md` に貼り付けて HDL化指示を行う。

---

## 🔖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
このガイドおよび関連モデルは、教育・個人学習用途で自由に使用可能です。
