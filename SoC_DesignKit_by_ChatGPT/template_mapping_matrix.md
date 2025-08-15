---
layout: clean
title: テンプレート対応マトリクス（EduController × SoC_DesignKit_by_ChatGPT）
permalink: /SoC_DesignKit_by_ChatGPT/
---

---

# 🗺️ テンプレート対応マトリクス（EduController × SoC_DesignKit_by_ChatGPT）

本資料は、EduControllerの各章（Part01〜09）に対し、  
SoC_DesignKit_by_ChatGPTに含まれるテンプレート群の対応関係を示します。  
教材の理論と実装テンプレの橋渡し、プロンプト設計のガイドとして活用できます。

---

## 📘 対応マトリクス

| 章 | 内容 | 対応テンプレート | 所属ディレクトリ |
|----|------|------------------|------------------|
| Part01 | 古典制御（PID） | `pid_controller.v`, `fixed_point_notes.md` | `/pid/` |
| Part02 | 状態空間制御 | （※今後追加：状態空間ブロックなど） | ― |
| Part03 | 適応制御 | ―（構造的対応なし） | ― |
| Part04 | デジタル制御 | `c_sample_pid.c`, `conversion_prompt.md` | `/c_to_hdl/` |
| Part05 | 実装・演習 | `testbench/`, `c_to_hdl/`, `pid/` | 複数ディレクトリ |
| Part06 | NN制御 | ―（実装テンプレ非対応） | ― |
| Part07 | 強化学習 | ―（実装テンプレ非対応） | ― |
| Part08 | データ駆動制御 | ―（実装テンプレ非対応） | ― |
| Part09 | LLM統合制御 | `llm_control_prompt.md`, `fsm_llm_hybrid_example.md`, `fsm/`一式 | `/llm/`, `/fsm/` |

---

## 🔁 テンプレート × プロンプト対応表

| テンプレート | 対応プロンプト | 説明 |
|--------------|----------------|------|
| `fsm_example_counter.yaml` | `fsm_prompt.md` | 状態定義からVerilog構成へ誘導 |
| `c_sample_pid.c` | `conversion_prompt.md` | C→Verilog変換指示テンプレ |
| `fsm_llm_hybrid_example.md` | `llm_control_prompt.md` | FSMとLLMのハイブリッド制御構成設計 |
| `pid_controller.v` | （補足記述あり） | HDL出力設計の学習実装例として使用 |

---

## 🔗 補助リソース

| ファイル | 用途 |
|----------|------|
| `fsm_to_mermaid.py` | YAML→Mermaid図変換（FSM構造可視化） |
| `waveform_analysis.md` | GTKWaveによる出力波形の確認ガイド |
| `execution_logs/` | 実行プロンプトとGPT応答ログの記録 |

---

## 📘 備考

- 本マトリクスは随時拡張され、状態空間制御（Part02）やNN制御（Part06）にも対応予定です。
- AITL-H構成（FSM×PID×LLM）の教材統合を意識し、Part09を中核にテンプレート群が構成されています。

---

## 🔖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)
