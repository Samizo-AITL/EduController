# 🧪 Part 5: 実装・応用編 / Implementation and Applications
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)

---

この章では、制御理論を実際のシステムに適用するための  
**Python実装・マイコン展開・ROS連携** などの実践的な応用手法を学びます。

This chapter focuses on **practical implementation methods** such as  
**Python coding, embedded systems deployment, and ROS integration** for applying control theory to real systems.

---

## 📚 **本章の構成 / Chapter Structure** [`theory/`](https://samizo-aitl.github.io/EduController/part05_practical/theory/)

| **セクション / Section** | **内容 / Description** |
|--------------------------|-------------------------|
| [`01_simulation_setup.md`](https://samizo-aitl.github.io/EduController/part05_practical/theory/01_simulation_setup.html) | Python制御シミュレーションの環境構築<br>Setting up a Python-based control simulation |
| [`02_python_control.md`](https://samizo-aitl.github.io/EduController/part05_practical/theory/02_python_control.html) | Pythonによる制御設計の実装方法<br>Implementing control design with Python |
| [`03_embedded_control.md`](https://samizo-aitl.github.io/EduController/part05_practical/theory/03_embedded_control.html) | Arduino等のマイコン向け制御展開<br>Control deployment on microcontrollers like Arduino |
| [`04_ros_control.md`](https://samizo-aitl.github.io/EduController/part05_practical/theory/04_ros_control.html) | ROS制御ノードの設計と通信構成<br>Designing ROS control nodes and communication layout |

---

## 💻 **実装・シミュレーションコード / Implementation & Simulation** [`simulation/`](https://samizo-aitl.github.io/EduController/part05_practical/simulation/)

| **ファイル名 / Script** | **内容 / Description** |
|--------------------------|-------------------------|
| [`dc_motor_sim.py`](https://samizo-aitl.github.io/EduController/part05_practical/simulation/dc_motor_sim.py) | 状態空間モデルによるDCモータ制御<br>DC motor control using state-space model |
| [`ros_pid_node.py`](https://samizo-aitl.github.io/EduController/part05_practical/simulation/ros_pid_node.py) | ROS用PID制御ノード実装<br>PID control node implementation for ROS |

---

## 📊 **ノートブック・図解 / Notebooks & Visuals**

| **ファイル名** | **内容 / Description** |
|----------------|-------------------------|
| [`ros_pid_log_plot.py`](https://samizo-aitl.github.io/EduController/part05_practical/notebooks/ros_pid_log_plot.py) | ROSトピック可視化スクリプト（.py版）<br>Python script for ROS topic visualization |
| [`ros_pid_log_plot.ipynb`](https://samizo-aitl.github.io/EduController/part05_practical/notebooks/ros_pid_log_plot.ipynb) | 上記のNotebook形式<br>Notebook version of the above for log analysis |
| [`figures/`](https://samizo-aitl.github.io/EduController/part05_practical/figures/) | 制御ブロック図・構成図などの図版<br>Figures including block diagrams and architecture charts |

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
5. [Part 6](https://samizo-aitl.github.io/EduController/part06_ai/) に接続し、**AI制御へ展開**  
   *Connect to Part 6 for AI-based control integration*

---

## 🔗 **関連章・接続 / Related Parts**

| **章 / Chapter** | **内容 / Description** |
|------------------|-------------------------|
| [Part 4: Digital Control](https://samizo-aitl.github.io/EduController/part04_digital/) | 離散制御理論・Z変換<br>Digital control theory and Z-transform |
| [Part 6: AI Control](https://samizo-aitl.github.io/EduController/part06_ai/) | ニューラル・強化学習・DNN制御<br>Neural networks, reinforcement learning, DNN-based control |
| [Part 9: LLM統合](https://samizo-aitl.github.io/EduController/part09_llm/) | ChatGPT等との統合型制御（AITL構想）<br>LLM-integrated control systems (AITL concept) |

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 **ライセンス / License**
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](#-ライセンス--license)  

> 教材・コード・図表の性質に応じたハイブリッドライセンスを採用。  
> *Hybrid licensing based on the nature of the materials, code, and diagrams.*

| 📌 項目 / Item | ライセンス / License | 説明 / Description |
|------|------|------|
| **コード（Code）** | [MIT License](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布が可能<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 著者表示必須<br>*Attribution required* |
| **図表・イラスト（Figures & diagrams）** | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ許可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

**⬅️ [前章 / Previous Chapter](https://samizo-aitl.github.io/EduController/part04_digital/)**  
デジタル制御の基礎、Z変換、DSP実装など、離散時間系の制御と実装方法を学びます。  
Covers the basics of digital control, Z-transform, and DSP implementation for discrete-time systems.

**[次章 / Next Chapter ➡️➡️](https://samizo-aitl.github.io/EduController/part06_nn_control/)**  
ニューラルネットワークを利用した制御（NN-PID、逆モデル制御など）を扱います。  
Covers neural network-based control methods such as NN-PID and inverse model control.

**🏠 [トップページ / Back to Home](https://samizo-aitl.github.io/EduController/)**

