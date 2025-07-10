#!/usr/bin/env python
# coding: utf-8

import rospy
from std_msgs.msg import Float32

class PIDController:
    def __init__(self):
        # パラメータ読み込み（launchやrosparamから設定可能）
        self.kp = rospy.get_param("~kp", 1.0)
        self.ki = rospy.get_param("~ki", 0.0)
        self.kd = rospy.get_param("~kd", 0.0)
        self.target = rospy.get_param("~target", 0.0)
        self.dt = rospy.get_param("~dt", 0.05)  # 制御周期 [s]

        self.integral = 0.0
        self.prev_error = 0.0

        # Publisher: モータ出力など
        self.pub = rospy.Publisher("/motor_cmd", Float32, queue_size=10)

        # Subscriber: センサデータ入力
        self.sub = rospy.Subscriber("/sensor_data", Float32, self.control_callback)

        rospy.loginfo("PID Controller initialized.")

    def control_callback(self, msg):
        # 誤差計算
        error = self.target - msg.data
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt

        # PID計算
        u = self.kp * error + self.ki * self.integral + self.kd * derivative

        # 出力
        self.pub.publish(Float32(u))
        self.prev_error = error

        rospy.loginfo(f"[PID] Error={error:.3f}, U={u:.3f}")

if __name__ == '__main__':
    rospy.init_node("ros_pid_node")
    try:
        controller = PIDController()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
