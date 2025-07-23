# 🎛️ EduController：制御理論とAI制御の教育フレームワーク

**EduController** は、古典制御から現代制御、さらにAIベースの次世代型制御までを体系的に学べる、**段階的・実践的な制御教育教材プロジェクト**です。  
Pythonを活用し、制御理論の直感的理解から、HDL記述やLLM統合設計まで幅広くサポートします。

---

- 🇺🇸 [English README here](./README_en.md)

---

## 🧭 構成概要：制御理論とAI制御の2系統

EduControllerは、全9章から構成され、以下の2系統に分類されます：

- 🎓 **制御理論系（Part 01〜05）**  
  古典制御、状態空間、デジタル制御、実装演習を体系的に学習

- 🤖 **AI制御系（Part 06〜09）**  
  ニューラルネット、強化学習、データ駆動制御、LLM統合制御を段階的に習得

> ※ 各章は独立して学習可能ですが、AI制御系は制御理論の基礎を前提としています。

---

## 📚 章構成一覧（リンク付き）

### 🎓 制御理論系

| 章 | ディレクトリ | 内容概要 |
|----|----------------|----------|
| Part 01 | [part01_classical](./part01_classical/) | PID制御、ボード線図、安定性 |
| Part 02 | [part02_modern](./part02_modern/) | 状態空間、LQR、カルマンフィルタ |
| Part 03 | [part03_adaptive](./part03_adaptive/) | 適応・ロバスト制御（MRAC、H∞、L1） |
| Part 04 | [part04_digital](./part04_digital/) | デジタル制御、Z変換、DSP実装 |
| Part 05 | [part05_practical](./part05_practical/) | Python実装、ROS演習、FPGA制御 |

---

### 🤖 AI制御系

| 章 | ディレクトリ | 内容概要 |
|----|----------------|----------|
| Part 06 | [part06_nn_control](./part06_nn_control/) | ニューラルネット制御（NN-PID、逆モデル） |
| Part 07 | [part07_rl_control](./part07_rl_control/) | 強化学習制御（Q学習、DDPG、PPO） |
| Part 08 | [part08_data_driven](./part08_data_driven/) | データ駆動制御（Koopman、行列識別） |
| Part 09 | [part09_llm_hybrid](./part09_llm_hybrid/) | LLM統合・ハイブリッド制御（FSM×PID×LLM） |

---

## 🔩 実装支援ツールキット（目玉モジュール）

### 🔹 [`matlab_tools/`](./matlab_tools/)  
- Simulinkによる **PID・状態空間制御の可視化**
- Simulink Coderによる **Cコード生成**
- 生成されたCコードは `c_to_hdl/` を通じてHDL設計へ展開可能

### 🔹 [`SoC_DesignKit_by_ChatGPT/`](./SoC_DesignKit_by_ChatGPT/)  
- FSM、PID、LLM制御構成のテンプレート群
- ChatGPTプロンプトによるVerilog生成や、`testbench/` による波形検証も含む
- **教育から実装・PoCまで橋渡し可能な再利用可能テンプレート集**

> 🧠 教材・Simulink・ChatGPTを接続した「教育×実装×AI」の融合設計を実現

---

## 🔧 推奨ツール

| 分類 | ツール群 | 主な用途 |
|------|-----------|-----------|
| 🐍 Python系 | `control`, `scipy`, `matplotlib`, `torch`, `gymnasium` | 理論演習、AI制御実験 |
| 📊 GUI系 | MATLAB / Simulink | ブロック図設計、状態空間設計、Cコード生成（Simulink Coder） |
| 🤖 LLM系 | ChatGPT / GPT-4o | 設計支援プロンプト、C→Verilog変換、設計記録支援 |
| ⚙️ 実装系 | ROS / Verilog / FPGA | ハードウェア実装、PoC展開（Part05・09） |

---

## 🗂️ ディレクトリ構成

本リポジトリは、古典・現代・AI制御の学習と実装を支援する構造化教材パッケージです。  
章別教材と演習ツールは以下のように構成されています：

```
EduController/
├── part01_classical/               # 古典制御理論（ゲイン・Bode・位相余裕など）
├── part02_modern/                  # 現代制御（状態空間・可制御性・可観測性）
├── part03_adaptive/                # 適応制御（MRACなど）
├── part04_digital/                 # デジタル制御（Z変換・離散系）
├── part05_practical/               # 組込み・干渉・ノイズ・実装技術
├── part06_nn_control/              # ニューラルネットワーク制御（学習済み制御）
├── part07_rl_control/              # 強化学習制御（Q学習・Actor-Critic）
├── part08_data_driven/             # データ駆動制御（VRFT・システム同定）
├── part09_llm_hybrid/              # LLM統合型制御（自然言語×制御）
│
├── SoC_DesignKit_by_ChatGPT/       # HDL記述ベースの制御テンプレート集
│   ├── fsm/                        # 有限状態機械（FSM）テンプレート
│   ├── pid/                        # PID制御のVerilog記述例
│   ├── llm/                        # FSM×LLM統合制御テンプレート
│   ├── c_to_hdl/                   # C → Verilog変換プロンプトテンプレ
│   ├── testbench/                  # HDLテストベンチと波形解析
│   ├── execution_logs/             # ChatGPT対話ログ（任意記録）
│   ├── prompts/control_templates/  # ChatGPT用プロンプトテンプレート群
│   └── template_mapping_matrix.md  # テンプレート対応表（設計マッピング）
│
├── matlab_tools/                   # Simulink設計＋Cコード生成演習
│   ├── pid_simulink_example.slx    # PID制御モデル（Simulink）
│   ├── state_space_example.slx     # 状態空間モデル（Simulink）
│   ├── model_to_code.md            # Simulink→Cコード変換手順
│   └── getting_started.md          # Simulink入門手引き
│
├── README.md                       # トップページ（日本語）
└── README_en.md                    # 英文版トップページ
```

> 📦 各ディレクトリ内の教材詳細は、それぞれの `README.md` をご覧ください。

---

## 🚀 特徴

- 🔁 理論 → 実装 → AI応用 を一貫して学習可能
- 🧠 LLM（ChatGPT）と連携した再利用型設計
- 📊 SimulinkとHDLの橋渡しにも対応（Simulink Coder）
- 🛠️ テンプレート中心設計で再現性の高い教材構築

---

## 🔗 関連プロジェクト

- 🧩 [Edusemi v4.x](https://github.com/Samizo-AITL/Edusemi-v4x)  
  半導体教育教材（プロセス設計、Python、SoC設計など）

- 🤖 [AITL-H：Hybrid型知能制御](https://github.com/Samizo-AITL/AITL-H)  
  FSM×PID×LLMによる3層ハイブリッド制御。EduController Part09と連携

- 🧠 [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT)  
  ChatGPTの構造的プロンプト設計支援フレームワーク。EduControllerの設計支援にも活用

---

## 👤 執筆者情報 / Author

**三溝 真一（Shinichi Samizo）**  
- 信州大学大学院 電気電子工学 修了  
- 元 セイコーエプソン株式会社 技術者（1997年〜）  

📌 **経験領域**：  
- 半導体デバイス（ロジック／メモリ／高耐圧混載）  
- 薄膜ピエゾアクチュエータ
- PrecisionCoreプリントヘッド製品化

📬 **連絡先**
- ✉️ Email: [shin3t72@gmail.com](mailto:shin3t72@gmail.com)  
- 🐦 X (Twitter): [https://x.com/shin3t72](https://x.com/shin3t72)  
- 💻 GitHub: [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/)

---

## 🔖 ライセンス / License

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
本教材は教育・研究・個人学習の目的で自由にご利用いただけます。

---

💬 [EduController教材の議論はこちら → Discussions](https://github.com/Samizo-AITL/EduController/discussions)
