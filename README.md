---
layout: default
title: EduController/README.md
---

# 🎛️ **EduController：制御理論とAI制御の教育フレームワーク**

**EduController** は、**古典制御**から**現代制御**、さらに**AIベースの次世代型制御**までを体系的に学べる、**段階的・実践的な制御教育教材プロジェクト**です。  
**Python** を活用し、**制御理論の直感的理解**から、**HDL記述**や**LLM統合設計**まで幅広くサポートします。

---

🇺🇸 [**English README here**](https://github.com/Samizo-AITL/EduController/blob/main/README_en.md)

---

## 🧭 **構成概要：制御理論・AI制御・統合制御の3系統**  
## 🧭 **Overview: Three Tracks – Classical, AI-based, and Hybrid Control**

EduController は、全10章から構成され、以下の3系統に分類されます：  
EduController consists of 10 chapters, categorized into the following three tracks:

- 🎓 **制御理論系（Part 01〜05）｜Classical & Modern Control**  
  古典制御、状態空間、デジタル制御、実装演習を体系的に学習  
  Systematic learning of classical control, state-space methods, digital control, and practical implementation

- 🤖 **AI制御系（Part 06〜08）｜AI-based Control**  
  ニューラルネット、強化学習、データ駆動制御を段階的に習得  
  Step-by-step mastery of neural networks, reinforcement learning, and data-driven control

- 🧠 **統合・応用制御系（Part 09〜10）｜Hybrid & Applied Control**  
  LLM統合や倒立振子を通じて制御の総合実装力を強化  
  Comprehensive application of control theory through LLM integration and inverted pendulum control

> ※ 各章は独立して学習可能ですが、AI制御・統合制御パートは制御理論の基礎を前提としています。  
> ※ Each chapter can be studied independently, but AI and hybrid control parts assume prior understanding of classical control theory.

---

## 📚 **章構成一覧（リンク付き）｜Chapter Structure (with Links)**

### 🎓 **制御理論系｜Classical & Modern Control**

| 章 | ディレクトリ | 内容概要｜Overview |
|----|----------------|--------------------|
| **Part 01** | [part01_classical](./part01_classical/) | **PID制御、ボード線図、安定性**<br>PID control, Bode plot, Stability |
| **Part 02** | [part02_modern](./part02_modern/) | **状態空間、LQR、カルマンフィルタ**<br>State-space, LQR, Kalman Filter |
| **Part 03** | [part03_adaptive](./part03_adaptive/) | **適応・ロバスト制御（MRAC、H∞、L1）**<br>Adaptive & Robust Control (MRAC, H∞, L1) |
| **Part 04** | [part04_digital](./part04_digital/) | **デジタル制御、Z変換、DSP実装**<br>Digital Control, Z-Transform, DSP Implementation |
| **Part 05** | [part05_practical](./part05_practical/) | **Python実装、ROS演習、FPGA制御**<br>Python, ROS Practice, FPGA-based Control |

### 🤖 **AI制御系｜AI-based Control**

| 章 | ディレクトリ | 内容概要｜Overview |
|----|----------------|--------------------|
| **Part 06** | [part06_nn_control](./part06_nn_control/) | **ニューラルネット制御（NN-PID、逆モデル）**<br>Neural Network Control (NN-PID, Inverse Model) |
| **Part 07** | [part07_rl_control](./part07_rl_control/) | **強化学習制御（Q学習、DDPG、PPO）**<br>Reinforcement Learning Control (Q-learning, DDPG, PPO) |
| **Part 08** | [part08_data_driven](./part08_data_driven/) | **データ駆動制御（Koopman、行列識別）**<br>Data-driven Control (Koopman, System Identification) |

### 🧠 **統合・応用制御系｜Hybrid & Applied Control**

| 章 | ディレクトリ | 内容概要｜Overview |
|----|----------------|--------------------|
| **Part 09** | [part09_llm_hybrid](./part09_llm_hybrid/) | **LLM統合・ハイブリッド制御（FSM×PID×LLM）**<br>LLM-integrated Hybrid Control (FSM×PID×LLM) |
| **Part 10** | [part10_pendulum](./part10_pendulum/) | **倒立振子の総合制御（PID / LQR / DDPG / HDL）**<br>Integrated Control of Inverted Pendulum (PID / LQR / DDPG / HDL) |

---

## 🔩 **実装支援ツールキット（目玉モジュール）**

### 🔹 [**matlab_tools/**](./matlab_tools/)

- **Simulink** による **PID・状態空間制御の可視化**
- **Simulink Coder** による **Cコード生成**
- 生成Cコードは `c_to_hdl/` により **HDL設計へ展開可能**

### 🔹 [**SoC_DesignKit_by_ChatGPT/**](./SoC_DesignKit_by_ChatGPT/)

- **FSM、PID、LLM制御構成のテンプレート群**
- **ChatGPTプロンプトによるVerilog自動生成**  
- `testbench/` による **波形検証**も含む

> 🧠 教材・Simulink・ChatGPTを接続した「**教育 × 実装 × AI**」の融合設計を支援

---

## 🔧 **推奨ツール**

| 分類 | ツール群 | 主な用途 |
|------|-----------|-----------|
| 🐍 **Python系** | `control`, `scipy`, `matplotlib`, `torch`, `gymnasium` | **理論演習、AI制御実験** |
| 📊 **GUI系** | **MATLAB / Simulink** | **ブロック図設計、Cコード生成** |
| 🤖 **LLM系** | **ChatGPT / GPT-4o** | **設計支援、C→Verilog変換、対話設計** |
| ⚙️ **実装系** | **ROS / Verilog / FPGA** | **ハードウェア制御実装、PoC展開** |

---

## 🗂️ **ディレクトリ構成**

```
EduController/
├── part01_classical/            # 古典制御理論（PID・ボード線図・安定性）
├── part02_modern/               # 現代制御理論（状態空間・LQR・カルマン）
├── part03_adaptive/             # 適応・ロバスト制御（MRAC・H∞・L1）
├── part04_digital/              # デジタル制御（Z変換・離散時間系・DSP）
├── part05_practical/            # 実装・ノイズ・ROS・FPGA制御演習
├── part06_nn_control/           # ニューラルネット制御（NN-PID・逆モデル）
├── part07_rl_control/           # 強化学習制御（Q学習・DDPG・PPO）
├── part08_data_driven/          # データ駆動制御（Koopman・行列識別）
├── part09_llm_hybrid/           # LLM統合制御（FSM×PID×LLMハイブリッド）
├── part10_pendulum/             # 倒立振子の総合制御（PID・LQR・RL・HDL・LLM）
│
├── SoC_DesignKit_by_ChatGPT/    # ChatGPTベースの制御設計テンプレート群
│   ├── fsm/                     # FSM（有限状態機械）のテンプレート
│   ├── pid/                     # PID制御のVerilog記述例
│   ├── llm/                     # LLM統合制御テンプレート（自然言語対応）
│   ├── c_to_hdl/                # Cコード→Verilog変換プロンプト
│   ├── testbench/               # テストベンチ・波形検証（Verilog用）
│   ├── prompts/                 # ChatGPTプロンプトテンプレート（設計補助）
│
├── matlab_tools/                # Simulink設計とCコード生成支援モジュール
│   ├── *.slx                    # Simulinkモデル（PID、状態空間）
│   ├── *.md                     # Simulink操作ガイド・導入手順
│
├── README.md                    # 日本語トップREADME（本ファイル）
└── README_en.md                 # 英語版トップREADME

```

> 📦 各ディレクトリ内の教材詳細は、それぞれの `README.md` をご覧ください。

---

## 🚀 **特徴**

- 🔁 **理論 → 実装 → AI応用** を一貫学習  
- 🧠 **LLM（ChatGPT）と連携**した再利用設計  
- 📊 **Simulink → HDL** の橋渡し設計  
- 🛠️ **テンプレート中心設計**で高再現性

---

## 🔗 **関連プロジェクト**

- 🧩 [**Edusemi-v4x**](https://github.com/Samizo-AITL/Edusemi-v4x)  
  **半導体設計・プロセス教育教材**（Python、sky130、OpenLane）

- 🤖 [**AITL-H**](https://github.com/Samizo-AITL/AITL-H)  
  **FSM×PID×LLM**の三層制御フレームワーク（**Part09と連携**）

- 🧠 [**SamizoGPT**](https://github.com/Samizo-AITL/SamizoGPT)  
  **ChatGPTのプロンプト設計支援**テンプレート集（**設計支援と連携**）

---

## 👤 **執筆者情報 / Author**

**三溝 真一（Shinichi Samizo）**  
- **信州大学大学院 電気電子工学 修了**  
- 元 **セイコーエプソン**株式会社 技術者（1997年〜）

📌 **経験領域**：  
- **半導体デバイス（ロジック・メモリ・高耐圧混載）**  
- **インクジェット薄膜ピエゾアクチュエータ**  
- **PrecisionCoreプリントヘッド製品化・BOM管理・ISO教育**

📬 **連絡先**  
- ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)  
- 🐦 [https://x.com/shin3t72](https://x.com/shin3t72)  
- 💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/)

---

## 🔖 **ライセンス / License**

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
教育・研究・個人学習を目的とした **自由な使用・改変・再配布** を歓迎します。

---

💬 [**EduController教材の議論はこちら → Discussions**](https://github.com/Samizo-AITL/EduController/discussions)

---

