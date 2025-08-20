---
layout: clean
title: MATLAB / Simulink：導入と活用ガイド
permalink: /matlab_tools/getting_started.html 
---

---

# 🧰 MATLAB / Simulink：導入と活用ガイド

本資料は **EduController教材** において、  
**Simulinkを用いた制御ブロックの可視化・設計・Cコード生成** を行うための導入ガイドです。  

制御理論の学習に加えて、**モデルベース設計（Model-Based Design）** の視点を養うことを目的としています。

---

## ✅ 本教材におけるSimulinkの役割

| **用途 / Use Case** | **対象章 / Target Chapters** | **目的 / Purpose** |
|---------------------|------------------------------|--------------------|
| **PID設計と可視化** | Part01, Part05 | ブロック図で制御構造と応答を直感的に理解 |
| **状態空間モデル構成** | Part02 | 行列ベースの制御設計（A,B,C,D）を視覚化 |
| **Cコード生成** | Part05 | Simulink Coder による HDL 前段階のコード出力 |
| **FSM構造モデリング** | Part09 | Stateflow 連携による FSM 設計（応用） |

---

## 🛠️ 環境準備

### 📦 必要ソフトウェア

- **MATLAB**（推奨バージョン：R2021以降）
- **Simulink**（必須）
- **Simulink Coder**（Cコード生成に必要）
- **オプション**：Stateflow, Embedded Coder

### 🎓 教育版・学生版ライセンス

MATLAB は教育機関を通じて **学生版ライセンス** や **オンキャンパスライセンス** が提供されています。  
詳細は [📘 MathWorks公式：学術利用](https://www.mathworks.com/academia/) を参照してください。

---

## 📂 同梱モデル一覧

| **ファイル名** | **内容 / Description** |
|----------------|-------------------------|
| [`pid_simulink_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/pid_simulink_example.slx) | 比例積分制御のモデル（応答確認付き） |
| [`state_space_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/state_space_example.slx) | 状態空間モデル（A,B,C,D構成）＋ステップ応答 |
| [`model_to_code.md`](https://samizo-aitl.github.io/EduController/matlab_tools/model_to_code.html) | Simulink Coder でCコードを生成する方法 |

---

## 📘 操作手順：PID制御モデル例

1. [`pid_simulink_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/pid_simulink_example.slx) を開く  
2. ブロック図上で `Kp` や `Ki` を調整  
3. **Scope** ブロックでステップ応答を観察  
4. 必要に応じて「シミュレーション → コード生成」（要 Simulink Coder）

---

## 🔄 HDL連携構想（参考）

Simulink Coder により生成した Cコードは、  
[`SoC_DesignKit_by_ChatGPT/c_to_hdl/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/) に渡して  
**ChatGPTによる C→Verilog 変換** に活用可能です。

> 💡 例：`conversion_prompt.md` に貼り付けて HDL化の指示を行う。

---

## 📖 参考リンク

- [📘 Simulink入門（MathWorks公式）](https://www.mathworks.com/learn/tutorials/simulink-onramp.html)  
- [📘 Simulink Coder ドキュメント](https://www.mathworks.com/products/simulink-coder.html)  
- [📘 Control System Toolbox](https://www.mathworks.com/products/control.html)  

---

## 🔖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
このガイドおよび関連モデルは、教育・個人学習用途で自由に使用可能です。

---

**🏠 [トップページへ戻る](https://samizo-aitl.github.io/EduController/README.html)**
