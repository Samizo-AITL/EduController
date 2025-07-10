# 🧮 digital_pid.py
# 連続PID制御と離散PID制御の比較シミュレーション（Tustin法による離散化）

import numpy as np
import matplotlib.pyplot as plt
import control

# --- 連続時間プラント（1次遅れ系） ---
Kp_plant = 1.0
tau = 1.0
G_s = control.tf([Kp_plant], [tau, 1])

# --- PIDゲイン設定 ---
Kp = 2.0
Ki = 1.0
Kd = 0.5

# --- 連続時間PID（制御器） ---
s = control.TransferFunction.s
Gc_s = Kp + Ki / s + Kd * s
sys_continuous = control.feedback(Gc_s * G_s, 1)

# --- 離散化（Tustin法） ---
Ts = 0.1  # サンプリング周期
Gc_z = control.sample_system(Gc_s, Ts, method='tustin')
G_z = control.sample_system(G_s, Ts, method='zoh')
sys_discrete = control.feedback(Gc_z * G_z, 1)

# --- ステップ応答（比較） ---
t_cont, y_cont = control.step_response(sys_continuous, T=np.arange(0, 10, 0.01))
t_disc, y_disc = control.step_response(sys_discrete, T=np.arange(0, 10, Ts))

# --- 描画 ---
plt.figure(figsize=(10, 5))
plt.plot(t_cont, y_cont, label="Continuous PID", linewidth=2)
plt.step(t_disc, y_disc, where='post', label="Digital PID (Tustin)", linestyle='--')
plt.title("Step Response: Continuous vs Digital PID")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("../figures/digital_pid_response.png", dpi=300)
plt.show()
