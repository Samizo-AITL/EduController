---
layout: clean
title: 01. モデルフリー制御とは？
permalink: /part08_data_driven/theory/01_model_free_control.html
---

---

# 🔄 01. モデルフリー制御とは？ / What is Model-Free Control?


> 💡 **Note:** 数式や図が正しく表示されない場合は、[GitHub版はこちら](https://github.com/Samizo-AITL/EduController/blob/main/part08_data_driven/theory/01_model_free_control.md) をご覧ください。

---

本節では、**モデルフリー制御（Model-Free Control）**の基本概念と背景を解説します。  
This section explains the **basic concepts and background of Model-Free Control**,  
a method that designs controllers **without explicitly building mathematical models** of the target system.

---

## 🎯 なぜモデルフリー制御なのか？ / Why Model-Free Control?

- **従来のモデルベース制御 / Traditional Model-Based Control**：
  - 数式モデル（微分方程式や状態空間）を前提  
    Based on mathematical models (differential equations or state-space)
  - 高精度だが、建模が困難・コスト高・ブラックボックス系に弱い  
    High accuracy but costly, difficult to model, and poor for black-box systems

- **モデルフリー制御の利点 / Advantages of Model-Free Control**：
  - **観測データのみ**で制御器設計が可能  
    Controller design possible from **only observed data**
  - 実験的アプローチとの親和性が高い  
    High affinity with experimental approaches
  - 実用現場で柔軟に対応しやすい  
    Flexible in practical field applications

---

## 🔧 モデルフリー制御の分類 / Types of Model-Free Control

| **種類 / Type** | **特徴 / Features** | **例 / Examples** |
|-----------------|---------------------|-------------------|
| 経験則ベース / Heuristic-Based | 人工知能的な制御則の設計 | Ziegler–Nichols, Fuzzy |
| データ駆動制御 / Data-Driven | データから動的モデルや制御器を学習 | DMD, Koopman, Subspace Identification |
| 強化学習制御 / RL-Based | 状態・報酬に基づき方策を学習 | DDPG, PPO, SAC |

---

## 📐 基本構造 / Basic Structure

モデルフリー制御は、「入力 $u(t)$ と出力 $y(t)$ の観測対」に基づいて制御器を構築します。  
Model-free control builds controllers based on observed input–output pairs:

- **モデルベース制御 / Model-Based**：
  $$\dot{x}(t) = f(x(t), u(t))$$

- **モデルフリー制御 / Model-Free**：
  $$y(t+1) = \mathcal{F}(y(t), y(t-1), \ldots, u(t), u(t-1), \ldots)$$

ここで $\mathcal{F}$ はデータから構成される関数（NNや線形予測など）です。  
Here, $\mathcal{F}$ is a function derived from data (e.g., neural networks, linear predictors).

---

## 📈 応用の流れ（概略） / General Workflow

1. 実験またはシミュレーションからデータを収集  
   Collect data from experiments or simulations  
2. 入力–出力系列を整形し、動的モデルを学習（回帰・識別など）  
   Format input–output series and learn a dynamic model (regression, identification)  
3. 得られたモデルを用いて予測・制御則を構築  
   Build prediction and control laws using the obtained model  
4. 制御性能を検証し、再学習を繰り返す  
   Validate control performance and iterate learning

---

## 🧠 制御への統合戦略 / Integration Strategies

- **予測制御（MPC）への組み込み / Integration into MPC**  
- Koopman/DMD による線形化 → LQR設計  
  Linearization via Koopman/DMD → LQR design  
- 強化学習とのハイブリッド設計  
  Hybrid design with reinforcement learning

---

## 🧪 本教材で扱う代表例 / Examples in This Chapter

| **手法 / Method** | **解説ファイル / Theory File** | **コード / Code** |
|-------------------|--------------------------------|-------------------|
| Koopman演算子 | [02_koopman_operator.md](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/02_koopman_operator/) | [koopman_linearization.py](https://samizo-aitl.github.io/EduController/part08_data_driven/simulation/koopman_linearization.py) |
| 動的モード分解（DMD） | [03_dmd.md](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/03_dmd/) | [dmd_analysis.py](https://samizo-aitl.github.io/EduController/part08_data_driven/simulation/dmd_analysis.py) |
| サブスペース同定法 | [04_subspace_id.md](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/04_subspace_id/) | [subspace_identification.py](https://samizo-aitl.github.io/EduController/part08_data_driven/simulation/subspace_identification.py) |

---

## 🔚 まとめ / Summary

モデルフリー制御は、AIやビッグデータ時代において重要な選択肢の一つです。  
In the era of AI and big data, model-free control is an essential design option.  
以降の節では、より具体的なアルゴリズムと実装例を通じて、その適用方法を学びます。  
The following sections present algorithms and implementation examples in detail.

---

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part08_data_driven/theory/02_koopman_operator.html)**  
Koopman演算子と線形化について解説します。  
Covers Koopman operator and linearization.

**🏠 [Part 08 トップ / Back to Part 08 Top](https://samizo-aitl.github.io/EduController/part08_data_driven/)**
