# 🔄 Part 03: 適応制御・ロバスト制御（Adaptive & Robust Control）

本章では、制御対象のパラメータ変動・モデリング誤差に対応する  
**適応制御**と**ロバスト制御**について理論と実装の両面から学びます。  
また、FSM×PID×LLMで構成される AITL-H における「理性層」の柔軟化技術としても位置づけられます。

In this chapter, we learn both the theory and implementation of **adaptive** and **robust** control techniques,  
which are essential for dealing with system parameter variations and modeling uncertainties.  
These are also key techniques for enhancing the "rational layer" in the AITL-H architecture (FSM × PID × LLM).

---

## 🎯 学習目標 / Learning Objectives

- モデル変動・外乱に強い制御器の設計方法を理解する  
- MRACやゲインスケジューリングなどの適応戦略を体験する  
- H∞制御の基本概念と感度関数・補償関数を理解する  
- FSM/LLMと連携した適応的な制御判断の構造を設計できる  

- Understand how to design controllers that are robust to plant variations and disturbances  
- Learn adaptive strategies like MRAC and gain scheduling  
- Grasp the fundamentals of H-infinity control, sensitivity and complementary functions  
- Design adaptive decision-making structures using FSM and LLM  

---

## 🧩 構成一覧 / Chapter Structure

### 📘 [theory/](./theory/)

| ファイル名 | 内容 |
|------------|------|
| [`01_adaptive_intro.md`](./theory/01_adaptive_intro.md) | 適応制御の概要と必要性 |
| [`02_mrac_design.md`](./theory/02_mrac_design.md)       | MRAC（モデル参照型適応制御）の理論 |
| [`03_gain_scheduling.md`](./theory/03_gain_scheduling.md) | ゲインスケジューリング制御の仕組み |
| [`04_robust_control.md`](./theory/04_robust_control.md) | ロバスト制御とH∞制御の基礎 |

---

### 🧪 [simulation/](./simulation/)

| スクリプト名 | 内容 |
|--------------|------|
| [`mrac_simulation.py`](./simulation/mrac_simulation.py) | MITルールによるMRACのステップ追従 |
| [`gain_schedule_demo.py`](./simulation/gain_schedule_demo.py) | スケジューリングによる比例制御の補間 |
| [`hinf_synthesis_demo.py`](./simulation/hinf_synthesis_demo.py) | 感度・補償関数のボード解析によるH∞デモ |

---

### 🖼️ [figures/](./figures/)

| ファイル名 | 内容 |
|------------|------|
| [`mrac_response.png`](./figures/mrac_response.png) | MRAC応答曲線 |
| [`gain_schedule_response.png`](./figures/gain_schedule_response.png) | GS制御の動的応答 |
| [`hinf_sensitivity_response.png`](./figures/hinf_sensitivity_response.png) | H∞制御における $S$/$T$ の周波数応答 |

---

## 🔗 AITL-Hとの連携 / AITL-H Integration

| AITL層 | 制御役割 | 本章との関係 |
|--------|----------|--------------|
| 本能（FSM） | 状態遷移制御 | モードごとのゲインスケジューリング |
| 理性（PID） | 汎用的物理制御 | MRACでチューニング、H∞で保証強化 |
| 知性（LLM） | 状況予測・判断 | 制御戦略選択・制御パラメータ提案支援 |

---

## 🚧 今後の展開予定 / Future Extensions

- [`05_l1_adaptive.md`](./theory/05_l1_adaptive.md)：L1適応制御の設計原理（予定）  
- [`robust_block_diagram.png`](./figures/robust_block_diagram.png)：H∞制御構成図のAI生成（予定）  
- [`notebooks/`](./notebooks/)：MRAC・GSのインタラクティブ実験ノート追加予定  
- [`AITL連携図`](../figures/aitl_structure.png)：Part03を含むAITL全体構造図を統合更新予定  

---

## 📎 関連リンク / Related Links

- 🔁 [Part 02: PID制御の基礎](../part02_pid_control/README.md)  
- 🧠 [AITL-H 概要](../../aitl_h/README.md)  
- 📦 [制御教材トップページ](../../README.md)
