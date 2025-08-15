---
layout: default
title: matlab_tools/
permalink: /matlab_tools/
---

---

# 🧰 matlab_tools/  
[![GitHub](https://img.shields.io/badge/GitHub-Open%20Repo-black?logo=github)](https://github.com/Samizo-AITL/EduController/tree/main/matlab_tools)  
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

💡 **このページは概要です。詳細なコードやモデルは [GitHubリポジトリ](https://github.com/Samizo-AITL/EduController/tree/main/matlab_tools/) を参照してください。**  
ブラウザ上で直接ファイル閲覧・ダウンロード・履歴確認が可能です。

このディレクトリは、**SimulinkやMATLABコードによる制御設計演習**を支援する補助モジュール群です。  
設計モデルからCコードへの変換や、将来的なVerilog連携（C→HDL）に向けた教材基盤としても活用されます。

---

## 📘 MATLAB / Simulink とは？

**MATLAB** は、数値計算・可視化・プログラミングを統合した技術計算環境です。  
**Simulink** は、MATLABと連携して動作するブロック線図ベースの**モデルベースデザインツール**であり、制御系設計・信号処理・システムシミュレーションに広く利用されています。

| 概要 | 説明 |
|------|------|
| **MATLAB** | スクリプトベースの数値計算環境。行列演算、関数定義、制御工学ツールボックスなどを利用可能。 |
| **Simulink** | 連続/離散システムをブロック線図で設計・シミュレーション。GUIベースで制御系構築が可能。 |
| **Simulink Coder** | 作成したモデルからC/C++コードを自動生成し、組込みシステムへ実装可能。 |

> 🎯 本教材は **Simulinkでモデル設計 → Cコード生成 → HDL連携** までの流れを教育目的で支援します。

---

## 📁 内容構成
| ファイル / ディレクトリ | 内容 / Description |
|------------------------|---------------------|
| [`getting_started.md`](https://samizo-aitl.github.io/EduController/matlab_tools/getting_started.html) | Simulink利用手順（基本操作〜モデル開発） |
| [`model_to_code.md`](https://samizo-aitl.github.io/EduController/matlab_tools/model_to_code.html) | SimulinkモデルからCコード生成する手順 |
| [`pid_simulink_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/pid_simulink_example.slx) | PID制御のSimulinkモデル |
| [`state_space_example.slx`](https://samizo-aitl.github.io/EduController/matlab_tools/state_space_example.slx) | 状態空間モデル例（離散系設計） |

---

## 🎯 活用目的
- **EduController** の前段フェーズ（制御モデル設計）でのSimulink活用
- **Cコード生成後**、[`c_to_hdl/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/) によるVerilog化への導入
- PID制御・状態空間制御などの設計検証
- MATLAB/Simulink教育から自動化・HDL連携までの一貫教材化

---

## 🔗 関連リンク
| ディレクトリ | 役割 |
|--------------|------|
| [`c_to_hdl/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/c_to_hdl/) | CコードをVerilog HDLに変換（今後の展開） |
| [`testbench/`](https://samizo-aitl.github.io/EduController/SoC_DesignKit_by_ChatGPT/testbench/) | HDL化後のシミュレーション検証 |
| [EduController](https://samizo-aitl.github.io/EduController/) | 教材本体との統合演習（Part04, Part05など） |

---

## 🛠️ 今後の拡張予定
- Simulink + Embedded Coder による自動Cコード生成→HDL変換支援
- `fsm_simulink_example.slx` の追加（状態遷移可視化設計）
- `.m` ファイル形式での状態空間シミュレーションスクリプト追加
- SimulinkモデルからのPython連携（Simulink Compiler活用）

---

## 📖 参考ドキュメント
- [📘 MathWorks公式：Simulink入門](https://www.mathworks.com/learn/tutorials/simulink-onramp.html)  
- [📘 Simulink Coder ドキュメント](https://www.mathworks.com/products/simulink-coder.html)  
- [📘 Control System Toolbox](https://www.mathworks.com/products/control.html)

---

## 👤 **著者 / Author**
| 項目 / Item | 詳細 / Details |
|-------------|----------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |

---

## 📄 **ライセンス / License**
> 教材・コード・図表の性質に応じたハイブリッドライセンスを採用  
> *Hybrid licensing based on the nature of the materials, code, and diagrams.*

| 項目 / Item | ライセンス / License | 説明 / Description |
|-------------|----------------------|--------------------|
| **コード（Code）** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布可<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須<br>*Attribution required* |
| **図表・イラスト（Figures & diagrams）** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

🏠 [トップページに戻る](https://samizo-aitl.github.io/EduController/)
