---
layout: default
title: "🐍 02. Pythonによる制御設計の基本（Control System Design in Python）"
permalink: /part05_practical/theory/02_python_control.html
---

---

# 🐍 02. Pythonによる制御設計の基本（Control System Design in Python）

> ℹ️ **Webで数式が正しく表示されない場合はこちら** → [GitHub版を見る](https://github.com/Samizo-AITL/EduController/blob/main/part05_practical/theory/02_python_control.md)

---

本節では、Python制御ライブラリ（`control`, `scipy`）を用いた  
**基本的な制御系設計・解析手法**を学びます。  
MATLABと類似の操作性を持ち、古典〜状態空間まで幅広く対応できます。

This section covers **basic control system design and analysis** using Python libraries (`control`, `scipy`),  
providing MATLAB-like operability and supporting a wide range from classical to state-space methods.

---

## 🎯 学習目標 / Learning Objectives

- Pythonで伝達関数・状態空間モデルを定義できる  
- ステップ応答・極配置・ボード線図などの解析ができる  
- 閉ループ制御系を構成し、応答を可視化できる  
- PythonとMATLABの構文的な違いに慣れる  

---

## 🔁 1. 伝達関数の定義と応答解析 / Transfer Function Definition & Response

```python
import control
import matplotlib.pyplot as plt

# G(s) = 1 / (s^2 + 2s + 1)
num = [1]
den = [1, 2, 1]
G = control.tf(num, den)

# ステップ応答 / Step Response
t, y = control.step_response(G)
plt.plot(t, y)
plt.title("Step Response")
plt.grid()
plt.show()
```

---

## 🧮 2. 状態空間モデルの定義と解析 / State-Space Model

Pythonでは `control.ss()` 関数を使って状態空間表現を構成できます。

### 一般形 / General Form
$$
\dot{x}(t) = A x(t) + B u(t) \\
y(t) = C x(t) + D u(t)
$$

```python
import control

A = [[0, 1],
     [-1, -2]]
B = [[0],
     [1]]
C = [[1, 0]]
D = [[0]]

sys_ss = control.ss(A, B, C, D)

# 固有値（極）の取得 / Get poles
poles = control.pole(sys_ss)
print("Poles:", poles)
```
- `control.ss(A, B, C, D)`：状態空間システムを定義  
- `control.pole(sys_ss)`：固有値を算出 → 安定性を確認  

---

## 🔁 3. フィードバック系の構成 / Feedback System

閉ループ構造（負帰還）により安定化や誤差低減を実現できます。

### 例：比例ゲインによる閉ループ制御 / Example: Proportional Control

プラント：
$$
G(s) = \frac{1}{s^2 + 2s + 1}
$$
比例ゲイン： $K=2$

```python
import control
import matplotlib.pyplot as plt

G = control.tf([1], [1, 2, 1])
K = 2.0

G_cl = control.feedback(K * G, 1)

t, y = control.step_response(G_cl)
plt.plot(t, y)
plt.title("Closed-loop Step Response")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid()
plt.show()
```

---

## 🔁 4. ボード線図と安定余裕 / Bode Plot & Stability Margins

周波数特性を評価することで、安定性やロバスト性を確認できます。

```python
import control
import matplotlib.pyplot as plt

G = control.tf([1], [1, 2, 1])
mag, phase, omega = control.bode(G, dB=True, Hz=True)
plt.show()
```

### 安定余裕の取得 / Get Stability Margins
```python
gm, pm, wg, wp = control.margin(G)

print(f"Gain Margin  : {gm:.2f}")
print(f"Phase Margin : {pm:.2f} deg")
print(f"Gain Crossover Freq : {wg:.2f} rad/s")
print(f"Phase Crossover Freq: {wp:.2f} rad/s")
```

| 指標 / Metric     | 推奨範囲 / Recommended | 説明 / Description |
|------------------|------------------------|--------------------|
| GM (Gain Margin) | ≧ 6 dB                 | ゲイン増加に対する安定余裕 |
| PM (Phase Margin)| ≧ 30〜45°               | 遅延や近似誤差に対する余裕 |
| クロス周波数      | 数 Hz〜数 kHz            | 応答速度の指標 |

---

## 📘 まとめ / Summary

| 機能 / Feature            | Python関数 |
|---------------------------|------------|
| 伝達関数作成               | `control.tf()` |
| 状態空間作成               | `control.ss()` |
| ステップ応答               | `control.step_response()` |
| ボード線図                 | `control.bode()` |
| 安定余裕                   | `control.margin()` |

---

## 📚 参考 / References

- [Python Control Systems Library](https://python-control.readthedocs.io/)  
- Franklin, Powell & Emami-Naeini, *Feedback Control of Dynamic Systems*  
- Nise, *Control Systems Engineering*  

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part05_practical/theory/01_simulation_setup.html)**  
Python制御環境の構築手順を解説。  
Explains how to set up the Python control environment.

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part05_practical/theory/03_embedded_control.html)**  
マイコン向け制御展開について解説。  
Explains control deployment on microcontrollers.

**🏠 [第5章トップ / Back to Part 5 Top](https://samizo-aitl.github.io/EduController/part05_practical/)**
