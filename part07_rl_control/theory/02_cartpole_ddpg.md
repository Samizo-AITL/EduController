---
layout: default
title: 02_cartpole_ddpg
permalink: /part07_rl_control/theory/02_cartpole_ddpg.html
---

---

# 🧠 02. 倒立振子制御へのDDPG応用（CartPole + DDPG）

> ℹ️ 数式が正しく表示されない場合は、[GitHub版はこちら](https://github.com/Samizo-AITL/EduController/blob/main/part07_rl_control/theory/02_cartpole_ddpg.md) を参照してください。

---

本節では、強化学習アルゴリズムの一つ **DDPG（Deep Deterministic Policy Gradient）** を用いて、  
代表的な制御対象 **倒立振子（CartPole）** の安定化制御器を学習します。

This section applies the **DDPG** algorithm to the classic **CartPole** control task,  
training a controller to stabilize the pole in a continuous action setting.

---

## 🎯 CartPole 環境の概要 / Overview of the CartPole Environment

- **目標 / Goal**：振子を立てたまま台車を左右に移動させ、倒れないよう制御する  
  Keep the pole upright by moving the cart left or right.
- **状態ベクトル / State vector**  $(s)$ ：

$$
s = [x, \dot{x}, \theta, \dot{\theta}]
$$
  
  （位置・速度・角度・角速度 / position, velocity, angle, angular velocity）
- **行動ベクトル / Action vector**  $(a)$ ：  
  台車に加える連続的な力 / Continuous force applied to the cart

> 使用環境 / Environment: `Pendulum-v1` または連続版 `CartPoleContinuous-v0`

---

## 🧪 使用アルゴリズム：DDPG / Algorithm: DDPG

DDPG（Deep Deterministic Policy Gradient）は、  
**Actor-Critic構造に基づく連続制御向けアルゴリズム**です。

- **Actor**：状態 $s$ に対して行動 $a$ を決定  
  $\mu(s|\theta^\mu)$
- **Critic**：行動の良さを評価  
  $Q(s,a|\theta^Q)$
- **ターゲットネット / Target Networks** による学習安定化  
- **経験再生バッファ / Replay Buffer** によるデータ効率向上

---

## ⚙️ 学習の流れ / Training Loop

1. **環境初期化 / Initialize environment** → $s_0$ を取得  
2. **Actorネットで行動選択 / Action selection**：$a_t = \mu(s_t) + \text{noise}$  
3. **環境ステップ / Environment step**：$(r_t, s_{t+1})$ を取得  
4. **経験保存 / Store experience**：$(s_t, a_t, r_t, s_{t+1})$  
5. **バッチ学習 / Batch update**：Actor & Critic を更新  
6. **ターゲットネット更新 / Soft update target networks**  
7. 上記を繰り返し、**最適ポリシー**を獲得

---

## 📊 学習過程の観察 / Monitoring Training

学習ログ可視化で制御性能の改善を確認できます。

- **報酬推移 / Reward progression**（エピソード平均）  
- **エピソード長 / Episode length**（平均継続ステップ数）  
- **最終挙動のアニメーション / Final policy animation**

> 📁 関連ファイル / Related files:  
> - [`cartpole_ddpg.py`](https://samizo-aitl.github.io/EduController/part07_rl_control/simulation/cartpole_ddpg.py)  
> - [`ddpg_training_log.ipynb`](https://samizo-aitl.github.io/EduController/part07_rl_control/notebooks/ddpg_training_log.ipynb)

---

## 🧠 技術メモ / Technical Notes

- Actor出力に **$\tanh$** を適用し、アクション範囲を制御  
- Ornstein-Uhlenbeckノイズで探索性を確保  
- ハイパーパラメータ（バッチサイズ、学習率、更新頻度）に敏感

---

## 🔚 まとめと展望 / Summary & Outlook

- DDPGは連続値制御問題に有効  
- 倒立振子のような不安定系も、学習を通じて安定化可能  
- 将来的にはMPCやモデルベース手法との統合が有望

---

**⬅️ [前節 / Previous: 01. RLの基本構造](https://samizo-aitl.github.io/EduController/part07_rl_control/theory/01_rl_basics.html)**  
Covers RL fundamentals, terminology, and the MDP framework.

**➡️➡️ [次節 / Next: 03. RL vs 古典制御](https://samizo-aitl.github.io/EduController/part07_rl_control/theory/03_rl_vs_classical.html)**  
Compares RL with classical control approaches and discusses hybrid strategies.

**🏠 [Part 07 トップ / Back to Part 07 Top](https://samizo-aitl.github.io/EduController/part07_rl_control/)**
