---
layout: default
title: 05. 安定余裕とロバスト性の評価
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

# 🛡️ 05. 安定余裕とロバスト性の評価

現実の制御系は、モデル誤差・外乱・遅延などによる不確かさを常に抱えています。安定性を保証しつつ、こうした変動に耐える性能 ― それが「ロバスト性」です。本節では、**ゲイン余裕・位相余裕** による定量評価法とその設計指針を学びます。

---

## 🎯 本節の学習目標

- 安定余裕（ゲイン余裕・位相余裕）の定義と算出法を理解する
- 安定余裕が実システムに与える意味を把握する
- ロバスト性と安定余裕の関係性を説明できる
- 仕様に基づいた設計改善の方向性を見出せる

---

## ⚖️ 安定余裕とは？

### ✅ 位相余裕（Phase Margin, PM）

ゲイン交差周波数 $\omega_g$ における位相の余裕：

$$
\text{PM} = 180^\circ + \angle G(j\omega_g)
$$

### ✅ ゲイン余裕（Gain Margin, GM）

位相交差周波数 $\omega_p$ におけるゲインの余裕：

$$
\text{GM} = \frac{1}{|G(j\omega_p)|} \quad \text{または} \quad -20 \log_{10} |G(j\omega_p)| [\mathrm{dB}]
$$

---

## 🧠 なぜ必要か？

- **モデルのズレや外乱**があっても安定を保つ必要がある
- 位相が予期せず回る／ゲインが増減する → 不安定の原因に
- **十分な余裕があると、ノイズやパラメータ変動に強くなる**

---

## 🎛️ 設計目安と実務値

| 指標 | 安定の目安 | 備考 |
|------|------------|------|
| 位相余裕 PM | $> 30^\circ$ | 45～60°が望ましい場合も |
| ゲイン余裕 GM | $> 6$ dB     | 10～20 dBが好まれる場合も |

---

## 🧪 周波数応答からの読み取り

### 手順（ボード線図）

1. ゲインプロットが0 dBになる点 $\omega_g$ を見つける  
2. その周波数における位相 → PMを計算  
3. 位相が $-180^\circ$ になる点 $\omega_p$ を見つける  
4. その周波数におけるゲイン → GMを計算  

### Python例（controlライブラリ）

```python
import control
from control.freqplot import margin

G = control.tf([1], [1, 2, 1])
gm, pm, wg, wp = margin(G)
print(f"Gain Margin: {gm}, Phase Margin: {pm}")
```

--- 

## 🔍 ロバスト性との関係

## ✅ ロバスト性とは？
- 不確かさや変動に対する安定性・性能維持の能力
- モデル誤差、パラメータ変動、外乱などへの耐性

安定余裕がロバスト性を担保する理由
- 大きなPM/GM → 安定の「バッファ」あり
- ノイズ・遅延・位相ずれ があっても発散しにくい

---

## 💡 設計改善のヒント
- PMが小さい → 位相補償器（リード補償）を追加
- GMが小さい → ゲインを抑える or フィルタ追加
- 両者が小さい → 制御器の構造見直し（PI → PIDなど）

---

## 📚 参考資料
- 森北出版「制御工学」
- Franklin et al., Feedback Control of Dynamic Systems
- Python: control.margin, bode_plot

---
