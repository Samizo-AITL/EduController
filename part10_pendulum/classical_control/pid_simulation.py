# pid_simulation.py
# 倒立振子のカート位置制御に対するPID制御の例

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 倒立振子（Cart-Pole）の簡略化モデル：カートの位置制御のみを対象とする

# PID制御器クラス
class PID:
    def __init__(self, Kp, Ki, Kd, dt):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, setpoint, measured):
        error = setpoint - measured
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

# システムの微分方程式（カート＋線形近似された倒立振子の運動方程式）
def cart_pendulum_system(X, t, pid, M=1.0, m=0.1, l=0.5, g=9.81):
    x, x_dot, theta, theta_dot = X
    u = pid.compute(0.0, x)  # カート位置を原点に制御

    # 非線形式の簡略化（近似線形系）
    x_ddot = (u + m * l * theta_dot**2 * np.sin(theta) - m * g * np.sin(theta) * np.cos(theta)) / (M + m * (1 - np.cos(theta)**2))
    theta_ddot = ((M + m) * g * np.sin(theta) - np.cos(theta) * (u + m * l * theta_dot**2 * np.sin(theta))) / (l * (M + m * (1 - np.cos(theta)**2)))

    return [x_dot, x_ddot, theta_dot, theta_ddot]

# 初期状態
X0 = [0.2, 0.0, 0.1, 0.0]  # カート位置0.2m, 振子角0.1rad

# 時間軸
dt = 0.01
t = np.arange(0, 10, dt)

# PID制御器インスタンス
pid = PID(Kp=50.0, Ki=1.0, Kd=10.0, dt=dt)

# 微分方程式を数値積分
X = odeint(cart_pendulum_system, X0, t, args=(pid,))

# 結果をプロット
x = X[:,0]
theta = X[:,2]

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(t, x)
plt.title("Cart Position x(t)")
plt.xlabel("Time [s]")
plt.ylabel("x [m]")
plt.grid()

plt.subplot(1,2,2)
plt.plot(t, theta)
plt.title("Pendulum Angle θ(t)")
plt.xlabel("Time [s]")
plt.ylabel("θ [rad]")
plt.grid()

plt.tight_layout()
plt.show()
