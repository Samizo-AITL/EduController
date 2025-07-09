# 🧪 Part 5: 実装・応用編（Implementation and Applications）

本章では、制御理論の実践的な応用に焦点を当て、  
Python や MATLAB によるシミュレーション、ROS・FPGA・組込み系との連携など、  
現実的な制御系設計と実装フローを学びます。

---

## 🎯 学習目標 / Learning Objectives

- 制御理論をPythonやMATLABでシミュレーションできる
- ROSやマイコン環境と制御アルゴリズムを接続する方法を知る
- センサ・アクチュエータとのインタフェースを理解する
- 状態推定・パラメータチューニングを実装ベースで体験する
- FPGAやリアルタイム制御への発展的応用の方向性を掴む

---

## 🧩 主なトピック / Key Topics

| トピック | 内容 |
|----------|------|
| 制御理論のコード実装 | PID, LQR, Kalman などを Python / MATLAB で設計 |
| Python実装 | `control`, `scipy`, `numpy`, `matplotlib` による可視化 |
| 組込み連携 | Raspberry Pi, Arduino 等との簡易I/O制御 |
| ROS連携 | トピック/サービスを使った動的制御系との接続（入門） |
| FPGA制御入門 | RTLでのPID, FIR制御器の構成（概要） |
| Jupyter演習 | インタラクティブな可視化と学習ツール化

---

## 📂 サブフォルダ構成
```
part5_practical/
├── notebooks/      # Jupyterベースの演習教材
├── python/         # スクリプトベースの制御設計コード
├── ros/            # ROSベースの実験例（launch, pub/sub）
├── embedded/       # マイコンやRaspberry Piとの連携
├── fpga/           # Verilog/VHDLベース制御（設計例）
├── figures/        # 回路図、ブロック図、システム構成図
└── README.md
```
---

## 🛠️ 推奨ツール / Tools

- Python: `control`, `scipy`, `jupyter`, `matplotlib`, `pyserial`
- MATLAB / Simulink
- ROS2 (Foxglove, rqt_plot, turtlesim などで可視化)
- ハードウェア: Arduino, Raspberry Pi, DE10-Nano (FPGA)

---

## 🔗 関連資料

- ROS Tutorials: https://docs.ros.org/
- Python Control Library: https://python-control.readthedocs.io/
- Raspberry Pi GPIO: https://gpiozero.readthedocs.io/
- FPGA 制御実装例（Edusemi 特別編 第4章）

---

## 📌 備考

この章は「理論を現場に活かす」ための**接地的なアウトプット**を目指します。  
コードの精度よりも、実験と制御ループの全体像を捉えることが目的です。

---
