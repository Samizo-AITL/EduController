---
layout: default
title: EduController/README.md
---

---

# 🎛️ **EduController：制御理論とAI制御の教育フレームワーク**  
**EduController: Educational Framework for Control Theory and AI Control**

---

## 🔗 **公式リンク | Official Links**

| 言語 / Language | 種別 / Type | リンク / Link |
|---|---|---|
| 🇯🇵 **Japanese Version** | 🌐 GitHub Pages | [https://samizo-aitl.github.io/EduController/](https://samizo-aitl.github.io/EduController/) |
| 🇯🇵 **Japanese Version** | 💻 GitHub | [https://github.com/Samizo-AITL/EduController](https://github.com/Samizo-AITL/EduController) |
| 🇺🇸 **English Version** | 🌐 GitHub Pages | [https://samizo-aitl.github.io/EduController/en/](https://samizo-aitl.github.io/EduController/en/) |
| 🇺🇸 **English Version** | 💻 GitHub | [https://github.com/Samizo-AITL/EduController/tree/main/en](https://github.com/Samizo-AITL/EduController/tree/main/en) |

---

## 📘 **概要 | Overview**
**JP:** EduController は、古典制御から現代制御、さらに AI ベースの次世代型制御までを体系的に学べる、段階的かつ実践的な教材プロジェクトです。Python による制御理論の直感的理解から HDL 記述、LLM 統合設計まで幅広くサポートします。  
**EN:** EduController is a step-by-step, practical educational project covering classical, modern, and AI-based next-generation control. It supports a wide range of learning, from intuitive understanding of control theory using Python to HDL coding and LLM-integrated design.

---

## 🧭 **構成概要 | Structure Overview**
**JP:** EduController は全 10 章で構成され、以下の 3 系統に分類されます。  
**EN:** EduController consists of 10 chapters, categorized into the following three tracks.

| 系統 / Track | 内容（JP） | Overview (EN) |
|---|---|---|
| 🎓 **制御理論系 (Part 01〜05)** | 古典制御、状態空間、デジタル制御、実装演習 | Classical control, state-space, digital control, practical implementation |
| 🤖 **AI制御系 (Part 06〜08)** | ニューラルネット、強化学習、データ駆動制御 | Neural networks, reinforcement learning, data-driven control |
| 🧠 **統合・応用制御系 (Part 09〜10)** | LLM統合制御、倒立振子総合制御 | LLM-integrated control, inverted pendulum control |

---

## 📚 **章構成一覧 | Chapter Structure**

### 🎓 **制御理論系 / Classical & Modern Control**
| 章 / Chapter | ディレクトリ | 内容概要（JP） | Overview (EN) |
|---|---|---|---|
| **Part 01** | [part01_classical](./part01_classical/) | PID制御、ボード線図、安定性 | PID control, Bode plot, stability |
| **Part 02** | [part02_modern](./part02_modern/) | 状態空間、LQR、カルマンフィルタ | State-space, LQR, Kalman filter |
| **Part 03** | [part03_adaptive](./part03_adaptive/) | 適応・ロバスト制御（MRAC、H∞、L1） | Adaptive & robust control (MRAC, H∞, L1) |
| **Part 04** | [part04_digital](./part04_digital/) | デジタル制御、Z変換、DSP実装 | Digital control, Z-transform, DSP implementation |
| **Part 05** | [part05_practical](./part05_practical/) | Python実装、ROS演習、FPGA制御 | Python, ROS practice, FPGA-based control |

### 🤖 **AI制御系 / AI-based Control**
| 章 / Chapter | ディレクトリ | 内容概要（JP） | Overview (EN) |
|---|---|---|---|
| **Part 06** | [part06_nn_control](./part06_nn_control/) | ニューラルネット制御（NN-PID、逆モデル） | Neural network control (NN-PID, inverse model) |
| **Part 07** | [part07_rl_control](./part07_rl_control/) | 強化学習制御（Q学習、DDPG、PPO） | Reinforcement learning control (Q-learning, DDPG, PPO) |
| **Part 08** | [part08_data_driven](./part08_data_driven/) | データ駆動制御（Koopman、行列識別） | Data-driven control (Koopman, system identification) |

### 🧠 **統合・応用制御系 / Hybrid & Applied Control**
| 章 / Chapter | ディレクトリ | 内容概要（JP） | Overview (EN) |
|---|---|---|---|
| **Part 09** | [part09_llm_hybrid](./part09_llm_hybrid/) | LLM統合制御（FSM×PID×LLM） | LLM-integrated hybrid control (FSM×PID×LLM) |
| **Part 10** | [part10_pendulum](./part10_pendulum/) | 倒立振子の総合制御（PID / LQR / DDPG / HDL） | Integrated control of inverted pendulum (PID / LQR / DDPG / HDL) |

---

## 🔩 **実装支援ツール / Implementation Toolkit**
| ディレクトリ | 内容概要（JP） | Overview (EN) |
|---|---|---|
| [**matlab_tools/**](./matlab_tools/) | Simulink による PID・状態空間制御の可視化、Cコード生成、HDL設計への展開 | Visualization of PID/state-space control in Simulink, C code generation, HDL design |
| [**SoC_DesignKit_by_ChatGPT/**](./SoC_DesignKit_by_ChatGPT/) | FSM・PID・LLM制御のテンプレート、ChatGPTによるVerilog生成、テストベンチ検証 | Templates for FSM, PID, LLM control; Verilog generation via ChatGPT; testbench verification |

---

## 🔧 **推奨ツール / Recommended Tools**
| 分類 / Category | ツール | 主な用途（JP） | Main Use (EN) |
|---|---|---|---|
| 🐍 Python系 | `control`, `scipy`, `matplotlib`, `torch`, `gymnasium` | 理論演習、AI制御実験 | Theoretical exercises, AI control experiments |
| 📊 GUI系 | MATLAB / Simulink | ブロック図設計、Cコード生成 | Block diagram design, C code generation |
| 🤖 LLM系 | ChatGPT / GPT-4o | 設計支援、C→Verilog変換 | Design assistance, C→Verilog conversion |
| ⚙️ 実装系 | ROS / Verilog / FPGA | ハードウェア制御実装、PoC展開 | Hardware control implementation, PoC |

---

## 🔗 **関連プロジェクト / Related Projects**
| Project | JP（概要） | EN (Summary) |
|---|---|---|
| 🎓 [**Edusemi-v4x**](https://samizo-aitl.github.io/Edusemi-v4x/) <br>💻 [GitHub](https://github.com/Samizo-AITL/Edusemi-v4x) | 半導体設計・プロセス教育教材（Python、sky130、OpenLane） | Semiconductor design & process education (Python, sky130, OpenLane) |
| 🤖 [**AITL-H**](https://samizo-aitl.github.io/AITL-H/) <br>💻 [GitHub](https://github.com/Samizo-AITL/AITL-H) | FSM×PID×LLMの三層制御フレームワーク（Part09と連携） | Three-layer control framework (FSM×PID×LLM) |
| 🧠 [**SamizoGPT**](https://samizo-aitl.github.io/SamizoGPT/) <br>💻 [GitHub](https://github.com/Samizo-AITL/SamizoGPT) | ChatGPTのプロンプト設計支援テンプレート集（設計支援と連携） | Prompt design templates for ChatGPT (design assistance) |

---

## 👤 **執筆者情報 / Author**
| 📌 項目 / Item | 内容（JP） | Details (EN) |
|---|---|---|
| **氏名 / Name** | 三溝 真一 | Shinichi Samizo |
| **学歴 / Education** | 信州大学大学院 電気電子工学 修了 | M.Eng., Electrical & Electronic Engineering, Shinshu University |
| **経歴 / Career** | 元 セイコーエプソン株式会社 技術者（1997年〜） | Former engineer, Seiko Epson Corp. (1997–) |
| **経験領域 / Expertise** | 半導体デバイス（ロジック・メモリ・高耐圧混載）、インクジェット薄膜ピエゾアクチュエータ、PrecisionCore製品化・BOM管理・ISO教育 | Semiconductor devices (logic, memory, high-voltage mixed-signal), inkjet thin-film piezo actuators, PrecisionCore productization, BOM management, ISO training |
| **連絡先 / Contact** | ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)<br>🐦 [https://x.com/shin3t72](https://x.com/shin3t72)<br>💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/) | ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)<br>🐦 [https://x.com/shin3t72](https://x.com/shin3t72)<br>💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/) |

---

## 📄 **ライセンス / License**
| 📌 項目 / Item | 内容（JP） | Details (EN) |
|---|---|---|
| **ライセンス種別 / Type** | MITライセンス | MIT License |
| **利用条件 / Usage** | 自由に使用・改変・再配布可能 | Free to use, modify, and redistribute |
| **推奨利用 / Recommended Uses** | 教育・研究・社内研修 | Education, research, corporate training |

---

## 💬 **フィードバック / Feedback**
💬 [**EduController教材の議論はこちら → Discussions**](https://github.com/Samizo-AITL/EduController/discussions)
