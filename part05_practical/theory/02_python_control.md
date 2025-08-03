# 🐍 02. Pythonによる制御設計の基本（Control System Design in Python）

本節では、Python制御ライブラリ（`control`, `scipy`）を用いた  
**基本的な制御系設計・解析手法**を学びます。  
MATLABと類似の操作性を持ち、古典〜状態空間まで幅広く対応できます。

---

## 🎯 学習目標

- Pythonで伝達関数・状態空間モデルを定義できる  
- ステップ応答・極配置・ボード線図などの解析ができる  
- 閉ループ制御系を構成し、応答を可視化できる  
- PythonとMATLABの構文的な違いに慣れる

---

## 🔁 1. 伝達関数の定義と応答解析

```python
import control
import matplotlib.pyplot as plt

# G(s) = 1 / (s^2 + 2s + 1)
num = [1]
den = [1, 2, 1]
G = control.tf(num, den)

# ステップ応答
t, y = control.step_response(G)
plt.plot(t, y)
plt.title("Step Response")
plt.grid()
plt.show()
```

---

## 🧮 2. 状態空間モデルの定義と解析

Pythonでは `control.ss()` 関数を使って状態空間表現（State-Space）を構成できます。

### 状態空間モデルの一般形

$$
\begin{aligned}
\dot{x}(t) &= A x(t) + B u(t) \\\\
y(t) &= C x(t) + D u(t)
\end{aligned}
$$

```python
import control

# モデル定義
A = [[0, 1],
     [-1, -2]]
B = [[0],
     [1]]
C = [[1, 0]]
D = [[0]]

sys_ss = control.ss(A, B, C, D)

# 固有値（極）の取得
poles = control.pole(sys_ss)
print("Poles:", poles)
```

	•	control.ss(A, B, C, D)：状態空間システムを定義
	•	control.pole(sys_ss)：固有値を算出 → 安定性を確認

---

## 🔁 3. フィードバック系の構成

制御系では、**負帰還構造**を用いて出力の安定化や誤差低減を実現します。  
Pythonでは `control.feedback()` を使って簡単に閉ループ系を構成できます。

### 例：比例ゲインによる閉ループ制御

対象プラント：

$$
G(s) = \frac{1}{s^2 + 2s + 1}
$$

制御器： $K=2$ の比例制御とする。

```python
import control
import matplotlib.pyplot as plt

# プラント（伝達関数）
G = control.tf([1], [1, 2, 1])
K = 2.0  # 比例ゲイン

# 負帰還系（閉ループ系）の構築
G_cl = control.feedback(K * G, 1)

# ステップ応答のプロット
t, y = control.step_response(G_cl)
plt.plot(t, y)
plt.title("Closed-loop Step Response")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid()
plt.show()
```

---

## 🔁 4. ボード線図と安定余裕の確認

周波数領域の特性は、制御系の安定性やロバスト性を評価する上で極めて重要です。  
Pythonでは `control.bode()` 関数で**ボード線図（振幅・位相）**を描画できます。

### Bode線図とは？

- **ゲイン特性**（振幅 vs 周波数）
- **位相特性**（位相 vs 周波数）

これらを対数スケールで描くことで、**フィルタ特性・位相遅れ・安定余裕**が視覚的に把握できます。

---

### ✅ PythonによるBode線図の描画

```python
import control
import matplotlib.pyplot as plt

# 伝達関数 G(s)
G = control.tf([1], [1, 2, 1])

# Bodeプロット（dB表記、Hzスケール）
mag, phase, omega = control.bode(G, dB=True, Hz=True)
plt.show()
```

---

### 📏 安定余裕の算出

`control.margin()` を使えば、以下の情報を数値として取得できます：

- **ゲイン余裕（Gain Margin）**：利得が何倍まで増加しても安定か（dBで表記）
- **位相余裕（Phase Margin）**：何度の位相遅れまで許容されるか（deg）
- **ゲイン交差周波数（Gain crossover frequency）**：|G(jω)| = 1（0dB）となる周波数
- **位相交差周波数（Phase crossover frequency）**：∠G(jω) = -180°となる周波数

```python
import control

G = control.tf([1], [1, 2, 1])
gm, pm, wg, wp = control.margin(G)

print(f"Gain Margin  : {gm:.2f}")
print(f"Phase Margin : {pm:.2f} deg")
print(f"Gain Crossover Freq : {wg:.2f} rad/s")
print(f"Phase Crossover Freq: {wp:.2f} rad/s")
```
この情報をもとに、安定性の余裕と応答のロバスト性を評価できます。

---

### ⚠️ 安定余裕の設計基準（目安）

制御系の設計では、ゲイン余裕（GM）や位相余裕（PM）を**ある程度確保**しておくことで、  
モデル誤差・ノイズ・遅延などに対して**ロバストな安定性**が得られます。

| 指標              | 推奨範囲         | 説明                                      |
|-------------------|------------------|-------------------------------------------|
| ゲイン余裕 (GM)   | ≧ 6 dB           | ゲインが6 dB増加しても不安定化しない     |
| 位相余裕 (PM)     | ≧ 30〜45 度      | 遅延や近似誤差に対する余裕がある          |
| クロス周波数       | 数 Hz〜数 kHz     | 応答速度の指標（高すぎるとノイズに弱い） |

> ⚠️ **注意**：高い応答性（速さ）を求めすぎると、位相余裕が不足して**振動**や**発散**を引き起こすことがあります。

---

## 📘 まとめ

| 機能                    | Python関数                             |
|-------------------------|----------------------------------------|
| Bode線図の描画          | `control.bode(sys)`                    |
| 安定余裕の数値取得      | `gm, pm, wg, wp = control.margin(sys)` |
| ゲイン交差周波数の取得  | `wg`                                   |
| 位相交差周波数の取得    | `wp`                                   |

安定余裕は、**制御対象が未知成分を含む場合**や**制御器設計の初期検証段階**で特に重要です。

---

## 📚 参考資料

- [Python Control Systems Library Documentation](https://python-control.readthedocs.io/)
- Franklin, Powell & Emami-Naeini, *Feedback Control of Dynamic Systems*
- Nise, *Control Systems Engineering*
- MATLAB Control Toolbox との比較：`02_simulation_setup.md` 参照

---





　

