---
layout: clean
title: 🧪 テストベンチ実行ガイド
permalink: /SoC_DesignKit_by_ChatGPT/testbench/run_testbench.html
---

---

# 🧪 テストベンチ実行ガイド  
*How to Run Testbenches in Verilog*

---

## 🎯 目的 / Objective
本ガイドでは、**Verilogで作成したRTL**を検証するための  
**テストベンチ（Testbench）実行方法**を説明します。  
Icarus Verilog / Verilator を利用して、**動作検証・デバッグ**を行います。

---

## ✅ 必要ツール / Required Tools

| ツール名 | 用途 |
|----------|------|
| **Icarus Verilog** (`iverilog`, `vvp`) | ソースのコンパイルとシミュレーション |
| **Verilator** | 高速シミュレーション、C++連携 |
| **GTKWave** | 波形ファイル（VCD/FST）の可視化 |

---

## 🔧 実行手順 / Execution Steps

### Icarus Verilog を使う場合
```bash
# 1. コンパイル（テストベンチ + DUT）
$ iverilog -o sim_out tb_module.v ../rtl/module.v

# 2. 実行（シミュレーション）
$ vvp sim_out

# 3. 波形表示（GTKWave）
$ gtkwave wave.vcd
```

### Verilator を使う場合
```bash
# 1. C++コード生成
$ verilator --cc --exe tb_module.cpp ../rtl/module.v

# 2. ビルド & 実行
$ make -C obj_dir -f Vmodule.mk Vmodule
$ ./obj_dir/Vmodule
```

---

## 🧪 観測ポイント / Key Checks

| 観測対象 | 説明 / Description |
|----------|--------------------|
| **リセット処理** | `reset` が期待通りに効いているか |
| **クロック同期** | `posedge clk` の動作確認 |
| **出力信号** | DUTからの出力が期待値と一致するか |
| **波形ログ** | VCDファイルで内部信号も確認 |

---

## 📘 教材との接続 / Related Learning Resources

| ファイル | 内容 |
|----------|------|
| [`tb/`](../testbench/) | テストベンチサンプル |
| [`rtl/`](../rtl/) | C→HDL生成済みRTL |
| [`waveform_analysis.md`](../testbench/waveform_analysis.md) | 波形解析ガイド |
| [`execution_logs/`](../execution_logs/) | 実行ログ保存用 |

---

## 📎 ヒント / Tips
- まずは**小規模回路**から動作検証を始めるとデバッグが容易。  
- `$monitor` を活用してコンソール出力でも確認可能。  
- 波形解析と組み合わせることで、RTLの不具合箇所を特定しやすくなります。

---

## 📄 ライセンス / License
本教材は **ハイブリッドライセンス** で提供されます。

- **MIT License** © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
  → コード・ドキュメント部分はMITライセンスで自由に利用可能  
- **Educational Use License**  
  → 教材部分（解説・図表・演習ガイド）は教育・研究用途での利用・改変を許諾  
  → 商用利用は要相談  
