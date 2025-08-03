---
layout: default
title: 01. PID制御の基礎
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

# 🧠 02. 倒立振子制御へのDDPG応用（CartPole + DDPG）

本節では、強化学習アルゴリズムの一つである DDPG（Deep Deterministic Policy Gradient）を用いて、  
代表的な制御対象である倒立振子（CartPole）を安定化させる制御器を学習します。

---

## 🎯 CartPole 環境の概要

- 目標：振子を立てたまま台車を左右に移動させ、倒れないように制御する  
- 状態ベクトル（ $s$ ）：  
  $[x, \dot{x}, \theta, \dot{\theta}]$（位置・速度・角度・角速度）
- 行動ベクトル（ $a$ ）：  
  台車に加える連続的な力（連続アクション環境を使用）

> 使用環境：`Pendulum-v1` または連続版の `CartPoleContinuous-v0`

---

## 🧪 使用するアルゴリズム：DDPG

DDPG（Deep Deterministic Policy Gradient）は、  
**Actor-Critic構造に基づく連続制御向けアルゴリズム**です。

- Actor：状態 $s$ に対して行動 $a$ を決定（ $\mu(s|\theta^\mu)$ ）  
- Critic：行動の良さ（ $Q(s,a)$ ）を評価（ $Q(s,a|\theta^Q)$ ）  
- ターゲットネットによる安定化  
- 経験再生バッファ（Replay Buffer）によるデータ効率向上

---

## ⚙️ 学習の流れ

1. 環境を初期化し、状態 $s_0$ を取得  
2. Actorネットで行動 $a_t$ を決定（＋ノイズ）  
3. 環境から $r_t, s_{t+1}$ を受け取る  
4. 経験 $(s_t, a_t, r_t, s_{t+1})$ を保存  
5. バッチ学習によりActorとCriticを更新  
6. ターゲットネットをソフト更新  
7. 上記をエピソード単位で繰り返し、最適ポリシーを獲得

---

## 📊 学習過程の観察

学習ログを以下のように可視化することで、制御器の改善を確認できます：

- 報酬の推移（エピソードごと）  
- エピソード継続時間（平均ステップ数）  
- 最終的な制御挙動のアニメーションまたはGIF出力

> 📁 関連ファイル：
> - [`cartpole_ddpg.py`](../simulation/cartpole_ddpg.py)  
> - [`ddpg_training_log.ipynb`](../notebooks/ddpg_training_log.ipynb)

---

## 🧠 技術メモ

- Actorの出力には $\tanh$ を使い、アクション範囲を制御  
- Ornstein-Uhlenbeckノイズで探索性を確保  
- DDPGはハイパーパラメータに敏感：バッチサイズ・学習率・更新頻度

---

## 🔚 まとめと展望

DDPGを用いることで、連続値制御を必要とする倒立振子問題にも対応可能です。  
学習により動的環境に適応したポリシーを自動獲得できます。

📁 次へ：[`03_rl_vs_classical.md`](./03_rl_vs_classical.md)

---
