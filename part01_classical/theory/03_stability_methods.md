---
layout: default
title: 03. 安定性判別法（Routh, 根軌跡, ナイキスト）
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

# 🧮 03. 安定性判別法（Routh, 根軌跡, ナイキスト）

制御系の最も基本的な要件は「安定であること」です。本節では、古典制御理論における安定性の定義と、主要な判別法である **Routh-Hurwitz判別法**, **根軌跡法（Root Locus）**, **ナイキスト法（Nyquist）** を学びます。

---

## 🎯 本節の学習目標

- 安定性の定義と必要条件を理解する
- Routh表による安定性判別を手計算できる
- 根軌跡法による安定判定と極配置の概念を理解する
- ナイキスト線図と周波数応答による安定性評価を習得する

---

## 📌 安定性の定義

制御系が安定であるとは、**すべての閉ループ極が左半平面にある**ことを意味します。

- **連続系**：すべての極の実部が負
- **離散系**：すべての極が単位円内

---

## 🔢 Routh-Hurwitz判別法

伝達関数：

$$
G(s) = \frac{N(s)}{D(s)} = \frac{b_ms^m + \cdots + b_0}{a_ns^n + \cdots + a_0}
$$

安定性は $D(s)$ の根（極）に依存します。**Routh表**を用いて、**正の実部を持つ根が存在するかを判定**します。

### 手順（例：4次系）

1. 係数を使って1列目を作成  
2. 順次、補間して表を構成  
3. 1列目の符号変化の回数 = 不安定極の数

✅ **すべての1列目が正 → 安定**

（表の例は紙面またはPDF用で図示）

---

## 📈 根軌跡法（Root Locus）

**極の位置変化を視覚的に追跡する方法**

開ループ伝達関数：

$$
G(s)H(s) = \frac{K \cdot N(s)}{D(s)}
$$

- ゲイン $K$ を変化させたときの**閉ループ極の軌跡**を表示
- 安定領域、減衰比、応答速度の変化を視覚的に把握可能

### 特徴

- 左半平面 → 安定
- 軌跡の右側 → 不安定
- PID設計・極配置の指針になる

---

## 🌀 ナイキスト判別法

**周波数応答を用いた安定性評価手法**

- 閉ループ系の安定性を**開ループ周波数応答**から評価可能
- Nyquist線図が点 $-1+j0$ を**何回・どの方向に囲むか**を見る

### 判別ルール（補足：$N = Z - P$）

- $P$：右半平面にある開ループ極の数
- $Z$：右半平面にある閉ループ極の数
- $N$：$-1$ 点を囲んだ回数（反時計回りを正）

✅ **$Z = 0$ → 安定**

---

## 🛠️ 各手法の比較

| 判別法 | 利点 | 注意点 |
|--------|------|--------|
| Routh-Hurwitz | 計算簡単・定量的 | 高次になると表が複雑 |
| 根軌跡法       | 可視化しやすい | モデルに依存・設計に応用 |
| ナイキスト法   | 周波数特性で可能 | 周波数応答取得が必要 |

---

## 🧪 Python実装例

- Routh表：数式処理 or 自作関数による計算  
- 根軌跡法：`control.root_locus()`  
- ナイキスト線図：`control.nyquist_plot()`

※ 詳細は `/simulation/stability_methods.py` を参照

---

## 📚 参考資料

- 「制御工学入門」森北出版  
- Franklin et al., *Feedback Control of Dynamic Systems*  
- Python: `control`, `sympy`, `matplotlib`

---
