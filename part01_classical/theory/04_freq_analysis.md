---
layout: default
title: 04. 周波数応答とボード線図の基礎
---

<!-- MathJax support for both inline and block math -->
<script type="text/javascript">
  window.MathJax = {
    tex: { inlineMath: [['$', '$'], ['\\(', '\\)']] },
    svg: { fontCache: 'global' }
  };
</script>
<script type="text/javascript"
  async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

# 📉 04. 周波数応答とボード線図の基礎

ボード線図（Bode plot）は、制御系の周波数応答特性を視覚的に評価するための基本的なツールです。本節では、ボード線図の読み方・描き方、およびゲイン交差周波数・位相余裕と安定性との関係について学びます。

---

## 🎯 本節の学習目標

- 周波数応答とは何かを理解する
- ボード線図の読み方と構成要素（ゲイン、位相）を把握する
- ゲイン交差周波数・位相余裕の意味を説明できる
- 安定性とロバスト性の観点から周波数特性を評価できる

---

## 🎧 周波数応答とは？

システム $G(s)$ において、$s = j\omega$ と置くことで**周波数応答**が得られます：

$$
G(j\omega) = |G(j\omega)| \angle \arg(G(j\omega))
$$

- **振幅特性（ゲイン）**：入力信号の大きさに対する出力の大きさ
- **位相特性**：入力と出力の間の遅れ（位相差）

---

## 📊 ボード線図（Bode Plot）の構成

- **横軸**：周波数（対数スケール, [rad/s]）
- **縦軸（上）**：ゲイン（dB）→ $20 \log_{10} |G(j\omega)|$
- **縦軸（下）**：位相（degree）→ $\arg G(j\omega)$

ボード線図は、周波数特性を2つのプロット（ゲイン・位相）に分けて表示する形式です。

---

## 🧠 重要な周波数点と概念

### ✅ ゲイン交差周波数 $\omega_g$

- ゲイン $|G(j\omega)| = 1$（0 dB）となる周波数

### ✅ 位相交差周波数 $\omega_p$

- 位相 $\angle G(j\omega) = -180^\circ$ となる周波数

---

## 🛡️ 安定性とロバスト性

### 位相余裕（Phase Margin, PM）

$$
\text{PM} = 180^\circ + \angle G(j\omega_g)
$$

- ゲイン交差周波数における位相の余裕

### ゲイン余裕（Gain Margin, GM）

$$
\text{GM} = \frac{1}{|G(j\omega_p)|} \quad \text{または} \quad -20\log_{10}|G(j\omega_p)|
$$

- 位相交差周波数におけるゲインの余裕

### ✅ 経験則（目安）

- 位相余裕：$> 30^\circ$  
- ゲイン余裕：$> 6$ dB  

---

## 🔧 典型的な応答の例

| 要素         | ゲイン傾き | 位相変化 |
|--------------|------------|----------|
| 積分器 $1/s$ | -20 dB/dec | -90°     |
| 微分器 $s$   | +20 dB/dec | +90°     |
| 一次遅れ     | -20 dB/dec | -90°（漸近） |
| 二次遅れ     | -40 dB/dec | -180°（漸近） |

---

## 🧪 Pythonでの可視化例

```python
import control
import matplotlib.pyplot as plt

G = control.tf([1], [1, 2, 1])  # 二次遅れ系など
control.bode_plot(G, dB=True, Hz=False, deg=True)
plt.show()
```

- control.bode_plot：ゲイン・位相を一括描画
- matplotlibとの連携で図の調整・保存が可能

出力例は /figures/bode_example.png を参照。

---

## 📚 参考資料
- 森北出版「制御工学」
- Franklin et al., Feedback Control of Dynamic Systems
- Python: control, matplotlib

---
