# ai_vs_pid_sim.py
# NN逆モデル制御とPID制御の比較シミュレーション

import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# NN逆モデル（事前訓練済みを想定）
class InverseModel(nn.Module):
    def __init__(self, hidden_dim=32):
        super(InverseModel, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(1, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1)
        )

    def forward(self, yd):
        return self.net(torch.tensor([yd], dtype=torch.float32))

# プラント（1次遅れ系）
class Plant:
    def __init__(self, a=0.9):
        self.y = 0.0
        self.a = a

    def step(self, u):
        self.y = self.a * self.y + (1 - self.a) * u
        return self.y

# PID制御器
class PID:
    def __init__(self, Kp=2.0, Ki=0.0, Kd=0.0):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, ref, y):
        error = ref - y
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return self.Kp * error + self.Ki * self.integral + self.Kd * derivative

# 比較シミュレーション
def run_comparison(model, plant_model, pid, steps=100, ref=1.0):
    # NN制御
    y_nn_log = []
    plant_nn = Plant()
    for _ in range(steps):
        u_nn = model(torch.tensor([ref], dtype=torch.float32)).item()
        y_nn = plant_nn.step(u_nn)
        y_nn_log.append(y_nn)

    # PID制御
    y_pid_log = []
    plant_pid = Plant()
    for _ in range(steps):
        u_pid = pid.compute(ref, plant_pid.y)
        y_pid = plant_pid.step(u_pid)
        y_pid_log.append(y_pid)

    return y_nn_log, y_pid_log

# 実行
if __name__ == "__main__":
    torch.manual_seed(0)
    model = InverseModel()
    model.load_state_dict(torch.load("inverse_model.pth"))  # 学習済みモデルを読み込む前提
    model.eval()

    pid = PID(Kp=2.0, Ki=0.1, Kd=0.0)

    y_nn_log, y_pid_log = run_comparison(model, Plant, pid)

    # プロット
    plt.figure()
    plt.plot(y_nn_log, label="NN Inverse Model")
    plt.plot(y_pid_log, label="PID Control", linestyle="--")
    plt.axhline(1.0, color="gray", linestyle=":", label="Reference")
    plt.xlabel("Time Step")
    plt.ylabel("Output y(t)")
    plt.title("NN vs PID Control")
    plt.grid()
    plt.legend()
    plt.show()
  
