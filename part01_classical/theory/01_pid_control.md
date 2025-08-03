# 🧩 01. PID制御の基礎  
## 🧩 01. Introduction to PID Control

PID（比例・積分・微分）制御は、最も基本的かつ広く使われているフィードバック制御の一種です。本節では、PID制御の原理とそれぞれの要素が制御系に与える影響を理解し、動作と設計の基本を習得します。  
PID (Proportional-Integral-Derivative) control is a widely used feedback control method. This section explains the principles and effects of each term and introduces basic design techniques.

---

## 🎯 本節の学習目標｜Learning Objectives

- PID制御の各成分（P, I, D）の働きを理解する  
- 各成分が応答に与える影響（速度・安定性・誤差）を説明できる  
- ブロック線図と伝達関数による表現ができる  
- Python/MATLABでステップ応答を確認できる  

---

## ⚙️ PID制御とは？｜What is PID Control?

PID制御は、以下のように制御量 $u(t)$ を定義します：

$$
u(t) = K_P e(t) + K_I \int_0^t e(\tau)\,d\tau + K_D \frac{de(t)}{dt}
$$

- $e(t)$：目標値と現在値の偏差（誤差）  
- $K_P$：比例ゲイン (Proportional gain)  
- $K_I$：積分ゲイン (Integral gain)  
- $K_D$：微分ゲイン (Derivative gain)

---

## 🧠 各成分の役割と影響｜Roles of P, I, D

| 成分 | 名称 | 働き | 効果 |
|------|------|------|------|
| P    | 比例 (Proportional) | 誤差に比例した出力 | 応答速度向上、過大だと振動の原因に |
| I    | 積分 (Integral) | 過去の誤差を累積 | 定常偏差の除去、過剰で遅れが大きくなる |
| D    | 微分 (Derivative) | 誤差の変化率に応答 | 応答を滑らかに、ノイズに敏感 |

---

## 🔧 ブロック線図と伝達関数｜Block Diagram and Transfer Function

### ▶ ブロック線図（例）｜Example Block Diagram

![PID制御のブロック図](../figures/pid_block_diagram.png)

### ▶ 伝達関数（ラプラス領域）｜Transfer Function (Laplace Domain)

$$
C(s) = K_P + \frac{K_I}{s} + K_D s
$$

---

## 🌀 ステップ応答の比較｜Step Response Comparison

以下は同一の一次遅れ系に対して、各制御要素を個別に加えたときの応答例です。

| 制御 | 応答特性 | 備考 |
|------|----------|------|
| Pのみ | 応答は速いが定常誤差あり | 単純な比例制御 |
| PI    | 定常誤差が解消されるが応答が遅くなる | 低速系向き |
| PD    | オーバーシュート抑制に有効だが誤差残る | ノイズに弱い |
| PID   | 安定性と応答性の両立を図る | 最も広く用いられる |

※ 実装例は [`/simulation/pid_simulation.py`](../simulation/pid_simulation.py) を参照。

---

## 💡 設計のポイント｜Design Tips

- **ゲイン調整（チューニング）が最重要**  
  - Ziegler-Nichols法、Cohen-Coon法、経験則などあり  
- **ノイズのある環境ではD項に注意**（微分はノイズを増幅）  
- **実装では離散化が必要**（Tustin法や前進差分法など）

---

## 📚 参考資料｜References

- 「制御工学入門」森北出版  
- *Feedback Control of Dynamic Systems* by Franklin, Powell, Emami-Naeini  
- Python: `scipy.signal`, `control`, `matplotlib` ライブラリ  
