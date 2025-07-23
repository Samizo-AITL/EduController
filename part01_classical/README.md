# ⚙️ Part 1: 古典制御理論（Classical Control Theory）

本章では、PID制御を中心とした古典制御理論を扱い、時間領域および周波数領域での応答解析・設計法を体系的に学びます。制御の基本構造から、安定性・ロバスト性までを段階的に理解し、Pythonによる可視化・シミュレーションを通じて実装感覚も身につけます。

---

## 🧭 構成（章別教材）

| No | 章タイトル | 内容概要 |
|----|------------|----------|
| 01 | [PID制御の基礎](theory/01_pid_control.md) | PID各成分の働き、ブロック線図、伝達関数の理解 |
| 02 | [過渡応答と定常偏差](theory/02_transient_response.md) | ステップ応答、時間定数、定常偏差の評価法 |
| 03 | [安定性判別法](theory/03_stability_methods.md) | Routh判別、根軌跡、ナイキスト法による安定判定 |
| 04 | [周波数応答とボード線図](theory/04_freq_analysis.md) | ゲイン・位相プロット、交差周波数、周波数特性 |
| 05 | [安定余裕とロバスト性](theory/05_gain_margin.md) | ゲイン余裕・位相余裕によるロバスト性評価 |

---

## 🧪 実行スクリプト

| ファイル | 内容 |
|---------|------|
| [`pid_simulation.py`](simulation/pid_simulation.py) | PID制御とステップ応答の比較 |
| [`transient_response.py`](simulation/transient_response.py) | 1次・2次遅れ系の応答描画 |
| [`stability_methods.py`](simulation/stability_methods.py) | Routh表, 根軌跡, ナイキスト線図 |
| [`bode_plot.py`](simulation/bode_plot.py) | ボード線図の自動描画 |
| [`gain_margin.py`](simulation/gain_margin.py) | PM/GMの自動計算と可視化 |

---

## 📓 Jupyterノートブック（補助教材）

| ノートブック | 内容 |
|-------------|------|
| [`pm_gm_analysis.ipynb`](notebooks/pm_gm_analysis.ipynb) | PM/GMの計算とボード線図描画（対話形式） |
| [`pid_design.ipynb`](notebooks/pid_design.ipynb) | PIDゲインと応答の関係（予定） |

---

## 🖼️ 教材図・グラフ（figures/）

| 図ファイル | 内容 |
|------------|------|
| `pid_block_diagram.png` | PID制御のブロック線図 |
| `step_response.png` | 各PID構成による応答比較 |
| `bode_example.png` | 周波数応答のボード線図 |
| `nyquist_example.png` | ナイキスト線図例 |
| `phase_gain_margin_example.png` | PM/GMの可視化付きボード線図 |

---

## ⚙️ 実行環境・依存ライブラリ

```bash
pip install control matplotlib numpy
```

- Python 3.8〜3.12 で動作確認済み
- 推奨エディタ：VSCode / Jupyter Lab / Google Colab

---

## 🧠 学習目標のまとめ
- PID制御の動作理解とゲイン調整
- 過渡応答・定常偏差の評価
- 安定性判定（Routh/RootLocus/Nyquist）
- 周波数応答とPM/GMによるロバスト設計

---

## 📚 参考資料
- 「制御工学入門」森北出版
- Feedback Control of Dynamic Systems – Franklin et al.
- Pythonライブラリ：control, matplotlib, numpy

---




