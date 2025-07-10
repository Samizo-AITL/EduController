# nn_pid_control.py
# ニューラルネットでPID制御器を補完する構成（PyTorch使用）

import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# NN-PID制御器
class NNPIDController(nn.Module):
    def __init__(self, input_dim=3, hidden_dim=32):
        super(NNPIDController, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )

    def forward(self, error, derror, ierror):
        x = torch.tensor([error, derror, ierror], dtype=torch.float32)
        return self.net(x)

# シンプルな1次遅れモデル
class Plant:
    def __init__(self, a=0.9):
        self.y = 0.0
        self.a = a

    def step(self, u):
        self.y = self.a * self.y + (1 - self.a) * u
        return self.y

# 制御シミュレーション
def run_simulation(controller, plant, ref=1.0, steps=100):
    y_log, u_log = [], []
    integral = 0.0
    prev_error = 0.0

    for t in range(steps):
        error = ref - plant.y
        derivative = error - prev_error
        integral += error
        prev_error = error

        u = controller(error, derivative, integral)
        u = u.item()
        y = plant.step(u)

        y_log.append(y)
        u_log.append(u)

    return y_log, u_log

# 実行
if __name__ == "__main__":
    torch.manual_seed(0)
    controller = NNPIDController()
    plant = Plant()

    y_log, u_log = run_simulation(controller, plant)

    plt.figure()
    plt.plot(y_log, label="Output y(t)")
    plt.plot(u_log, label="Control u(t)")
    plt.legend()
    plt.grid()
    plt.title("NN-PID Control Simulation")
    plt.xlabel("Time Step")
    plt.show()
