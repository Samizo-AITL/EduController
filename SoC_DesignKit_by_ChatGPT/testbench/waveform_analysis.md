---
layout: clean
title: 📊 波形確認ガイド（PID制御器）
permalink: /SoC_DesignKit_by_ChatGPT/testbench/waveform_analysis.html
---

---

# 📊 波形確認ガイド（PID制御器）  
*Waveform Verification Guide for PID Controller in Verilog*

---

## 🎯 目的 / Objective
本ガイドでは、**Verilog PID制御器**のシミュレーション結果を波形で確認する手順を解説します。  
Icarus Verilog + GTKWave 環境を用いて、**出力挙動・内部信号の動き**を可視化します。

---

## ✅ 必要ツール / Required Tools

| ツール名 | 用途 |
|----------|------|
| **Icarus Verilog** (`iverilog`) | Verilogソースのコンパイルとシミュレーション |
| **GTKWave** (`gtkwave`) | VCD波形ファイルの可視化 |

> 💡 これらはLinux/Mac/Windows（WSL含む）で利用可能。インストールは各OSのパッケージマネージャを推奨。

---

## 🔧 シミュレーション手順 / Simulation Steps

```bash
# 1. コンパイル（テストベンチ + DUT）
$ iverilog -o sim_pid tb_pid_controller.v ../pid/pid_controller.v

# 2. 実行（VCDファイル出力）
$ vvp sim_pid

# 3. 波形表示（GTKWave）
$ gtkwave wave.vcd
```

> 📝 **補足**：  
> - `$dumpfile("wave.vcd")` と `$dumpvars` をテストベンチに記述することで、波形ファイルが生成されます。  
> - 信号の階層パスに注意し、必要な内部信号も `$dumpvars` に追加すると解析が容易になります。

---

## 🧪 観測ポイント / Key Signals to Observe

| 信号名 | 説明 / Description |
|--------|--------------------|
| `ref` | 目標値（定数または可変） |
| `meas` | 測定値（毎クロック変化） |
| `ctrl_out` | PID制御出力（追従挙動を確認） |
| `error` | 目標値と測定値の差 |
| `integral` | 積分項（オプション、固定小数点精度を確認） |

---

## 📘 教材との接続 / Related Learning Resources

| モジュール | 関連内容 |
|------------|----------|
| [`pid_controller.v`](../pid/pid_controller.v) | テスト対象（DUT） |
| [`tb_pid_controller.v`](../testbench/tb_pid_controller.v) | テストベンチ |
| [`fixed_point_notes.md`](../notes/fixed_point_notes.md) | 固定小数点の精度と演算方法 |
| [`execution_logs/`](../execution_logs/) | 実行条件・結果記録用フォルダ |

---

## 📎 ヒント / Tips
- 波形は時間軸をズームして確認することで、制御応答の細部が把握しやすくなります。  
- `ctrl_out` のオーバーシュートや整定時間を測定することで、PIDゲインの適否を評価できます。  
- 複数シナリオを異なるVCDファイルに出力し、比較分析するのも効果的です。

---

## 📄 ライセンス / License
MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
本ガイドは**教育・設計支援目的**で自由に利用・改変可能です。
