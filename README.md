# 🎛️ EduController：制御理論とAI制御の教育フレームワーク

**EduController** は、古典制御から現代制御、さらにAIベースの次世代型制御までを体系的に学べる、**段階的・実践的な制御教育教材プロジェクト**です。  
Pythonを活用し、制御理論の直感的理解からAI統合型制御設計までをサポートします。

---

## 🧭 全体構成（Two-Part Curriculum）

### 🧱 第1部：制御理論（Part 1: Control Theory）

| ディレクトリ名 | 内容 | 主なキーワード |
|----------------|------|----------------|
| `part01_classical/` | 古典制御理論 | PID、ボード線図、安定性判別 |
| `part02_modern/`    | 現代制御理論 | 状態空間、LQR、カルマンフィルタ |
| `part03_adaptive/`  | 適応・ロバスト制御 | MRAC、H∞制御、L1制御 |
| `part04_digital/`   | デジタル制御と信号処理 | Z変換、FIR/IIR、FFT、離散PID |
| `part05_practical/` | 実装・演習編 | Python/ROS実装、マイコン制御、FPGA入門 |

---

### 🤖 第2部：AIによる制御（Part 2: AI-based Control）

| ディレクトリ名 | 内容 | 主なキーワード |
|----------------|------|----------------|
| `part06_nn_control/`     | ニューラルネット制御 | NN-PID、逆モデル、時系列制御 |
| `part07_rl_control/`     | 強化学習制御 | Q学習、DDPG、PPO、報酬設計 |
| `part08_data_driven/`    | データ駆動制御 | Koopman、行列識別、モデリング |
| `part09_llm_hybrid/`     | ハイブリッド・LLM統合制御 | FSM×PID×LLM、AITL構想、ChatGPT連携 |

---

## 🔧 推奨ツール / Tools

- Python：`control`, `scipy`, `matplotlib`, `torch`, `gymnasium`, `stable-baselines3`
- MATLAB / Simulink（オプション）
- Jupyter Notebook（演習と可視化）
- ROS（リアルタイム実装例）
- ChatGPT / GPT-4o（LLM連携）

---

## 🚀 特徴 / Features

- 🔁 古典〜AI制御を段階的に学べる構成
- 🧠 ChatGPTなどのLLMと連携した設計も可能
- 💡 直感的な演習を通じて理論と実装を接続
- 📚 授業・研修・自習に対応（MITライセンス）

---

## 📂 ディレクトリ構成（統一形式）

```
EduController/
├── part01_classical/        # 古典制御理論
├── part02_modern/           # 現代制御理論
├── part03_adaptive/         # 適応・ロバスト制御
├── part04_digital/          # デジタル制御とDSP
├── part05_practical/        # 実装・演習編
├── part06_nn_control/       # ニューラルネット制御
├── part07_rl_control/       # 強化学習による制御
├── part08_data_driven/      # データ駆動型制御
├── part09_llm_hybrid/       # LLM統合・AITL構想
└── README.md

```

---

## 🔖 ライセンス / License

MIT License © 2025 Shinichi Samizo  
本教材は教育・研究・個人学習の目的で自由にご利用いただけます。

---

## 📬 お問い合わせ

- GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)
- Email: shin3t72@gmail.com

---
