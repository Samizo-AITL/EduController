# 🧩 SoC_DesignKit_by_ChatGPT

**SoC_DesignKit_by_ChatGPT** は、[EduController](../) における制御実装演習のためのテンプレート集です。  
FSM、PID、LLM統合制御などの構成要素を、**HDL記述ベースで学ぶためのテンプレート・プロンプト・テストベンチ**を提供します。

本モジュールは、[**SamizoGPT**](https://github.com/Samizo-AITL/SamizoGPT) のプロンプト支援と連携し、ChatGPT等を用いた構造設計・コード生成・設計進化の記録（[`execution_logs/`](execution_logs/)）とも連動します。

---

## 🎯 目的 / Purpose

- 教材として学んだ制御理論を、**実装テンプレートとして具体化**
- FSM / PID / LLMなどの**実装構造を再利用可能な形で提供**
- ChatGPTを活用した C → Verilog 変換や制御構造生成の**プロンプト演習に対応**
- [EduController](../) 内の **Part05（実装編）・Part09（LLM制御）**と連動

---

## 📁 ディレクトリ構成

| ディレクトリ | 内容 |
|--------------|------|
| [`fsm/`](fsm/) | 有限状態機械テンプレート（YAML記述・Mermaid.js変換支援） |
| [`pid/`](pid/) | PID制御器のVerilog実装（固定小数点演算も含む） |
| [`llm/`](llm/) | FSM×LLM制御などのプロンプト統合制御テンプレ |
| [`c_to_hdl/`](c_to_hdl/) | CコードからVerilogへの変換支援（プロンプト付き） |
| [`testbench/`](testbench/) | テストベンチ例、波形確認、RTLシミュレーション補助 |

---

## 🧠 ChatGPT連携（SamizoGPT）

以下のプロンプトテンプレート群と連携しています（[`EduController/prompts/control_templates/`](../prompts/control_templates/) 配下）：

| テンプレート名 | 対応ディレクトリ | 内容 |
|-----------------------------|------------------|--------------------------------------------------|
| [`fsm_prompt.md`](../prompts/control_templates/fsm_prompt.md) | [`fsm/`](../fsm/) | 状態数・トリガ記述などからFSMテンプレ生成 |
| `conversion_prompt.md` ※近日追加予定 | [`c_to_hdl/`](../c_to_hdl/) | Cコード（制御式）をVerilogに変換 |
| `choose_template_prompt.md` ※近日追加予定 | 全体 | 初学者向けテンプレ選択支援 |
| `llm_control_prompt.md` ※近日追加予定 | [`llm/`](../llm/) | FSM×LLM制御の構造設計補助 |

> 💬 各テンプレートの実行ログは [`execution_logs/`](../execution_logs/) に記録可能です。

---

## 🔧 活用例

### ✅ FSM制御の可視化演習

```yaml
# fsm_example_counter.yaml
states:
  - idle
  - count
transitions:
  - from: idle
    to: count
    trigger: start
```

→ fsm_to_mermaid.py で自動図変換し、状態遷移を視覚化

### ✅ PID式のC→HDL変換演習（GPT連携）

```
// 入力
error = ref - meas;
output = Kp * error + Ki * integral;
```

→ conversion_prompt.md を使い、ChatGPTにVerilog記述を出力させる → testbench/ で波形確認へ

## 📎 連携教材 / Integration

このテンプレート群は以下の教材と連携しています：

| 教材 | 関連内容 |
|------|----------|
| [EduController](../) | 本体教材（Part05/09）から利用可能 |
| [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT) | プロンプトテンプレ設計の供給元 |
| [`execution_logs/`](execution_logs/) | テンプレ使用記録、プロンプト対話ログの保存先（任意） |

---

## 🛠️ 今後の拡張予定

- Simulink→C→Verilogへの自動変換連携（[`matlab_tools/`](./matlab_tools/) との接続）
- VHDLテンプレートへの拡張
- FPGA開発環境（Vivado等）との導入連携資料

---

## 🔖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
本テンプレートは教育・演習・個人開発用途で自由に使用可能です。

---
