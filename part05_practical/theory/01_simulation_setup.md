
# ⚙️ 01. 制御シミュレーション環境のセットアップ（Simulation Environment Setup）

本節では、制御系の設計・実験を行うために必要な**Python制御環境の構築手順**を解説します。  
MATLAB環境の代替としても十分に活用できる、無料かつ高機能なツール群を導入します。

---

## 🧩 対象環境

| OS/プラットフォーム | 備考 |
|----------------------|------|
| Windows / macOS / Linux | Anaconda環境で統一可能 |
| Raspberry Pi / Jetson | 軽量Python制御可能（実装編で扱う） |
| VSCode + Terminal     | GUIでの制御編集・実行に推奨 |

---

## 🐍 推奨ツールセット

| ツール名 | 用途 | インストール方法 |
|----------|------|------------------|
| Python ≥ 3.9 | 制御ロジック・数値解析 | Anaconda推奨 |
| `numpy`, `scipy` | 線形代数・信号処理 | `pip install scipy` |
| `control` | 古典〜現代制御（Python制御理論） | `pip install control` |
| `matplotlib` | 可視化・グラフ描画 | `pip install matplotlib` |
| `jupyter` | ノートブック実験環境 | `pip install notebook` |

---

## 🛠️ 環境構築手順（Anaconda使用例）

### ① Anaconda環境の作成（初回のみ）

```bash
conda create -n control_env python=3.10
conda activate control_env
```

### ② 必要パッケージのインストール
pip install numpy scipy matplotlib control notebook

### ③ Jupyterノートブックの起動
jupyter notebook

または .ipynb を直接開く

## ✅ 動作確認コード例（テスト用）
```
import numpy as np
import matplotlib.pyplot as plt
import control

sys = control.tf([1], [1, 2, 1])  # 2次遅れ系
t, y = control.step_response(sys)

plt.plot(t, y)
plt.title("Step Response (Test)")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid()
plt.show()
```

---

## 🧠 補足：MATLABとの対応表（Python対照表）

| MATLAB関数       | Python対応関数（`control`ライブラリ） |
|------------------|----------------------------------------|
| `tf(num,den)`    | `control.tf(num, den)`                 |
| `ss(A,B,C,D)`    | `control.ss(A, B, C, D)`               |
| `step(sys)`      | `control.step_response(sys)`           |
| `impulse(sys)`   | `control.impulse_response(sys)`        |
| `bode(sys)`      | `control.bode(sys)`                    |
| `nyquist(sys)`   | `control.nyquist_plot(sys)`            |
| `margin(sys)`    | `control.margin(sys)`                  |
| `c2d(sys,Ts)`    | `control.sample_system(sys, Ts)`       |
| `feedback(G,K)`  | `control.feedback(G*K, 1)`             |
| `pole(sys)`      | `control.pole(sys)`                    |
| `zero(sys)`      | `control.zero(sys)`                    |

---

## 📚 参考リンク

- [Python Control Systems Library](https://python-control.readthedocs.io/)
- [SciPy Signal Processing Reference](https://docs.scipy.org/doc/scipy/reference/signal.html)
- [Anaconda Distribution（公式）](https://www.anaconda.com/products/distribution)
- [Jupyter Notebook 公式](https://jupyter.org/)

---











