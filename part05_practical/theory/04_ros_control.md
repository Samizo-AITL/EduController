---
layout: default
title: "🤖 04. ROS制御ノードの設計とトピック通信（ROS Control Node Design）"
permalink: /part05_practical/theory/04_ros_control_node.html
---

---

# 🤖 04. ROS制御ノードの設計とトピック通信（ROS Control Node Design）

> ℹ️ **Webで数式やコードが正しく表示されない場合はこちら** → [GitHub版を見る](https://github.com/Samizo-AITL/EduController/blob/main/part05_practical/theory/04_ros_control_node.md)


本章では、**ROS（Robot Operating System）** を用いた制御構成の基本を解説します。  
センサ情報を購読し、制御演算を行ってアクチュエータに指令を送る「**制御ノード**」の設計を行います。

This section explains the basics of control architecture using **ROS**,  
focusing on designing **control nodes** that subscribe to sensor data, perform control calculations, and publish actuator commands.

---

## 🎯 学習目標 / Learning Objectives

- ROSノードとして制御器（PIDなど）を実装できる  
- センサデータの受信・処理・出力指令をトピックで構成できる  
- ノード間通信（Publisher / Subscriber）の基本構造を理解する  
- rqt_plot や rosbag による可視化・記録を行える  

---

## 🧱 制御ノードの基本構成（例） / Basic Control Node Structure

```text
[ センサノード ] --(トピック: /sensor_data)--> [ 🧠 制御ノード ] --(トピック: /motor_cmd)--> [ アクチュエータノード ]
```

- `/sensor_data`：角速度、距離、温度などの観測値（`std_msgs/Float32` など）  
- `/motor_cmd`：PWM値や電流指令など（`std_msgs/Float32` またはカスタム）

---

## 🧠 制御ノードのサンプルコード（PID制御） / PID Control Node Example

```python
# pid_node.py
import rospy
from std_msgs.msg import Float32

class PIDNode:
    def __init__(self):
        self.kp = rospy.get_param("~kp", 1.0)
        self.ki = rospy.get_param("~ki", 0.0)
        self.kd = rospy.get_param("~kd", 0.0)
        self.target = rospy.get_param("~target", 0.0)

        self.e_prev = 0
        self.e_sum = 0
        self.dt = 0.05

        self.sub = rospy.Subscriber("/sensor_data", Float32, self.callback)
        self.pub = rospy.Publisher("/motor_cmd", Float32, queue_size=10)

    def callback(self, msg):
        e = self.target - msg.data
        self.e_sum += e * self.dt
        de = (e - self.e_prev) / self.dt
        u = self.kp * e + self.ki * self.e_sum + self.kd * de
        self.e_prev = e
        self.pub.publish(u)

if __name__ == '__main__':
    rospy.init_node("pid_node")
    node = PIDNode()
    rospy.spin()
```

---

## 🔧 起動・通信確認コマンド例 / Run & Verify

```bash
roscore
rosrun my_pkg pid_node.py
rostopic echo /motor_cmd
rqt_plot /sensor_data /motor_cmd
```

---

## 🧪 デバッグ・可視化ツール / Debug & Visualization Tools

| ツール名 / Tool  | 機能 / Function                          | 使用例 / Example                  |
|------------------|------------------------------------------|------------------------------------|
| `rqt_plot`       | トピックの時系列データ可視化             | `/sensor_data`, `/motor_cmd`       |
| `rostopic echo`  | トピックの中身をターミナル表示           | `rostopic echo /motor_cmd`         |
| `rosbag`         | 通信内容の記録・再生                     | 実験データの保存・再解析           |
| `rosparam`       | パラメータの取得・更新                   | PIDゲインの動的調整                 |
| `roslaunch`      | 複数ノードの一括起動                     | 構成ファイルで簡略化                |

💡 ノード接続状態は `rqt_graph` で視覚的に確認可能。

---

## 📘 応用例（統合制御） / Advanced Use Cases

- **センサ融合**：IMU + カメラ → 状態推定ノードへ  
- **車両制御**：`/cmd_vel` → 左右モータ出力へ変換  
- **MPC/RL連携**：モデル予測制御や強化学習との統合  
- **LLM対話型制御**（AITL構想）との接続  

> 🧠 複数ノード構成により、柔軟かつ拡張性の高い知能制御が可能。

---

## 📚 参考 / References

- [ROS Wiki](https://wiki.ros.org/)  
- [ROS 2 Tutorials](https://docs.ros.org/en/foxy/Tutorials.html)  
- [rqt_plot - ROS Wiki](http://wiki.ros.org/rqt_plot)  
- [rosbag - Logging](http://wiki.ros.org/rosbag)  
- 本教材関連:  
  - `part05_practical/simulation/ros_pid_node.py`  
  - `part06_ai/`（AI制御・LLM統合）

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part05_practical/theory/03_embedded_control.html)**  
組込み制御への展開（C/Arduino実装）。

**🏠 [第5章トップ / Back to Part 5 Top](https://samizo-aitl.github.io/EduController/part05_practical/)**
