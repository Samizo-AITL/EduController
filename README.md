# 🎛️ EduController：制御理論とAI制御の教育フレームワーク

**EduController** は、古典制御から現代制御、さらにAIベースの次世代型制御までを体系的に学べる、**段階的・実践的な制御教育教材プロジェクト**です。  
Pythonを活用し、制御理論の直感的理解からAI統合型制御設計までをサポートします。

---

## 🧭 構成概要：制御理論とAI制御の2系統

EduControllerは、全9章から構成され、以下の2系統に分類されます：

- 🎓 **制御理論系（Part 01〜05）**  
  古典制御から現代制御、デジタル制御・実装技術までの体系的な章群

- 🤖 **AI制御系（Part 06〜09）**  
  ニューラルネット・強化学習・データ駆動・LLM統合など、AIによる次世代制御手法を扱う章群

※各章は独立して学べますが、AI制御系は制御理論の基礎知識を前提とします。

---

## 📚 章構成一覧（リンク付き）

### 🎓 制御理論系（Control Theory）

| 章 | ディレクトリ | 内容概要 |
|----|----------------|----------|
| Part 01 | [part01_classical](./part01_classical/) | 古典制御理論（PID、周波数解析、安定性） |
| Part 02 | [part02_modern](./part02_modern/) | 現代制御理論（状態空間、LQR、カルマン） |
| Part 03 | [part03_adaptive](./part03_adaptive/) | 適応・ロバスト制御（MRAC、H∞、L1） |
| Part 04 | [part04_digital](./part04_digital/) | デジタル制御とDSP（Z変換、FFTなど） |
| Part 05 | [part05_practical](./part05_practical/) | 実装・演習編（Python、ROS、FPGAなど） |

---

### 🤖 AI制御系（AI-based Control）

| 章 | ディレクトリ | 内容概要 |
|----|----------------|----------|
| Part 06 | [part06_nn_control](./part06_nn_control/) | ニューラルネット制御（NN-PID、逆モデル） |
| Part 07 | [part07_rl_control](./part07_rl_control/) | 強化学習制御（Q学習、DDPG、PPO） |
| Part 08 | [part08_data_driven](./part08_data_driven/) | データ駆動制御（Koopman、行列識別） |
| Part 09 | [part09_llm_hybrid](./part09_llm_hybrid/) | LLM統合・ハイブリッド制御（FSM×PID×LLM） |

---

## 🔧 推奨ツール / Tools

- Python：`control`, `scipy`, `matplotlib`, `torch`, `gymnasium`, `stable-baselines3`
- Jupyter Notebook（演習と可視化）
- ROS（リアルタイム実装例）
- MATLAB / Simulink（オプション）
- ChatGPT / GPT-4o（LLM連携）

---

## 🚀 特徴 / Features

- 🔁 古典〜AI制御を段階的に学べる構成
- 🧠 ChatGPTなどのLLMと連携した設計も可能
- 💡 直感的な演習を通じて理論と実装を接続
- 📚 授業・研修・自習に対応（MITライセンス）

---

## 🔗 関連プロジェクト / Related Projects

EduControllerは、以下のプロジェクトと連携・相互参照されています：

### 🧩 [Edusemi v4.x](https://github.com/Samizo-AITL/Edusemi-v4x)  
半導体教育に特化した教材プロジェクト。プロセス・回路・レイアウト設計を横断的に扱い、Python自動化やSoC設計も含まれます。  
**特別編では、AITL-H構想やLLM連携制御とも統合**されています。

### 🤖 [AITL-H：Hybrid型知能制御](https://github.com/Samizo-AITL/AITL-H)  
人型ロボットなどに向けた**階層型構造知能制御フレームワーク**。  
**FSM（本能）＋PID（理性）＋LLM（知性）**の3層によるハイブリッド制御を提案し、本教材の最終章（Part 09）と連動しています。

---

## 🔖 ライセンス / License

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
本教材は教育・研究・個人学習の目的で自由にご利用いただけます。

---

## 🧑‍🔬 執筆者情報

- **氏名**：三溝 真一（Shinichi Samizo）
- **学歴**：信州大学大学院 電気電子工学修士課程 修了
- **職歴**：  
　1997年 セイコーエプソン株式会社 入社  
　以下の開発・製品化に従事：  
　- 半導体デバイス技術（0.35µm〜0.18µmノード）  
　- ロジックデバイス、メモリデバイス、高耐圧インテグレーション技術の開発・量産化  
　- インクジェット薄膜ピエゾアクチュエータ開発  
　- PrecisionCoreプリントヘッド製品展開にも参画
 - **連絡先**：  
　GitHub：[Samizo-AITL](https://github.com/Samizo-AITL)  
  Email: [shin3t72@gmail.com](mailto:shin3t72@gmail.com)

---

