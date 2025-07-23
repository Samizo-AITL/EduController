# 📝 テンプレート実行ログ：FSM構成プロンプトセッション（2025年7月）

## 🎯 目的

- FSMテンプレートを使い、ChatGPTへVerilogコード生成を依頼
- Mermaid.js可視化と照合し、生成コードの構造整合性を確認
- SamizoGPTによるプロンプトテンプレートの検証記録

---

## 🗂️ 使用リソース

- プロンプト：`fsm_prompt.md`（ver. 2025.07）
- YAML：`fsm_example_counter.yaml`
- スクリプト：`fsm_to_mermaid.py`（状態遷移確認）
- GPTモデル：ChatGPT-4o

---

## 📤 入力プロンプト

```markdown
# タスク: このFSMをVerilogで実装して
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
	•	同期式FSM（クロック駆動）
	•	状態に応じた出力制御
	•	コメント付きVerilog記述でお願いします

---

## 🤖 ChatGPT応答要約（抜粋）

```verilog
module counter_fsm (...);
    ...
    always @(posedge clk or posedge reset) begin
        if (reset)
            state <= IDLE;
        else
            case (state)
                IDLE:    if (start) state <= COUNT1;
                COUNT1:  if (clk)   state <= COUNT2;
                COUNT2:  if (clk)   state <= DONE;
                DONE:    if (reset) state <= IDLE;
            endcase
    end
    ...
endmodule
```

---

---

## ✅ 評価

- ✅ YAML定義に忠実なVerilog構造が出力された  
- ✅ 出力信号も `assign` 文により正しく状態に応じて設定  
- ✅ コメント付きで可読性も高い  
- ⚠️ `clk` をトリガとした遷移表現は若干曖昧（要明示）

---

## 📎 備考

- Mermaid変換による状態遷移図との整合性：完全一致  
- 教材への反映候補：Part09（FSM演習）、`fsm_template.md` への統合案あり  
- モデル依存性（GPT-4o）を記録：再現性のために明示  

---

## 🔖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)

