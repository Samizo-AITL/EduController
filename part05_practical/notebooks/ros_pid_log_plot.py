# ros_pid_log_plot.py
# ROSの /sensor_data, /motor_cmd を購読してプロットするNotebook用スクリプト

import rospy
from std_msgs.msg import Float32
import matplotlib.pyplot as plt
import threading
import time

# データバッファ
sensor_log = []
motor_log = []
time_log = []

start_time = time.time()

def sensor_callback(msg):
    t = time.time() - start_time
    sensor_log.append(msg.data)
    time_log.append(t)

def motor_callback(msg):
    motor_log.append(msg.data)

def ros_listener():
    rospy.init_node("ros_pid_plotter", anonymous=True)
    rospy.Subscriber("/sensor_data", Float32, sensor_callback)
    rospy.Subscriber("/motor_cmd", Float32, motor_callback)
    rospy.spin()

# 別スレッドでROS購読を開始
listener_thread = threading.Thread(target=ros_listener)
listener_thread.start()

print("📡 ROSトピックを購読中...10秒後に描画")

time.sleep(10)  # 一定時間データ収集

# プロット
plt.figure(figsize=(10, 5))
plt.plot(time_log, sensor_log, label="Sensor Data", linewidth=2)
plt.plot(time_log, motor_log[:len(time_log)], label="Motor Command", linewidth=2)
plt.xlabel("Time [s]")
plt.ylabel("Value")
plt.title("ROS PID Control - Sensor vs Command")
plt.grid()
plt.legend()
plt.show()

