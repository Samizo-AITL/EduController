{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a3fe08e4",
   "metadata": {},
   "source": [
    "# 📈 NN-PID Controller Training\n",
    "このNotebookでは、PyTorchを用いた簡易NN-PID制御器の挙動と応答を可視化します。\n",
    "入力には、誤差、微分誤差、積分誤差を使用し、MLPを通じて制御入力を出力します。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb47187e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import torch\n",
    "import torch.nn as nn\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# NN構造\n",
    "class NNPIDController(nn.Module):\n",
    "    def __init__(self, input_dim=3, hidden_dim=32):\n",
    "        super(NNPIDController, self).__init__()\n",
    "        self.net = nn.Sequential(\n",
    "            nn.Linear(input_dim, hidden_dim),\n",
    "            nn.ReLU(),\n",
    "            nn.Linear(hidden_dim, 1)\n",
    "        )\n",
    "\n",
    "    def forward(self, error, derror, ierror):\n",
    "        x = torch.tensor([error, derror, ierror], dtype=torch.float32)\n",
    "        return self.net(x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0cd5a1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# プラント：一次遅れ系\n",
    "class Plant:\n",
    "    def __init__(self, a=0.9):\n",
    "        self.y = 0.0\n",
    "        self.a = a\n",
    "\n",
    "    def step(self, u):\n",
    "        self.y = self.a * self.y + (1 - self.a) * u\n",
    "        return self.y\n",
    "\n",
    "# シミュレーション関数\n",
    "def run_simulation(controller, plant, ref=1.0, steps=100):\n",
    "    y_log, u_log = [], []\n",
    "    integral = 0.0\n",
    "    prev_error = 0.0\n",
    "\n",
    "    for t in range(steps):\n",
    "        error = ref - plant.y\n",
    "        derivative = error - prev_error\n",
    "        integral += error\n",
    "        prev_error = error\n",
    "\n",
    "        u = controller(error, derivative, integral).item()\n",
    "        y = plant.step(u)\n",
    "\n",
    "        y_log.append(y)\n",
    "        u_log.append(u)\n",
    "\n",
    "    return y_log, u_log\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb5e1757",
   "metadata": {},
   "outputs": [],
   "source": [
    "# NN初期化と実行\n",
    "torch.manual_seed(0)\n",
    "controller = NNPIDController()\n",
    "plant = Plant()\n",
    "y_log, u_log = run_simulation(controller, plant)\n",
    "\n",
    "# プロット\n",
    "plt.figure(figsize=(10, 5))\n",
    "plt.plot(y_log, label=\"Output y(t)\")\n",
    "plt.plot(u_log, label=\"Control u(t)\")\n",
    "plt.xlabel(\"Time Step\")\n",
    "plt.title(\"NN-PID Control Response\")\n",
    "plt.grid()\n",
    "plt.legend()\n",
    "plt.show()\n"
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}
  
