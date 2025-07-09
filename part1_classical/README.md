# ⚙️ Part 1: 古典制御理論（Classical Control Theory）

本章では、制御理論の出発点である古典制御（時間領域と周波数領域）を学びます。  
PID制御・周波数応答・安定判別法を中心に、実践的な設計と調整手法を習得します。

---

## 🎯 学習目標 / Learning Objectives

- PID制御の基本構造と動作原理を理解する
- 過渡応答・定常偏差・安定性の評価法を学ぶ
- ボード線図・ナイキスト線図を用いた周波数解析を習得する
- ゲイン余裕・位相余裕から安定性を判断する
- Python や MATLAB による設計演習を行う

---

## 🧩 主なトピック / Key Topics

| トピック | 内容 |
|----------|------|
| PID制御 | 比例（P）・積分（I）・微分（D）の役割と調整 |
| 時間応答解析 | ステップ応答、立ち上がり時間、オーバーシュート |
| 周波数応答 | ボード線図・ナイキスト線図による安定性評価 |
| 安定性判別法 | Routh-Hurwitz, Nyquist Criterion |
| ゲイン/位相余裕 | ロバスト性評価の基本指標 |
| Python/MATLAB演習 | `control` モジュールを使った設計・描画 |

---

## 📂 サブフォルダ構成
```
part1_classical/
├── theory/         # 制御理論ノート（LaTeX or Markdown）
├── examples/       # 代表的な系（1次遅れ系, 2次遅れ系等）
├── python/         # Python演習コード（control/scipy）
├── matlab/         # MATLAB演習コード（任意）
├── figures/        # 使用する図（制御系構成、応答グラフ等）
└── README.md
```
---

## 🔧 推奨ツール / Tools

- Python: `control`, `scipy`, `matplotlib`, `numpy`
- MATLAB: `control system toolbox`
- Jupyter Notebook or VSCode for interactive learning

---

## 🔗 関連資料

- [Control Systems — Python Control Systems Library](https://python-control.readthedocs.io/)
- Ogata, K. “Modern Control Engineering”
- Dorf & Bishop, “Modern Control Systems”
- Edusemi-v4x 基礎編 第3章「フィードバックと安定性」

---

## 📌 備考

本章は後続の「状態空間制御」や「デジタル制御」の基盤になります。  
設計パラメータがどのように挙動に影響するか、**感覚的理解を得ることが目的**です。

---
