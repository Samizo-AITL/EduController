# 🧰 matlab_tools/

このディレクトリは、SimulinkやMATLABコードによる制御設計の演習を支援するための補助モジュール群です。  
設計モデルからCコードへの変換や、将来的なVerilog連携（C→HDL）に向けた教材基盤としても活用されます。

---

## 📁 内容構成

| ファイル名 | 内容 |
|------------|------|
| `getting_started.md` | Simulink利用手順ガイド（基本操作〜モデル開発） |
| `model_to_code.md` | SimulinkモデルからCコードを生成する手順 |
| `pid_simulink_example.slx` | PID制御のSimulinkモデル（連続制御の基本） |
| `state_space_example.slx` | 状態空間モデル（離散系設計の導入例） |

---

## 🎯 目的 / 活用意図

- EduControllerの **前段フェーズ**（制御モデル設計）におけるSimulink活用
- Cコード生成後、[`c_to_hdl/`](../c_to_hdl/) によるVerilog化の導入ステップ
- 離散時間制御、状態空間制御、PID制御などの設計検証

---

## 🔗 関連連携

| 関連ディレクトリ | 役割 |
|------------------|------|
| [`c_to_hdl/`](../c_to_hdl/) | CコードをVerilog HDLに変換（今後の展開） |
| [`testbench/`](../testbench/) | HDL化後のシミュレーション検証 |
| [`EduController`](../) | 教材本体との統合設計演習（Part04, Part05など） |

---

## 🛠️ 今後の拡張予定

- Simulink + Embedded Coder による自動Cコード生成→HDL変換支援
- `fsm_simulink_example.slx` の追加（状態遷移系の可視化設計）
- `.m` ファイル形式での状態空間シミュレーションスクリプト追加

---

## 📖 参考ドキュメント

- [MathWorks公式：Simulink入門](https://www.mathworks.com/learn/tutorials/simulink-onramp.html)
- [Simulink Coder ドキュメント](https://www.mathworks.com/products/simulink-coder.html)

---

## 🔖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
本ディレクトリ内の教材・モデルは教育・研究目的で自由に使用可能です。
