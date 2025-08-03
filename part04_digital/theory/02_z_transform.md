---
layout: default
title: 02. Z変換と離散時間制御系（Z-Transform & Discrete Control Representation）
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

# 🔁 02. Z変換と離散時間制御系（Z-Transform & Discrete Control Representation）

ディジタル制御では、連続系のラプラス変換に対応する離散時間の変換手法として  
**Z変換**を用います。これは**差分方程式を伝達関数的に表現**するための基本です。

---

## 🎯 学習目標

- Z変換の基本的な定義と性質を理解する  
- 離散系伝達関数 $G(z)$ の導出と意味を把握する  
- 極・零点・安定性の概念をZ領域で理解できる  
- 離散系と連続系の比較ができる

---

## 📐 Z変換の定義

離散信号 $x[k]$ に対して、Z変換は以下のように定義されます：

$$
X(z) = \mathcal{Z}\{x[k]\} = \sum_{k=0}^\infty x[k] z^{-k}
$$

- $z$ は複素数変数（ $z = re^{j\omega}$ ）  
- $z^{-1}$ は1ステップの遅れに相当： $x[k-1] = z^{-1}x[k]$

---

## 🔁 Z変換の基本性質

| 性質 | 内容 |
|------|------|
| 線形性 | $\mathcal{Z}\{ax[k] + by[k]\} = aX(z) + bY(z)$ |
| 時間シフト | $\mathcal{Z}\{x[k-n]\} = z^{-n}X(z)$ |
| 畳み込み定理 | $x[k] * h[k] \leftrightarrow X(z)H(z)$ |

---

## 🏗️ 離散時間伝達関数

- 連続系： $G(s) = \frac{Y(s)}{U(s)}$  
- 離散系： $G(z) = \frac{Y(z)}{U(z)}$

$$
G(z) = \frac{b_0 + b_1 z^{-1} + \dots + b_m z^{-m}}{1 + a_1 z^{-1} + \dots + a_n z^{-n}}
$$

- 差分方程式のZ変換から得られる

---

## ⚙️ 離散化（Tustin法など）

連続系から離散系へ変換する代表例：

### Tustin（双一次変換）

$$
s = \frac{2}{T_s} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}
$$

- 安定性・周波数特性の維持に優れる

### ゼロ次ホールド（ZOH）変換

- ラプラス変換 $G(s)$ からZ変換 $G(z)$ を直接求める手法
- MATLABでは `c2d()` 関数で変換可能

---

## 🧩 安定性判定（Z平面）

- 離散系では「**すべての極が単位円内にある**」ときに安定：

$$
|z_i| < 1 \quad \text{for all } i
$$

- $|z|=1$：限界安定（振動）
- $|z|>1$：不安定

---

## 🧪 Z変換の活用例（次章以降）

- PID制御器をZ領域で表現  
- フィルタ設計（FIR/IIR）の伝達関数構築  
- FFT解析など離散信号処理との融合

---

## 📚 参考資料

- Ogata, *Discrete-Time Control Systems*  
- Kuo, *Digital Control Systems*  
- MATLAB `c2d()` / `d2c()` 関数ドキュメント

---
