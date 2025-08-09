---
layout: default
title: matlab_tools/
permalink: /matlab_tools/
---

---

# 🧰 matlab_tools/

このディレクトリは、**SimulinkやMATLABコードによる制御設計の演習**を支援する補助モジュール群です。  
設計モデルからCコードへの変換や、将来的なVerilog連携（C→HDL）に向けた教材基盤としても活用されます。

---

## 📘 Simulink / MATLABとは？

**MATLAB** は、数値計算・可視化・プログラミングを統合した技術計算環境です。  
**Simulink** は、MATLABと連携して動作するブロック線図ベースの**モデルベースデザインツール**であり、制御系設計・信号処理・システムシミュレーションに広く用いられています。

| 概要 | 内容 |
|------|------|
| **MATLAB** | スクリプトベースの数値計算環境。行列演算、関数定義、制御工学ツールボックスなどを利用可能。 |
| **Simulink** | グラフィカルなブロック線図により、連続/離散システムを視覚的に設計・シミュレーション可能。ブロックの接続で制御系を構築。 |
| **Simulink Coder** | 作成したSimulinkモデルからC/C++コードを自動生成し、組込み制御システムへの実装が可能。 |

> 🎯 本教材は、制御工学の演習において **Simulinkでモデル設計 → Cコード生成 → HDL連携へ展開** する一連の流れを支援します。

---

## 📁 内容構成

| ファイル名 | 内容 |
|------------|------|
| [`getting_started.md`](https://samizo-aitl.github.io/EduController/matlab_tools/getting_started.html) | Simulink利用手順ガイド（基本操作〜モデル開発） |
| [`model_to_code.md`](https://samizo-aitl.github.io/EduController/matlab_tools/model_to_code.html) | SimulinkモデルからCコードを生成する手順 |
| [`pid_simulink_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/pid_simulink_example.slx) | PID制御のSimulinkモデル（連続制御の基本） |
| [`state_space_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/state_space_example.slx) | 状態空間モデル（離散系設計の導入例） |

---

## 🎯 目的 / 活用意図

- **EduController** の **前段フェーズ**（制御モデル設計）におけるSimulink活用
- **Cコード生成後**、[`c_to_hdl/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/) によるVerilog化の導入ステップ
- 離散時間制御、状態空間制御、PID制御などの設計検証
- **MATLAB/Simulinkの教育的導入**から自動化・HDL連携までの一貫教材化

---

## 🔗 関連連携

| 関連ディレクトリ | 役割 |
|------------------|------|
| [`c_to_hdl/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/) | CコードをVerilog HDLに変換（今後の展開） |
| [`testbench/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/testbench/) | HDL化後のシミュレーション検証 |
| [`EduController`](https://samizo-aitl.github.io/EduController/) | 教材本体との統合設計演習（Part04, Part05など） |

---

## 🛠️ 今後の拡張予定

- Simulink + Embedded Coder による自動Cコード生成→HDL変換支援
- `fsm_simulink_example.slx` の追加（状態遷移系の可視化設計）
- `.m` ファイル形式での状態空間シミュレーションスクリプト追加
- SimulinkモデルからのPython連携（Simulink Compiler活用）

---

## 📖 参考ドキュメント

- [📘 MathWorks公式：Simulink入門](https://www.mathworks.com/learn/tutorials/simulink-onramp.html)
- [📘 Simulink Coder ドキュメント](https://www.mathworks.com/products/simulink-coder.html)
- [📘 Control System Toolbox](https://www.mathworks.com/products/control.html)

---

## 👤 **著者・ライセンス / Author & License**

| **項目 / Item** | **内容 / Details** |
|-----------------|--------------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

**🏠 [トップページ / Back to Home](https://samizo-aitl.github.io/EduController/)**
