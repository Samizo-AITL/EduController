---
layout: default
title: Part10
permalink: /part10_pendulum/
---

---

# 🎯 Part 10：倒立振子の総合制御 / Hybrid Control of Inverted Pendulum

---

本章では、**倒立振子（Inverted Pendulum）** を題材として、  
以下の制御手法を段階的に**実装・比較**しながら学びます：

- 📐 **PID制御**（古典制御 / Classical Control）  
- 🧮 **LQR制御**（最適制御 / Optimal Control）  
- 🧠 **強化学習（DDPG, PPO） / Reinforcement Learning**  
- ⚙️ **HDL実装（FSM×PID） / HDL-based FSM×PID Implementation**  
- 🤖 **LLM連携による制御設計 / Control Design with LLMs**

> 本章は、**不安定系の代表例を通じて制御理論とAI制御を統合的に学ぶ**ことを目的とします。  
> Through this unstable system model, we aim to understand and integrate both classical and AI-based control approaches.

---

## 🧭 **構成概要 / Structure Overview**

| ディレクトリ / Directory | 内容 / Description |
|--------------------------|---------------------|
| [`model/`](https://samizo-aitl.github.io/EduController/part10_pendulum/model/) | 倒立振子の物理モデルと線形化<br>Physics-based modeling and linearization |
| [`classical_control/`](https://samizo-aitl.github.io/EduController/part10_pendulum/classical_control/) | PID制御の設計と応答解析<br>PID implementation and analysis |
| [`modern_control/`](https://samizo-aitl.github.io/EduController/part10_pendulum/modern_control/) | LQR制御・状態推定（カルマン）<br>LQR & Kalman filtering |
| [`rl_control/`](https://samizo-aitl.github.io/EduController/part10_pendulum/rl_control/) | Gymを用いたDDPG・PPO制御<br>RL control using Gym |
| [`hdl_implementation/`](https://samizo-aitl.github.io/EduController/part10_pendulum/hdl_implementation/) | FSM×PIDのVerilog記述<br>Verilog HDL implementation |
| [`llm_prompt_design/`](https://samizo-aitl.github.io/EduController/part10_pendulum/llm_prompt_design/) | LLMによるコード設計支援<br>Code generation with LLM prompts |
| [`ros_simulation/`](https://samizo-aitl.github.io/EduController/part10_pendulum/ros_simulation/) | ROS/Gazeboによる物理シミュレーション（予定）<br>ROS/Gazebo physical simulation (planned) |

---

## 🎓 **学習のステップ / Learning Workflow**

1. **モデル構築 / Modeling**  
   - 倒立振子の数理モデル化と線形近似  
   - Build mathematical models and linearize the pendulum system  

2. **PID制御 / Classical PID**  
   - Python・SimulinkによるPID設計・応答解析  
   - Design PID controllers in Python/Simulink  

3. **状態空間制御 / State-Space Control**  
   - LQR設計・カルマンフィルタによる推定器構築  
   - Design LQR controllers and state estimators  

4. **強化学習 / Reinforcement Learning**  
   - Gym/PyTorchでのDDPG・PPO訓練と評価  
   - Train DDPG/PPO agents for stabilization  

5. **HDL設計 / HDL Implementation**  
   - FSM＋PID制御器をVerilogで実装、GTKW・ModelSimで波形確認  
   - Implement HDL-based control using Verilog and testbench tools  

6. **LLM連携 / LLM Integration**  
   - ChatGPTを活用したプロンプト設計、Verilog自動生成支援  
   - Use ChatGPT for prompt-based Verilog code generation

---

## 🔧 **実行環境 / Execution Environment**

| 分類 / Type | ツール / Tools | 用途 / Purpose |
|-------------|----------------|----------------|
| 🐍 Python | `control`, `gymnasium`, `torch`, `matplotlib` | 制御器設計・学習 |
| 📊 Simulink | Simulink / Simscape | ブロック設計・応答解析 |
| 🔬 HDL | Verilog / GTKWave / ModelSim | HDL記述・波形検証 |
| 🤖 LLM | ChatGPT（GPT-4o推奨） | プロンプト設計支援 |
| 🧪 ROS | ROS2 / Gazebo | 拡張用の物理シミュレーション |

---

## 📌 **本章の目的 / Purpose of This Chapter**

- ✅ **理論と実装の統合**：倒立振子を通じて物理・状態空間・HDLを接続  
  Bridge theory and practice through inverted pendulum control  
- ✅ **多様な制御手法の比較体験**：PID、LQR、RLの効果を可視的に理解  
  Visually compare classical and AI control techniques  
- ✅ **LLM活用による設計支援**：LLMによる自動化・設計提案を体験  
  Leverage LLMs to support control design and code generation  

---

## 🚀 **今後の展開 / Future Expansions**

（中略：内容は同じ）

---

## 🔗 **関連リンク / Related Links**

- 📚 [EduController トップへ戻る / Back to EduController Home](https://samizo-aitl.github.io/EduController/)  
- 🤖 [AITL-H: FSM × PID × LLM アーキテクチャ](https://github.com/Samizo-AITL/AITL-H)  
- ✏️ [SamizoGPT: ChatGPT プロンプト集](https://github.com/Samizo-AITL/SamizoGPT)

---

**⬅️ [前章 / Previous Chapter](https://samizo-aitl.github.io/EduController/part09_llm_hybrid/)**  
LLM統合・ハイブリッド制御（FSM×PID×LLMなど）を扱います。  
Covers LLM-integrated hybrid control such as FSM×PID×LLM.

**🏠 [トップページ / Back to Home](https://samizo-aitl.github.io/EduController/)**
