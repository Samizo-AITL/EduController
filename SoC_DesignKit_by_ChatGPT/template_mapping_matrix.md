---
layout: clean
title: テンプレート対応マトリクス（EduController × SoC_DesignKit_by_ChatGPT）
permalink: /template_matrix/
---

---

# 🗺️ テンプレート対応マトリクス / Template Mapping Matrix
**EduController × SoC_DesignKit_by_ChatGPT**

[![GitHub](https://img.shields.io/badge/GitHub-Open%20Repo-black?logo=github)](https://github.com/Samizo-AITL/EduController)  
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

💡 **JP:** 本資料は、EduControllerの各章（Part01〜10）と  
SoC_DesignKit_by_ChatGPTに含まれるテンプレート群との対応関係を示します。  

💡 **EN:** This document maps each chapter of **EduController (Part01–10)** to the corresponding templates in **SoC_DesignKit_by_ChatGPT**.  
It acts as a bridge between theory and implementation, as well as a guide for prompt design.

---

## 📘 対応マトリクス / Mapping Matrix

| **章 / Chapter** | **内容 / Content** | **対応テンプレート / Templates** | **ディレクトリ / Directory** |
|------------------|--------------------|---------------------------------|-------------------------------|
| **Part01** | 古典制御（PID）<br>*Classical Control (PID)* | `pid_controller.v`, `fixed_point_notes.md` | `/pid/` |
| **Part02** | 状態空間制御<br>*State-space Control* | （※今後追加予定 / *Planned addition*） | ― |
| **Part03** | 適応制御<br>*Adaptive Control* | ―（未対応 / *Not supported*） | ― |
| **Part04** | デジタル制御<br>*Digital Control* | `c_sample_pid.c`, `conversion_prompt.md` | `/c_to_hdl/` |
| **Part05** | 実装・演習<br>*Implementation & Exercises* | `testbench/`, `c_to_hdl/`, `pid/` | 複数 / Multiple |
| **Part06** | NN制御<br>*Neural Network Control* | ―（未対応 / *Not supported*） | ― |
| **Part07** | 強化学習<br>*Reinforcement Learning* | ―（未対応 / *Not supported*） | ― |
| **Part08** | データ駆動制御<br>*Data-driven Control* | ―（未対応 / *Not supported*） | ― |
| **Part09** | LLM統合制御<br>*LLM-integrated Control* | `llm_control_prompt.md`, `fsm_llm_hybrid_example.md`, `fsm/` | `/llm/`, `/fsm/` |
| **Part10** | 倒立振子制御<br>*Hybrid Control of Inverted Pendulum* | `classical_control/`, `modern_control/`, `rl_control/`, `fsm/` | `/part10_pendulum/` |

---

## 🔁 テンプレート × プロンプト対応表  
**Template ↔ Prompt Mapping**

| **テンプレート / Template** | **対応プロンプト / Prompt** | **説明 / Description** |
|-----------------------------|----------------------------|-------------------------|
| `fsm_example_counter.yaml` | `fsm_prompt.md` | 状態定義から Verilog 構成へ誘導<br>*Guides from state definition to Verilog design* |
| `c_sample_pid.c` | `conversion_prompt.md` | C → Verilog 変換指示テンプレ<br>*Template for C→Verilog conversion* |
| `fsm_llm_hybrid_example.md` | `llm_control_prompt.md` | FSMとLLMのハイブリッド制御設計<br>*Hybrid control design of FSM × LLM* |
| `pid_controller.v` | （補足記述あり / *With notes*） | HDL出力設計の学習例<br>*Example for learning HDL design* |

---

## 🔗 補助リソース / Supplementary Resources

| **ファイル / File** | **用途 / Purpose** |
|----------------------|---------------------|
| `fsm_to_mermaid.py` | YAML → Mermaid 図変換（FSM構造可視化）<br>*Convert YAML to Mermaid for FSM visualization* |
| `waveform_analysis.md` | GTKWave出力波形の確認ガイド<br>*Guide to verifying waveforms in GTKWave* |
| `execution_logs/` | 実行プロンプトとGPT応答ログ<br>*Execution prompts and GPT response logs* |

---

## 📘 備考 / Notes

- 本マトリクスは随時拡張予定。  
  *This matrix will be continuously extended.*  
- 状態空間制御（Part02）、NN制御（Part06）などに対応を追加予定。  
  *Support for state-space control (Part02) and NN control (Part06) is planned.*  
- AITL-H構成（FSM × PID × LLM）を中核に、教材とテンプレ群を統合。  
  *The AITL-H architecture (FSM × PID × LLM) forms the core of integration between materials and templates.*  

---

## 📄 **ライセンス / License**

> 教材・コード・図表の性質に応じた **ハイブリッドライセンス** を採用  
> *Hybrid licensing based on the nature of materials, code, and diagrams.*

| **項目 / Item** | **ライセンス / License** | **説明 / Description** |
|-----------------|--------------------------|-------------------------|
| **コード（Code）** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布可<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須<br>*Attribution required* |
| **図表・イラスト（Figures & diagrams）** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

🏠 [トップページに戻る / Back to Top](https://samizo-aitl.github.io/EduController/)
