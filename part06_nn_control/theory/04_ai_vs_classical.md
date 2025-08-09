---
layout: default
title: 04. AI制御 vs 古典制御：特性比較と統合戦略
permalink: /EduController/part06_nn_control/theory/04_ai_vs_classical.html
---

---

# 🧮 04. AI制御 vs 古典制御  
**AI-based vs Classical Control: Comparison and Integration Strategy**

> 💡 **Note:** 数式や表がWebで正しく表示されない場合は、[GitHub版はこちら](https://github.com/Samizo-AITL/EduController/blob/main/part06_nn_control/theory/04_ai_vs_classical.md) を参照してください。

---

本章では、**AIを用いた制御（ニューラルネット・強化学習など）**と、  
**古典的制御（PID・LQRなど）**の特性を比較し、  
**使い分けと統合戦略**を整理します。

---

## 🎯 **学習目標 / Learning Objectives**

- AI制御と古典制御の**設計思想と特性の違い**を理解する  
- 両者の**長所と限界**を把握し、適用場面を判断できる  
- ハイブリッド型制御（AITL構想）の基盤を理解する  

---

## 🧠 **1. 設計思想とアプローチの違い**

| **項目 / Item** | **古典制御（PID/LQRなど）**                   | **AI制御（NN/RLなど）**                 |
|----------------|----------------------------------------------|-----------------------------------------|
| 設計方法       | 数理モデル・解析に基づく                      | データ・経験に基づく学習                 |
| 必要条件       | モデル構造や安定条件の明確化                  | 入出力データの蓄積と学習設計             |
| 実装性         | 高い（組込み・計算コスト低）                   | 高計算量・学習プロセスが必要              |
| 解釈性         | 高い（ゲイン・周波数応答で説明可能）           | 低め（ブラックボックス的）               |
| 柔軟性         | 限定的（線形・定常系が中心）                   | 高い（非線形・時変システムに適応可能）    |

---

## ⚖️ **2. 利点と限界**

### ✅ 古典制御の強み
- 安定性・性能指標の**数理的保証**が容易  
- 実装がシンプルで**計算資源が少なくても動作**  
- 環境変動やノイズに対して堅牢  

### ⚠️ 古典制御の限界
- 非線形・高次元系には適用が困難  
- モデル誤差や外乱に影響されやすい  

---

### ✅ AI制御の強み
- 高い関数近似能力で**複雑な動作を実現**  
- 学習により逐次的な性能改善が可能  
- 非線形性・時変性に対応可能  

### ⚠️ AI制御の課題
- 安定性や動作保証が難しい  
- 大量かつ高品質なデータが必要  
- 学習コスト・実装負荷が高い  

---

## 🔁 **3. 統合戦略（ハイブリッド制御）**

| **パターン / Pattern** | **内容 / Description**                      | **例 / Example**                      |
|------------------------|----------------------------------------------|----------------------------------------|
| NN補助PID              | PID出力をNNで補正                           | NN-PID制御（02章参照）                 |
| NNによるゲイン調整     | NNが動的にゲイン生成                        | ゲインスケジューリングNN               |
| 逆モデル × PID         | 逆モデルで初期入力推定 + PIDで微調整        | 安定性と追従性の両立                   |
| ルール+NN+LLM          | FSMで状態遷移 + NN推定 + LLMで判断          | AITL構想（09章）                       |

---

## 🔮 **4. 展望：AITL構想との接続**

AITL（Adaptive Intelligent Three-Layered）構想では、以下の**三層アーキテクチャ**で制御設計を分担します：

1. **本能層（FSM）** — 状態遷移・ルールベース制御（例：緊急停止）  
2. **理性層（PID/NN）** — 連続量制御・フィードバック制御  
3. **知性層（LLM）** — 目的推論・制御モード選択・自己チューニング  

> 🎯 **目的:** AI制御と古典制御を融合し、**柔軟性と安全性**を兼ね備えた制御システムを構築する。

---

## 📚 **参考資料 / References**
- Franklin, Powell. *Feedback Control of Dynamic Systems*  
- Levine. *The Control Handbook*  
- Reinforcement Learning & Control Survey (2021)  
- 本教材 [`part09_llm/`](https://samizo-aitl.github.io/EduController/part09_llm/) — LLM統合制御との連携展開  

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part06_nn_control/theory/03_inverse_model/)**  
逆モデル制御の構造と学習方法を解説。  
Covers inverse model control structure and learning methods.

**🏠 [Part 06 トップ / Back to Part 06 Top](https://samizo-aitl.github.io/EduController/part06_nn_control/)**  
全体概要と各章リンクを掲載。  
Provides full overview and links to all sections.
