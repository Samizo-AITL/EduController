---
layout: default
title: 03. 離散PID制御の設計（Digital PID Controller Design）
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

# 🧮 03. 離散PID制御の設計（Digital PID Controller Design）

PID制御器はディジタル制御においても依然として主流のアルゴリズムです。  
この章では、**連続時間のPIDをZ変換**により**離散時間制御器へ変換**する方法を扱います。

---

## 🎯 学習目標

- PID制御器の離散化方法を理解する  
- 前進差分、後退差分、Tustin法の違いを比較できる  
- Pythonで離散PIDを実装し、応答を観察できる  
- 離散化による遅延・量子化の影響を認識できる

---

## 🔁 連続PID制御器の構造

$$
u(t) = K_p e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}
$$

- $K_p$：比例ゲイン、$K_i$：積分ゲイン、$K_d$：微分ゲイン  
- この制御則を**差分方程式に変換**して離散時間で実装する

---

## 🔀 離散化手法の比較

### ① 前進差分（Forward Euler）

- 微分：$\frac{de(t)}{dt} \approx \frac{e[k+1] - e[k]}{T_s}$
- 積分：$\int e(t)\,dt \approx \sum e[k] T_s$

### ② 後退差分（Backward Euler）

- 微分： $\frac{e[k] - e[k-1]}{T_s}$  
- 積分： $I[k] = I[k-1] + e[k] T_s$

### ③ 双一次変換（Tustin法）

- より安定性・周波数応答を保つ変換  
- ラプラス領域の $s$ を Z変換：

$$
s \approx \frac{2}{T_s} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}
$$

---

## 🧮 離散PIDの実装例（Tustin法）

$$
G_c(z) = K_p + K_i \cdot \frac{T_s}{2} \cdot \frac{1 + z^{-1}}{1 - z^{-1}} + K_d \cdot \frac{2}{T_s} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}
$$

- 上記は Z 領域での PID 制御器  
- 差分方程式に変換し、逐次計算で実装可能

---

## 🧪 Pythonでの実験（次章：`digital_pid.py`）

- 同一プラント（1次系 or 2次系）に対し：
  - 連続PID vs 離散PID（Tustin）
- サンプリング周期やゲインによる挙動の違いを観察
- 離散化による遅れ、微分ノイズの影響を評価

---

## 🧠 実装上の注意点

| 要素 | 注意事項 |
|------|----------|
| 積分項 | ワインドアップ防止が必要 |
| 微分項 | 雑音増幅を防ぐため、微分先行型 or LPF 併用 |
| サンプリング周期 | 遅すぎると安定性低下、速すぎると計算負荷 |

---

## 📚 参考資料

- Astrom & Hagglund, *PID Controllers: Theory, Design, and Tuning*  
- Ogata, *Discrete-Time Control Systems*  
- MATLAB `pid()` / `pidTuner` ツール

---
