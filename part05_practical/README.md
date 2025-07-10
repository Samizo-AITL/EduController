# 🧪 Part 5: 実装・応用編（Implementation and Applications）

この章では、制御理論を実際のシステムに適用するための  
**Python実装・マイコン展開・ROS連携** などの実践的な応用手法を学びます。

---

## 📚 本章の構成

| セクション                     | 内容                                    |
|-------------------------------|-----------------------------------------|
| [01_simulation_setup.md](theory/01_simulation_setup.md) | Python制御シミュレーションの環境構築     |
| [02_python_control.md](theory/02_python_control.md)     | Pythonによる制御設計の実装方法           |
| [03_embedded_control.md](theory/03_embedded_control.md) | Arduino等のマイコン向け制御展開          |
| [04_ros_control.md](theory/04_ros_control.md)           | ROS制御ノードの設計と通信構成            |

---

## 💻 実装・シミュレーションコード

| ファイル名                                                   | 内容                             |
|--------------------------------------------------------------|----------------------------------|
| [dc_motor_sim.py](simulation/dc_motor_sim.py)                | 状態空間モデルによるDCモータ制御 |
| [ros_pid_node.py](simulation/ros_pid_node.py)                | ROS用PID制御ノード実装           |

---

## 📊 ノートブック・図解

| ディレクトリ                | 内容                             |
|-----------------------------|----------------------------------|
| [notebooks/](notebooks/)    | 制御可視化や検証用のJupyter演習 |
| [figures/](figures/)        | 制御ブロック図・構成図等の図版  |

---

## 🔧 使用ライブラリ・ツール

- Python: `control`, `matplotlib`, `pyserial`
- ROS1 (Noetic) / ROS2 (Foxy)
- Arduino IDE / STM32CubeIDE
- `rqt_plot`, `rosbag`, `rosparam`

---

## 🧪 実験の流れ

1. Pythonで制御モデルを実装・確認
2. 組み込み向けに離散PID等を移植
3. ROSノード化してセンサ/アクチュエータと接続
4. 可視化・ロギングで実験を支援
5. [Part06](../part06_ai/) へ接続し、AI制御へ展開

---

## 🔗 関連章・接続

| 章                     | 内容                             |
|------------------------|----------------------------------|
| [Part 4: Digital Control](../part04_digital/) | 離散制御理論・Z変換                   |
| [Part 6: AI Control](../part06_ai/)          | ニューラル・強化学習・DNN制御         |
| [Part 9: LLM統合](../part09_llm/)            | ChatGPT等との統合型制御（AITL構想）   |

---

## 📬 メンテナンス・著作権

- 制作者：三溝 真一（Samizo Shinichi）  
- GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
- Email: [shin3t72@gmail.com](mailto:shin3t72@gmail.com)  
- ライセンス：MIT License

---
