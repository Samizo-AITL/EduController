import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# --- パラメータ定義 ---
Kp = 1.0   # 比例ゲイン
Ki = 0.5   # 積分ゲイン
Kd = 0.1   # 微分ゲイン

# --- 被制御対象（プラント）定義：1次遅れ系 G(s) = 1 / (s + 1) ---
plant = ctl.tf([1], [1, 1])

# --- 各制御器の定義 ---
P = ctl.tf([Kp], [1])
PI = ctl.tf([Kp, Ki], [1, 0])
PD = ctl.tf([Kd, Kp], [1])
PID = ctl.tf([Kd, Kp, Ki], [1, 0])

controllers = {
    "P": P,
    "PI": PI,
    "PD": PD,
    "PID": PID
}

# --- ステップ応答描画 ---
t = np.linspace(0, 10, 500)
plt.figure(figsize=(10, 6))

for label, controller in controllers.items():
    system = ctl.feedback(controller * plant, 1)
    t_out, y_out = ctl.step_response(system, t)
    plt.plot(t_out, y_out, label=label)

plt.title("Step Response with Different PID Controllers")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("../figures/step_response.png", dpi=300)
plt.show()
