# 🚨 03. 例外処理とLLMによる知識注入

本節では、従来の制御系では困難だった**例外的状況や未知の事象への対応**について、  
LLMを活用して「知識ベース制御」や「意味的補完」を行うアプローチを紹介します。

---

## 🔧 例外処理とは？

- 想定外の状況・入力・環境変化に対して、システムを安全・安定に保つための処理
- 通常のFSMやPIDでは事前定義が困難なものも多い（例：異常音・通信断・誤操作）

---

## 🧠 LLMが担う役割

| 項目 | 内容 |
|------|------|
| 状況理解 | 異常の自然言語的記述を文脈理解（例：「ブザー音が鳴っている」） |
| 原因推定 | 「これは過熱異常の可能性がある」と過去知識から推定 |
| 対応策提案 | 「電源を落として30秒待ってください」などの行動提案 |
| FSM補完 | 状態遷移の例外パスとして挿入可能（例：回復状態 → 通常復帰） |

---

## 📘 実装例（ChatGPTベース）

```python
def handle_exception(observation_text):
    prompt = f"異常が発生しました：{observation_text}。原因と対応策を述べてください。"
    return chatgpt_respond(prompt)
```

### 入力例：
```
「センサが全く反応しない」「温度が急上昇している」
```

### 出力例（ChatGPT）：
```
「センサ断線の可能性があります。機器を停止し、センサ接続を確認してください。」
```

---

## 💬 FSMへの統合イメージ

- 通常の状態遷移に「異常状態」や「再初期化状態」を挿入
- LLMが状況判断 → FSM構造の一部を再構築（自己適応）

---

## 🔒 安全性と制約

- 制御に関わる判断は「信頼できる例外クラス」のみに限定する
- LLM出力は**最終判断者ではなく提案者**として位置づける
- 実時間性・検証性とのトレードオフを意識

---

## 🔚 まとめ

- LLMは「人間的な状況理解」により、例外処理・知識注入の鍵となる
- FSMと組み合わせることで、より頑健で柔軟な制御システムが実現可能

📄 次へ：[04_goal_reasoning.md](./04_goal_reasoning.md)

---
