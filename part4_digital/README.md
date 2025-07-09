# 💻 Part 4: デジタル制御と信号処理（Digital Control & Signal Processing）

本章では、離散時間領域での制御設計や信号処理を扱います。  
サンプリング理論、Z変換、ディジタルPID設計、FIR/IIRフィルタ、FFTなど、  
実装を意識したデジタル制御設計の基礎を学びます。

---

## 🎯 学習目標 / Learning Objectives

- 連続系と離散系の違いを理解し、サンプリングの基本を学ぶ
- Z変換による離散時間系の記述と安定性解析を行う
- 離散PID制御の設計法を理解し、シミュレーションできる
- FIR/IIR フィルタの設計と特性を把握する
- FFTを使った信号の周波数解析・雑音除去を体験する
- 実際のディジタル制御設計プロセスを一通り実施する

---

## 🧩 主なトピック / Key Topics

| トピック | 内容 |
|----------|------|
| 離散時間システム | サンプリング、ZOH、ディジタルモデル化 |
| Z変換と極配置 | 離散系安定性、設計視点の違い |
| 離散PID制御 | 前進差分/後退差分法によるディジタル制御設計 |
| フィルタ設計 | FIR/IIRの原理と実装（scipy.signalなど） |
| FFT解析 | 時系列信号のスペクトル可視化と処理 |
| Python演習 | `scipy.signal`, `numpy.fft`, `control` などの応用

---

## 📂 サブフォルダ構成
```
part4_digital/
├── theory/         # 離散制御・DSPに関する解説資料
├── examples/       # 離散化対象系、信号例
├── python/         # Pythonコード（Z変換、PID、FFT等）
├── matlab/         # MATLAB/Simulinkによる離散制御演習
├── figures/        # サンプリング図、Bode応答、スペクトル図など
└── README.md
```
---

## 🛠️ 推奨ツール / Tools

- Python: `scipy.signal`, `numpy.fft`, `matplotlib`, `control`
- MATLAB: 離散制御設計機能 + DSP System Toolbox
- シミュレーション：Jupyter Notebook、MATLAB Live Script

---

## 🔗 関連資料

- Franklin, Powell, Emami-Naeini, “Digital Control of Dynamic Systems”
- Oppenheim & Schafer, “Discrete-Time Signal Processing”
- Python SciPy Signal Documentation: https://docs.scipy.org/doc/scipy/reference/signal.html

---

## 📌 備考

本章では、アナログからディジタルへと移る際の考え方の違いを明確にし、  
**実装可能な制御理論と信号処理の橋渡し**を行います。

---
