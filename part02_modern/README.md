# 🧠 Part 2: 現代制御理論（Modern Control Theory）

本章では、状態空間モデルを用いた現代制御理論を学びます。  
可制御性・可観測性を土台に、LQR、カルマンフィルタ、H∞制御などの先進的制御手法を扱います。

---

## 🎯 学習目標 / Learning Objectives

- 状態空間表現の構成と意味を理解する
- 可制御性・可観測性の定義と判定方法を習得する
- 最適制御理論（LQR）とその導出法を理解する
- カルマンフィルタによる状態推定の基本原理を学ぶ
- H∞制御の基礎概念とロバスト性設計の考え方をつかむ
- Python や MATLAB による実装を体験する

---

## 🧩 主なトピック / Key Topics

| トピック | 内容 |
|----------|------|
| 状態空間表現 | A, B, C, D行列によるシステムモデル化 |
| 可制御性・可観測性 | Kalman判定法、構造的理解 |
| LQR制御 | 二次性能指標に基づく最適状態フィードバック |
| カルマンフィルタ | ノイズ下の状態推定とベイズ推定の実装 |
| H∞制御（入門） | ロバスト制御の考え方と基礎設計 |
| Python/MATLAB演習 | `control`, `scipy.signal`, `numpy.linalg` などでの実装

---

## 📂 サブフォルダ構成
```
part2_modern/
├── theory/         # 状態空間と最適制御の理論資料
├── examples/       # システムモデル（倒立振子、車両モデル等）
├── python/         # Pythonによる制御設計
├── matlab/         # MATLAB演習（LQR, カルマン等）
├── figures/        # 状態遷移図、性能評価などの図
└── README.md
```
---

## 🛠️ 推奨ツール / Tools

- Python: `control`, `scipy.linalg`, `matplotlib`, `sympy`
- MATLAB: `Control System Toolbox`, `Robust Control Toolbox`
- 可視化: `plotly`, `graphviz`（構造図の描画）

---

## 🔗 関連資料

- Bryson & Ho, “Applied Optimal Control”
- Zhou, Doyle, Glover, “Robust and Optimal Control”
- Python Control Library: https://python-control.readthedocs.io/
- Edusemi 応用編「LQR制御と状態空間設計」

---

## 📌 備考

本章では「システムの内面（状態）」を扱うことで、観測や最適化の重要性が見えてきます。  
**古典制御が“外部から操作”するのに対し、現代制御は“内部状態を操作”する制御です。**

---
