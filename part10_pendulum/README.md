# 🎯 Part 10：倒立振子の総合制御（Hybrid Control of Inverted Pendulum）

本章では、**倒立振子（Inverted Pendulum）**を題材として、以下の制御手法を段階的に実装・比較します：

- 📐 **PID制御**（古典制御）
- 🧮 **LQR制御**（最適制御 / 状態空間）
- 🧠 **強化学習（DDPG, PPO）**
- ⚙️ **HDL実装（FSM×PID）**
- 🤖 **LLM連携による制御器設計**

> 実践的な不安定系のモデルを通じて、**制御理論とAI制御の統合的理解**を目指します。

---

## 🧭 構成概要

| ディレクトリ | 内容 |
|--------------|------|
| [`model/`](./model/) | 倒立振子の物理モデル（微分方程式、線形化） |
| [`classical_control/`](./classical_control/) | PID制御（Python, Simulink） |
| [`modern_control/`](./modern_control/) | LQR、カルマンフィルタ、状態空間設計 |
| [`rl_control/`](./rl_control/) | DDPG/PPOによる強化学習制御（gym環境） |
| [`hdl_implementation/`](./hdl_implementation/) | FSM・PIDベースのHDL制御器（Verilog） |
| [`llm_prompt_design/`](./llm_prompt_design/) | ChatGPT用プロンプトテンプレート（C→Verilog） |
| [`ros_simulation/`](./ros_simulation/) | ROS/Gazeboによる物理シミュレーション（拡張予定） |

---

## 🎓 学習のステップ

1. **モデル理解**：  
   倒立振子の数理モデルを構築し、状態方程式へ変換

2. **古典制御の実装**：  
   PID制御による初期安定化をPython・Simulinkで実施

3. **状態空間制御の適用**：  
   LQRによる最適制御器設計と、カルマンフィルタによる状態推定を導入

4. **強化学習との比較**：  
   DDPGやPPOを用いた自己学習型制御の導入と性能比較

5. **HDL実装への展開**：  
   FSMやPID制御器をVerilogで記述し、波形評価まで確認

6. **LLMとの連携**：  
   ChatGPTを用いた制御器設計支援と、自動コード生成を実験

---

## 🔧 実行環境

| 分類 | ツール群 | 用途 |
|------|----------|------|
| 🐍 Python | `control`, `scipy`, `gymnasium`, `torch` | PID / LQR / RL 実装 |
| 📊 Simulink | Simulink / Simscape | ブロック設計 / PIDモデル化 |
| 🔬 HDL | Verilog / GTKWave / ModelSim | HDL制御器実装・検証 |
| 🤖 LLM | ChatGPT (GPT-4o 推奨) | HDL設計支援・プロンプト設計 |
| 🤖 ROS | ROS2 / Gazebo | 実ロボットシミュレーション（拡張） |

---

## 📌 本章の目的

- ✅ 倒立振子という典型的不安定系を通じて「理論」と「実装」を結びつける
- ✅ PIDやLQRといった従来型制御と、RLやLLMを用いた次世代制御の接続を体験
- ✅ 制御器のHDL化や、設計支援としてのLLM活用を実践的に学ぶ

---

## 🔗 関連リンク

- [EduController トップへ戻る](../README.md)
- [AITL-H：FSM×PID×LLM 制御アーキテクチャ](https://github.com/Samizo-AITL/AITL-H)
- [SamizoGPT：ChatGPTプロンプト集](https://github.com/Samizo-AITL/SamizoGPT)

---

## 🖋️ 執筆者

**三溝 真一（Shinichi Samizo）**  
- [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/)
- [shin3t72@gmail.com](mailto:shin3t72@gmail.com)

---

## 📖 ライセンス

MIT License © 2025 [Shinichi Samizo](https://github.com/Samizo-AITL)  
教育・研究・個人学習を目的とした自由な利用を歓迎します。
