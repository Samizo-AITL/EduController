# 🧮 04. AI制御 vs 古典制御：特性比較と統合戦略

本章では、AIを用いた制御（ニューラルネット・強化学習）と、  
従来の古典的制御（PID・LQRなど）との**比較・使い分け・統合方針**を探ります。

---

## 🎯 学習目標 / Learning Objectives

- AI制御と古典制御の設計思想・特性を比較する  
- 両者の長所と限界を把握し、適用場面を考える  
- ハイブリッド型制御（AITL構想）の基盤を理解する

---

## 🧠 1. 設計思想とアプローチの違い

| 項目         | 古典制御（PID/LQRなど）             | AI制御（NN/RLなど）                 |
|--------------|------------------------------------|-------------------------------------|
| 設計方法     | 数理モデル・解析に基づく            | データ・経験に基づく学習            |
| 必要条件     | モデル構造や安定条件の明確化        | 入出力データの蓄積と学習設計        |
| 実装性       | 高い（組込み・計算コスト低）         | 高い計算量、学習プロセスが必要       |
| 解釈性       | 高い（ゲイン・周波数応答など）       | 低め（ブラックボックス的）          |
| 柔軟性       | 限定的（線形・定常系が中心）         | 高い（非線形・時変にも適応可能）     |

---

## ⚖️ 2. 利点と限界

### ✅ 古典制御の強み

- 安定性・性能指標が数理的に保証されやすい  
- シンプルで実装容易、堅牢性が高い  

### ⚠️ 古典制御の限界

- 非線形・高次元系に弱い  
- 実環境ではモデル誤差や外乱に影響されやすい  

---

### ✅ AI制御の強み

- 関数近似能力により複雑な動作を実現  
- 経験に基づく逐次的な性能改善が可能  

### ⚠️ AI制御の課題

- 安定性や動作保証が難しい  
- 学習データや訓練コストが大きい

---

## 🔁 3. 統合戦略（ハイブリッド制御）

| パターン             | 内容                                   | 例                                     |
|----------------------|----------------------------------------|----------------------------------------|
| NN補助PID            | PID出力にNNで補正                      | NN-PID制御（02章）                     |
| NNによるゲイン調整   | ゲインをNNが動的生成                   | ゲインスケジューリングNN              |
| 逆モデル × PID       | 逆モデルで制御初期値 + PIDで微調整     | 安定性と追従性の両立                   |
| ルール+NN+LLM        | 状態遷移（FSM）+ NN推定 + LLM判断      | AITL構想（09章）                       |

---

## 🔮 4. 展望：AITL構想との接続

AITL（Adaptive Intelligent Three-Layered）構想では、  
以下の3層で制御設計を分担します：

- **本能層（FSM）**：状態遷移・ルールベース制御（例：緊急停止）  
- **理性層（PID/NN）**：連続量制御・フィードバック制御  
- **知性層（LLM）**：目的推論・制御モード選択・自己チューニング

→ AI制御と古典制御を融合し、**人間的な柔軟性と安全性**を備えた制御を目指します。

---

## 📚 参考資料

- Franklin, Powell. “Feedback Control of Dynamic Systems”  
- Levine. “The Control Handbook”  
- Reinforcement Learning & Control Survey (2021)  
- 本教材 `part09_llm/`：LLM統合制御との連携展開

---
