# 🎯 FSM設計プロンプトテンプレート（SamizoGPT連携用）

このプロンプトテンプレートは、ChatGPTに対してFSM（有限状態機械）の構造を指示し、  
**VerilogなどのHDL記述**や**Mermaid図**などを自動生成させるためのものです。

---

## 📌 テンプレート形式

```markdown
# タスク: FSM制御の設計テンプレートを生成して
## 条件:
- 状態数: 4状態
- 出力制御: あり（状態ごとに異なる信号）
- HDL記述: Verilogベースでお願いします
- トリガ: start, clk, reset
- 設計思想をコメント付きで説明して
```

---

## 🔁 バリエーション例

🧩 YAMLベースのFSMを渡す場合

# タスク: このFSM定義をVerilogで実装して
## 入力形式: YAML
```yaml
fsm:
  name: counter_fsm
  states:
    - idle
    - count1
    - count2
    - done
  transitions:
    - from: idle
      to: count1
      trigger: start
    - from: count1
      to: count2
      trigger: clk
    - from: count2
      to: done
      trigger: clk
    - from: done
      to: idle
      trigger: reset
  outputs:
    - state: idle
      signal: 0b00
    - state: count1
      signal: 0b01
    - state: count2
      signal: 0b10
    - state: done
      signal: 0b11
```

条件:
	•	クロック同期の同期式FSMとして
	•	状態出力を assign 文で定義
	•	コメント付きで設計方針を説明

 ---

## ✅ ChatGPT出力の例（概要）

- `always @(posedge clk)` による状態遷移
- `case (state)` による状態処理
- 状態出力の `assign` 文
- `reg [1:0] state` などの型宣言
- コメント例：`// idle状態では出力を00に設定`

---

## 🔗 関連教材と接続

| リソース | 用途 |
|----------|------|
| `fsm_example_counter.yaml` | YAML構造のFSM定義入力 |
| `fsm_to_mermaid.py` | 状態遷移図の可視化用補助 |
| `fsm_template.md` | YAML形式FSMの設計指針テンプレート |
| `execution_logs/` | プロンプトの使用結果と応答記録を保存可能 |

---

## 📄 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
本プロンプトテンプレートは教育・設計支援目的で自由に利用・改変可能です。


