# 📊 波形確認ガイド（PID制御器）

この文書では、Verilogシミュレーション結果の波形を確認する手順を説明します。

---

## ✅ 必要ツール

- Icarus Verilog（iverilog）
- GTKWave（波形ビューワ）

---

## 🔧 シミュレーション手順

```bash
# コンパイル
$ iverilog -o sim_pid tb_pid_controller.v ../pid/pid_controller.v

# 実行（VCDファイル出力）
$ vvp sim_pid

# 波形表示
$ gtkwave wave.vcd
```

---

## 🧪 観測ポイント

| 信号 | 説明 |
|------|------|
| `ref` | 目標値（定数） |
| `meas` | 測定値（毎クロック変化） |
| `ctrl_out` | PID出力（追従挙動が確認できる） |
| `error`, `integral`（オプション） | モジュール内レジスタを `$dumpvars` に追加可 |

---

## 📘 教材との接続

| モジュール | 関連 |
|------------|------|
| `pid_controller.v` | テスト対象 |
| `tb_pid_controller.v` | テストベンチ |
| `fixed_point_notes.md` | 出力精度確認に活用 |
| `execution_logs/` | シミュレーション条件と結果を記録可能（任意） |

---

## 🔖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)

---
