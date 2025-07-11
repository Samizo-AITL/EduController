# 🔁 03. 逆モデル制御とニューラルネット（Inverse Model Control）

本章では、ニューラルネットワーク（NN）を用いて**制御対象の逆モデル**を学習し、  
得られたモデルをもとに**目標出力から必要な制御入力を推定する手法**を解説します。

---

## 🎯 学習目標 / Learning Objectives

- 逆モデル制御の基本概念と構成を理解する  
- NNによる逆モデルの学習と応用方法を学ぶ  
- 実験系での適用における課題と利点を整理する

---

## 🔄 1. 逆モデル制御とは

制御対象 $P$ の動作が $u(t) \rightarrow y(t)$ で表されるとき、  
**その逆関数** $P^{-1}$ をNNなどで学習し、目標出力 $y_d(t)$ を入力として制御入力 $u(t)$ を生成します。

$$
\begin{align*}
y(t) &= P(u(t)) \\
u(t) &= f_\theta(y_d(t), y(t), \dots) \approx P^{-1}(y_d)
\end{align*}
$$

---

## 🧠 2. 構成図と信号の流れ
```
[ y_d(t) ]  →  [ NN (逆モデル) ]  →  [ u(t) ]  →  [ Plant P ]  →  [ y(t) ]
↑                                 ↓
学習データ: (y_d, u)                 フィードバック
```
- NNは、過去の操作量・出力と目標から**必要な入力**を推定
- 教師信号は $u(t)$（操作入力）

---

## 🛠️ 3. 学習と適用

| 項目             | 内容                                           |
|------------------|------------------------------------------------|
| 入力特徴量       | $y_d(t)$, $y(t)$, 過去の $u(t-k)$ など          |
| 出力（教師信号） | $u(t)$：目標出力を得るための入力               |
| ネット構成       | MLPやLSTM（時系列考慮）、正則化が重要           |
| 学習方法         | MSE損失（$\|u_{\text{true}} - \hat{u}\|^2$）    |

---

## ✅ 利点と課題

### ✅ メリット

- モデルが取得できれば、**即時的な制御**が可能  
- 複雑なPIDチューニングが不要  
- 非線形性や時変性への柔軟な適応が可能

### ⚠️ 課題

- 逆関数が存在しない（非一意）な場合、精度が不安定  
- 学習に**大量の高品質データ**が必要  
- 安定性保証が難しく、外れ値や未知状態に弱い

---

## 🧪 実装例と実験（次章）

- `inverse_model_train.py`：逆モデルNNの訓練スクリプト  
- `ai_vs_pid_sim.py`：逆モデル制御 vs PID の比較実験  
- 実験対象：一次遅れ系 / 倒立振子 / モータ制御モデル

---

## 📚 参考資料

- Narendra & Parthasarathy (1990), “NNs for System Identification and Control”  
- Deep Inverse Models (DIM) in Adaptive Control  
- 本教材 `part06_nn_control/` 内のコード群

---
