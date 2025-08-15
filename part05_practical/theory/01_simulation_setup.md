---
layout: clean
title: "⚙️ 01. 制御シミュレーション環境のセットアップ（Simulation Environment Setup）"
permalink: /part05_practical/theory/01_simulation_setup.html
---

---

# ⚙️ 01. 制御シミュレーション環境のセットアップ（Simulation Environment Setup）

> ℹ️ **Webで数式が正しく表示されない場合はこちら** → [GitHub版を見る](https://github.com/Samizo-AITL/EduController/blob/main/part05_practical/theory/01_simulation_setup.md)

---

本節では、制御系の設計・実験を行うための **Python制御環境の構築手順** を解説します。  
MATLAB環境の代替としても十分活用できる、無料かつ高機能なツール群を導入します。

This section explains how to **set up a Python control environment** for designing and experimenting with control systems, providing a free and powerful alternative to MATLAB.

---

## 🧩 対象環境 / Target Platforms

| OS / Platform         | 備考 / Note |
|-----------------------|-------------|
| Windows / macOS / Linux | Anaconda環境で統一可能 / Unified with Anaconda |
| Raspberry Pi / Jetson | 軽量Python制御可能（実装編で扱う） / Lightweight Python control possible |
| VSCode + Terminal     | GUIでの編集・実行に推奨 / Recommended for GUI-based editing & execution |

---

## 🐍 推奨ツールセット / Recommended Toolset

| ツール / Tool | 用途 / Purpose | インストール方法 / Install Method |
|---------------|----------------|-----------------------------------|
| Python ≥ 3.9  | 制御ロジック・数値解析 / Control logic & numerical analysis | Anaconda推奨 / Use Anaconda |
| `numpy`, `scipy` | 線形代数・信号処理 / Linear algebra & signal processing | `pip install scipy` |
| `control`     | 古典〜現代制御（Python制御理論） / Classical to modern control theory | `pip install control` |
| `matplotlib`  | 可視化・グラフ描画 / Visualization & plotting | `pip install matplotlib` |
| `jupyter`     | ノートブック実験環境 / Notebook-based experiments | `pip install notebook` |

---

## 🛠️ 環境構築手順（Anaconda使用例） / Setup Procedure (Anaconda)

### ① 仮想環境の作成（初回のみ） / Create a Virtual Environment
```bash
conda create -n control_env python=3.10
conda activate control_env
```

### ② 必要パッケージのインストール / Install Required Packages
```bash
pip install numpy scipy matplotlib control notebook
```

### ③ Jupyterノートブックの起動 / Launch Jupyter Notebook
```bash
jupyter notebook
```
または `.ipynb` ファイルを直接開く / Or open `.ipynb` directly.

---

## ✅ 動作確認コード例（テスト用） / Test Script Example
```python
import numpy as np
import matplotlib.pyplot as plt
import control

sys = control.tf([1], [1, 2, 1])  # 2次遅れ系 / Second-order system
t, y = control.step_response(sys)

plt.plot(t, y)
plt.title("Step Response (Test)")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid()
plt.show()
```

---

## 🧠 MATLABとの対応表 / MATLAB–Python Function Mapping

| MATLAB関数 / MATLAB Function | Python (`control`ライブラリ) |
|------------------------------|------------------------------|
| `tf(num,den)`    | `control.tf(num, den)` |
| `ss(A,B,C,D)`    | `control.ss(A, B, C, D)` |
| `step(sys)`      | `control.step_response(sys)` |
| `impulse(sys)`   | `control.impulse_response(sys)` |
| `bode(sys)`      | `control.bode(sys)` |
| `nyquist(sys)`   | `control.nyquist_plot(sys)` |
| `margin(sys)`    | `control.margin(sys)` |
| `c2d(sys,Ts)`    | `control.sample_system(sys, Ts)` |
| `feedback(G,K)`  | `control.feedback(G*K, 1)` |
| `pole(sys)`      | `control.pole(sys)` |
| `zero(sys)`      | `control.zero(sys)` |

---

## 📚 参考リンク / References

- [Python Control Systems Library](https://python-control.readthedocs.io/)  
- [SciPy Signal Processing Reference](https://docs.scipy.org/doc/scipy/reference/signal.html)  
- [Anaconda Distribution](https://www.anaconda.com/products/distribution)  
- [Jupyter Notebook](https://jupyter.org/)

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part05_practical/)**  
Part 5 の概要説明と章構成を参照。  
See Part 5 overview and chapter structure.

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part05_practical/theory/02_python_control.html)**  
Pythonによる制御実装の方法を解説。  
Explains how to implement control design in Python.

**🏠 [第5章トップ / Back to Part 5 Top](https://samizo-aitl.github.io/EduController/part05_practical/)**
