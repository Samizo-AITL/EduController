# 🤖 04. ROS制御ノードの設計とトピック通信（ROS Control Node Design）

本章では、**ROS（Robot Operating System）** を用いた制御構成の基本を解説します。  
センサ情報を購読し、制御演算を行ってアクチュエータに指令を送る「**制御ノード**」の設計を行います。

---

## 🎯 学習目標

- ROSノードとして制御器（PIDなど）を実装できる  
- センサデータの受信・処理・出力指令をトピックで構成できる  
- ノード間通信（Publisher / Subscriber）の基本構造を理解する  
- rqt_plot や rosbag による可視化・記録を行える

---

## 🧱 制御ノードの基本構成（例）

```text
[ センサノード ] --(トピック: /sensor_data)--> [ 🧠 制御ノード ] --(トピック: /motor_cmd)--> [ アクチュエータノード ]
```
	•	/sensor_data：角速度、距離、温度などの観測値（std_msgs/Float32 など）
	•	/motor_cmd：PWM値や電流指令など（std_msgs/Float32 or カスタム）

## 🧠 制御ノードのサンプルコード（PID制御）
```
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

## 🔧 起動・通信確認コマンド例
```
roscore
rosrun my_pkg pid_node.py
rostopic echo /motor_cmd
rqt_plot /sensor_data /motor_cmd
```

---

## 🧪 デバッグ・可視化ツール

ROSでは、ノード間通信の確認や制御挙動の可視化に便利なツールが多数用意されています。

| ツール名       | 役割・機能                          | 使用例                         |
|----------------|-------------------------------------|--------------------------------|
| `rqt_plot`     | トピックの時系列データをグラフ化    | `/sensor_data`, `/motor_cmd` を可視化 |
| `rostopic echo`| トピックの中身をターミナル表示     | `rostopic echo /motor_cmd`    |
| `rosbag`       | 通信内容を記録・再生                | 実験データの再検証に使用       |
| `rosparam`     | パラメータの取得・更新              | PIDゲインの動的変更            |
| `roslaunch`    | 複数ノードの一括起動                | 構成ファイルで起動を簡略化     |

> 🔍 ノード同士の接続状態は `rqt_graph` で視覚的に確認できます。

---

## 📘 応用例（統合制御）

ROS制御ノードは、以下のような**高度な制御構成**にも展開できます。

- **センサ融合**：IMU + カメラ → 状態推定ノードへ
- **車両制御**：`/cmd_vel` などの指令 → 左右モータ出力へ変換
- **MPC/RL連携**：モデル予測制御や強化学習ポリシーとの協調
- **LLM対話型制御**（AITL構想）との接続も可能

> 🧠 複数ノードを組み合わせたシステム構成により、**柔軟で拡張性のある知能制御**が実現できます。

---

## 📚 参考資料

- [ROS Wiki](https://wiki.ros.org/)
- [ROS 2 Tutorials](https://docs.ros.org/en/foxy/Tutorials.html)
- [rqt_plot - ROS Wiki](http://wiki.ros.org/rqt_plot)
- [rosbag - ロギング機能](http://wiki.ros.org/rosbag)
- 本教材との関連：
  - `part05_practical/simulation/ros_pid_node.py`
  - `part06_ai/`：AI制御・LLM統合への展開

---



