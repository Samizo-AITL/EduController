# 🤖 Part 6: ニューラルネットによる制御（Neural Network-based Control）

本章では、ニューラルネットワーク（NN）を用いた制御手法を学びます。  
従来のPID制御との比較や、NNによる補正・逆モデル制御、強化学習との接続可能性について扱います。

---

## 🎯 学習目標 / Learning Objectives

- NN制御の基本原理（関数近似・逆モデル）を理解する  
- ニューラルPID（NN-PID）制御器を設計・訓練する  
- 逆モデル学習によるフィードフォワード制御を実装する  
- PIDとの比較や統合設計（AITL構想）を考察する

---

## 📁 ディレクトリ構成

```plaintext
part06_nn_control/
├── theory/                   # 理論資料（Markdown）
│   ├── 01_nn_control.md
│   ├── 02_nn_pid.md
│   ├── 03_inverse_model.md
│   └── 04_ai_vs_classical.md
├── simulation/               # PyTorchなどによるコード実装
│   ├── nn_pid_control.py
│   ├── inverse_model_train.py
│   └── ai_vs_pid_sim.py
├── notebooks/                # 可視化・実験Notebook
│   ├── train_nn_pid.ipynb
│   └── (future) ai_vs_pid_comparison.ipynb
├── figures/                  # 図版フォルダ
│   └── nn_pid_structure.png など
└── README.md                # 本章の概要と進捗まとめ
```

---

## 🧪 実験コードとNotebook

| 内容                           | ファイル名                                                    |
|--------------------------------|---------------------------------------------------------------|
| NN-PID制御器（PyTorch）        | [`nn_pid_control.py`](./simulation/nn_pid_control.py)         |
| NN制御の学習・可視化           | [`train_nn_pid.ipynb`](./notebooks/train_nn_pid.ipynb)        |
| 逆モデル制御の学習             | [`inverse_model_train.py`](./simulation/inverse_model_train.py) |
| PID vs NN 比較シミュレーション | [`ai_vs_pid_sim.py`](./simulation/ai_vs_pid_sim.py)           |

---

## 🧠 理論資料（Markdown）

| タイトル                         | ファイル                                                    |
|----------------------------------|-------------------------------------------------------------|
| NN制御の概要と特徴               | [`01_nn_control.md`](./theory/01_nn_control.md)             |
| NN-PID制御の構成と学習方法       | [`02_nn_pid.md`](./theory/02_nn_pid.md)                     |
| 逆モデル制御の理論と実装         | [`03_inverse_model.md`](./theory/03_inverse_model.md)       |
| AI制御と古典制御の比較と統合戦略 | [`04_ai_vs_classical.md`](./theory/04_ai_vs_classical.md)   |

---

 ## 🔜 今後の展開（Next Steps）

- LSTMやTransformerによる時系列制御への応用  
- 強化学習ベース制御への接続（→ [`part07_rl_control/`](../part07_rl_control/)）  
- AITL構想との統合：PID + NN + LLMによる三層制御アーキテクチャ（→ [`part09_llm_control/`](../part09_llm_control/)）

---

## 📚 参考文献・リンク

- [PyTorch公式ドキュメント](https://pytorch.org/docs/)
- Narendra & Parthasarathy, “Neural Networks for Control”, 1990
- 本教材：[EduController](https://github.com/Samizo-AITL/EduController)

---

