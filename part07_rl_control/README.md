# 🧠 Part 7: 強化学習による制御（Reinforcement Learning Control）

本章では、強化学習（Reinforcement Learning, RL）を用いた制御設計手法を学びます。  
制御対象とのインタラクションを通じて最適な行動ポリシーを獲得し、モデルフリーな自律制御を実現します。

---

## 🎯 学習目標 / Learning Objectives

- 強化学習の基本構造（状態・行動・報酬）を理解する  
- 倒立振子や2輪車両などの制御問題にRLを適用する  
- DDPG、PPOなどの代表的なアルゴリズムを実装する  
- GymやPyBulletなどのシミュレーション環境を使う  
- 制御理論との違いや利点・課題を把握する

---

## 📁 ディレクトリ構成（予定）

```plaintext
part07_rl_control/
├── theory/                   # 理論資料（Markdown）
│   ├── 01_rl_basics.md
│   ├── 02_cartpole_ddpg.md
│   ├── 03_rl_vs_classical.md
├── simulation/               # 実装コード
│   ├── cartpole_ddpg.py
│   └── ppo_pendulum.py
├── notebooks/                # 可視化や訓練経過分析用Notebook
│   └── ddpg_training_log.ipynb
├── figures/                  # 図版（構造図、学習曲線など）
└── README.md
```

---

## 🧪 実験コード（予定）

| 内容                         | ファイル名                                           |
|------------------------------|------------------------------------------------------|
| 倒立振子 DDPG実装            | [`cartpole_ddpg.py`](./simulation/cartpole_ddpg.py) |
| PendulumへのPPO適用         | [`ppo_pendulum.py`](./simulation/ppo_pendulum.py)   |
| 学習ログの可視化             | [`ddpg_training_log.ipynb`](./notebooks/ddpg_training_log.ipynb) |

---

## 🧠 理論資料（Markdown）

| タイトル                           | ファイル                                              |
|------------------------------------|-------------------------------------------------------|
| 強化学習の基本構造と用語解説       | [`01_rl_basics.md`](./theory/01_rl_basics.md)         |
| 倒立振子制御へのRL応用             | [`02_cartpole_ddpg.md`](./theory/02_cartpole_ddpg.md) |
| 古典制御との違いとハイブリッド展開 | [`03_rl_vs_classical.md`](./theory/03_rl_vs_classical.md) |

---

## 🔜 今後の展開（Next Steps）

- モデル予測制御との融合（MPC × RL）  
- 状態推定器・報酬設計の高度化  
- AITL構想との接続（LLMを使った報酬設計やRL補助）

---

## 📚 参考資料

- [OpenAI Gym](https://www.gymlibrary.dev/)  
- [Spinning Up in Deep RL](https://spinningup.openai.com/en/latest/)  
- Lillicrap et al., “Continuous Control with Deep Reinforcement Learning” (2016)  
- 本教材：[EduController](https://github.com/Samizo-AITL/EduController)

---
