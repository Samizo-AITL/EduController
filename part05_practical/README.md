# 🧪 Part 5: 実装・応用編 / Implementation and Applications

この章では、制御理論を実際のシステムに適用するための  
**Python実装・マイコン展開・ROS連携** などの実践的な応用手法を学びます。

This chapter focuses on **practical implementation methods** such as  
**Python coding, embedded systems deployment, and ROS integration** for applying control theory to real systems.

---

## 📚 **本章の構成 / Chapter Structure** [`theory/`](./theory/)

| **セクション / Section** | **内容 / Description** |
|--------------------------|-------------------------|
| [`01_simulation_setup.md`](theory/01_simulation_setup.md) | Python制御シミュレーションの環境構築<br>Setting up a Python-based control simulation |
| [`02_python_control.md`](theory/02_python_control.md)     | Pythonによる制御設計の実装方法<br>Implementing control design with Python |
| [`03_embedded_control.md`](theory/03_embedded_control.md) | Arduino等のマイコン向け制御展開<br>Control deployment on microcontrollers like Arduino |
| [`04_ros_control.md`](theory/04_ros_control.md)           | ROS制御ノードの設計と通信構成<br>Designing ROS control nodes and communication layout |

---

## 💻 **実装・シミュレーションコード / Implementation & Simulation** [`simulation/`](./simulation/)

| **ファイル名 / Script** | **内容 / Description** |
|--------------------------|-------------------------|
| [`dc_motor_sim.py`](simulation/dc_motor_sim.py) | 状態空間モデルによるDCモータ制御<br>DC motor control using state-space model |
| [`ros_pid_node.py`](simulation/ros_pid_node.py) | ROS用PID制御ノード実装<br>PID control node implementation for ROS |

---

## 📊 **ノートブック・図解 / Notebooks & Visuals**

| **ファイル名** | **内容 / Description** |
|----------------|-------------------------|
| [`ros_pid_log_plot.py`](notebooks/ros_pid_log_plot.py) | ROSトピック可視化スクリプト（.py版）<br>Python script for ROS topic visualization |
| [`ros_pid_log_plot.ipynb`](notebooks/ros_pid_log_plot.ipynb) | 上記のNotebook形式<br>Notebook version of the above for log analysis |
| [`figures/`](figures/) | 制御ブロック図・構成図などの図版<br>Figures including block diagrams and architecture charts |

---

## 🔧 **使用ライブラリ・ツール / Libraries & Tools**

- **Python**: `control`, `matplotlib`, `pyserial`  
- **ROS1 (Noetic)** / **ROS2 (Foxy)**  
- **Arduino IDE**, **STM32CubeIDE**  
- **補助ツール / Utilities**: `rqt_plot`, `rosbag`, `rosparam`

---

## 🧪 **実験の流れ / Implementation Flow**

1. Pythonで制御モデルを**設計・シミュレーション**  
   *Design and simulate control models using Python*  
2. 制御アルゴリズムを**マイコンに移植（離散化含む）**  
   *Port controllers to microcontrollers with discretization*  
3. **ROSノード化**してセンサやアクチュエータと接続  
   *Integrate with ROS and connect to sensors/actuators*  
4. `rqt_plot`や`rosbag`で**可視化・ロギング**  
   *Visualize and log using rqt_plot and rosbag*  
5. [Part 6](../part06_ai/) に接続し、**AI制御へ展開**  
   *Connect to Part 6 for AI-based control integration*

---

## 🔗 **関連章・接続 / Related Parts**

| **章 / Chapter** | **内容 / Description** |
|------------------|-------------------------|
| [Part 4: Digital Control](../part04_digital/) | 離散制御理論・Z変換<br>Digital control theory and Z-transform |
| [Part 6: AI Control](../part06_ai/) | ニューラル・強化学習・DNN制御<br>Neural networks, reinforcement learning, DNN-based control |
| [Part 9: LLM統合](../part09_llm/) | ChatGPT等との統合型制御（AITL構想）<br>LLM-integrated control systems (AITL concept) |

---

## 👤 **著者・ライセンス / Author & License**

| **項目 / Item** | **内容 / Details** |
|------------------|---------------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo）<br>Shinshu University / Ex-Epson |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

📎 **[トップに戻る / Back to Home](../README.md)**
