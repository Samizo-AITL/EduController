---
layout: clean
title: 01_rl_basics
permalink: /part07_rl_control/theory/01_rl_basics.html
---

---

# 🧠 01. 強化学習の基本構造（RL Basics）

> ℹ️ 数式が正しく表示されない場合は、[GitHub版はこちら](https://github.com/Samizo-AITL/EduController/blob/main/part07_rl_control/theory/01_rl_basics.md) を参照してください。

---

本節では、**強化学習（Reinforcement Learning, RL）**の基本構造と主要な用語・概念を解説します。  
RLは、エージェントが**環境と相互作用しながら最適な行動ポリシーを学習**する枠組みに基づきます。

This section explains the **basic structure, terminology, and concepts** of Reinforcement Learning (RL).  
RL is based on the idea that an agent **learns optimal policies through interaction with the environment**.

---

## 🎯 強化学習の基本要素（MDP） / RL Fundamentals (MDP)

強化学習は、**マルコフ決定過程（Markov Decision Process, MDP）**として定式化されます。

| 要素 / Element | 内容 / Description |
|------|------|
| $S$  | 状態空間（State Space） |
| $A$  | 行動空間（Action Space） |
| $R$  | 報酬関数 $r(s, a)$ |
| $P$  | 遷移確率 $P(s'|s, a)$ |
| $\pi$ | ポリシー（方策）：状態→行動の写像 / State→Action mapping $\pi(a|s)$ |

---

## 🔄 学習の流れ（Agent–Environment Loop）

1. エージェントが状態 $s_t$ を観測  
   Agent observes current state $s_t$
2. ポリシー $\pi$ に基づき行動 $a_t$ を選択  
   Agent selects action $a_t$ based on $\pi$
3. 環境が新しい状態 $s_{t+1}$ と報酬 $r_t$ を返す  
   Environment returns new state $s_{t+1}$ and reward $r_t$
4. エージェントが報酬に基づき $\pi$ を更新  
   Agent updates $\pi$ based on the reward
5. 上記を繰り返し、累積報酬を最大化  
   Loop continues to maximize cumulative rewards

---

## 📐 報酬と目的関数 / Rewards & Objective Function

エージェントの目的は、**累積報酬（Return）**を最大化することです。

- 割引累積報酬（Discounted Return）  
  $$
  G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k}
  $$
  - $\gamma \in [0, 1)$：割引率 / Discount factor (e.g., 0.99)

---

## 🧮 方策と価値関数 / Policy & Value Functions

- 方策（Policy）：$\pi(a|s)$  
  - 状態に対する行動選択の確率分布または決定論的関数
- 状態価値関数（State Value Function）：  
  $$
  V^\pi(s) = \mathbb{E}[G_t \mid s_t = s, \pi]
  $$
- 行動価値関数（Action Value Function）：  
  $$
  Q^\pi(s, a) = \mathbb{E}[G_t \mid s_t = s, a_t = a, \pi]
  $$

---

## 🔧 モデルフリー vs モデルベース / Model-Free vs Model-Based

| 種類 / Type | 特徴 / Characteristics |
|--------------|------------------------|
| モデルフリー / Model-Free | 環境モデルなし。Q学習、Policy Gradientなど |
| モデルベース / Model-Based | 遷移モデルを推定・利用。MPCに近いアプローチ |

---

## 🔍 主なアルゴリズム分類 / Main Algorithm Categories

| 系統 / Category | 例 / Examples |
|----------------|--------------|
| 値ベース / Value-Based | Q-learning, DQN |
| 方策ベース / Policy-Based | Policy Gradient, REINFORCE |
| アクター・クリティック / Actor-Critic | A2C, DDPG, PPO（連続制御向け） |

---

## 🛠️ 制御応用での特徴 / RL in Control Applications

- **モデル不要**（Model-Free制御）  
- **適応性・柔軟性が高い**（非線形・ノイズ耐性）  
- 訓練コスト・時間が大きい、安定性保証が難しい  
- PID等の古典制御との**ハイブリッド設計**が有効

---

## 🔚 まとめ / Summary

強化学習は、「試行錯誤＋報酬」に基づき制御戦略を獲得する手法です。  
次節では、倒立振子制御（CartPole）へのRL適用例を通して、実装と挙動を学びます。

---

**➡️ [次節 / Next: 02. 倒立振子 DDPG実装](https://samizo-aitl.github.io/EduController/part07_rl_control/theory/02_cartpole_ddpg.html)**  
Applies RL to cartpole control using the DDPG algorithm.

**🏠 [Part 07 トップ / Back to Part 07 Top](https://samizo-aitl.github.io/EduController/part07_rl_control/)**
