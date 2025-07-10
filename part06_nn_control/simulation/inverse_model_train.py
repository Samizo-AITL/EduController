# inverse_model_train.py
# ニューラルネットによる逆モデル制御の学習スクリプト

import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

# 1次遅れ系の順モデル
class Plant:
    def __init__(self, a=0.9):
        self.y = 0.0
        self.a = a

    def step(self, u):
        self.y = self.a * self.y + (1 - self.a) * u
        return self.y

# 逆モデルNN（入力: 目標出力 y_d(t)、出力: u(t)）
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

# 訓練データ生成
def generate_data(plant, N=200):
    yd_list, u_list = [], []

    for _ in range(N):
        yd = np.random.uniform(0, 1)
        # 逆推定：uを試して最も近いものを記録（簡易逆モデル）
        best_u, best_diff = 0.0, float('inf')
        for u_try in np.linspace(0, 1, 100):
            y_out = plant.a * plant.y + (1 - plant.a) * u_try
            if abs(y_out - yd) < best_diff:
                best_u = u_try
                best_diff = abs(y_out - yd)
        yd_list.append(yd)
        u_list.append(best_u)

    return torch.tensor(yd_list).unsqueeze(1), torch.tensor(u_list).unsqueeze(1)

# 学習ループ
def train_model(model, yd_train, u_train, epochs=1000):
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    loss_fn = nn.MSELoss()
    losses = []

    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(yd_train).squeeze()
        loss = loss_fn(outputs, u_train.squeeze())
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
    return losses

# 実行
if __name__ == "__main__":
    plant = Plant()
    model = InverseModel()
    yd_train, u_train = generate_data(plant, N=300)
    losses = train_model(model, yd_train, u_train, epochs=500)

    # 損失可視化
    plt.figure()
    plt.plot(losses)
    plt.xlabel("Epoch")
    plt.ylabel("MSE Loss")
    plt.title("Inverse Model Training Loss")
    plt.grid()
    plt.show()

    # 学習結果の可視化
    yds = torch.linspace(0, 1, 100).unsqueeze(1)
    preds = model(yds).detach().numpy()

    plt.figure()
    plt.plot(yds.numpy(), preds, label="Predicted u(t)")
    plt.xlabel("Desired Output y_d(t)")
    plt.ylabel("Estimated Input u(t)")
    plt.title("Inverse Model Prediction")
    plt.grid()
    plt.legend()
    plt.show()
  
