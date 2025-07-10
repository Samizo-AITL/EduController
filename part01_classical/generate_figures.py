# 📦 generate_figures.py
# Part1 の図を一括生成するスクリプト

import numpy as np
import matplotlib.pyplot as plt
import control
import os

os.makedirs("figures", exist_ok=True)

# --- PIDステップ応答 ---
def save_pid_step_response():
    Kp, Ki, Kd = 1.0, 0.5, 0.1
    plant = control.tf([1], [1, 1])
    controllers = {
        "P": control.tf([Kp], [1]),
        "PI": control.tf([Kp, Ki], [1, 0]),
        "PD": control.tf([Kd, Kp], [1]),
        "PID": control.tf([Kd, Kp, Ki], [1, 0])
    }
    t = np.linspace(0, 10, 500)
    plt.figure()
    for label, C in controllers.items():
        sys = control.feedback(C * plant, 1)
        t_out, y_out = control.step_response(sys, t)
        plt.plot(t_out, y_out, label=label)
    plt.title("Step Response with Different PID Controllers")
    plt.xlabel("Time [s]")
    plt.ylabel("Output")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("figures/step_response.png", dpi=300)
    plt.close()

# --- 過渡応答（1次・2次） ---
def save_transient_response():
    G1 = control.tf([1], [1, 1])
    wn, zeta = 2.0, 0.5
    G2 = control.tf([wn**2], [1, 2*zeta*wn, wn**2])
    t = np.linspace(0, 10, 500)
    t1, y1 = control.step_response(G1, t)
    t2, y2 = control.step_response(G2, t)
    plt.figure()
    plt.plot(t1, y1, label="1st-order")
    plt.plot(t2, y2, label="2nd-order")
    plt.title("Step Response: 1st-order vs 2nd-order")
    plt.xlabel("Time [s]")
    plt.ylabel("Output")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("figures/transient_response.png", dpi=300)
    plt.close()

# --- Bode線図（例） ---
def save_bode_example():
    G = control.tf([1], [1, 1])
    plt.figure()
    mag, phase, omega = control.bode(G, dB=True, deg=True, Plot=False)
    plt.subplot(2, 1, 1)
    plt.semilogx(omega, 20*np.log10(mag), label='Gain')
    plt.axhline(0, color='gray', linestyle='--')
    plt.ylabel("Gain [dB]")
    plt.grid(True)
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.semilogx(omega, phase * 180/np.pi, label='Phase')
    plt.axhline(-180, color='gray', linestyle='--')
    plt.xlabel("Frequency [rad/s]")
    plt.ylabel("Phase [deg]")
    plt.grid(True)
    plt.legend()
    plt.suptitle("Bode Plot Example")
    plt.tight_layout()
    plt.savefig("figures/bode_example.png", dpi=300)
    plt.close()

# --- Root Locus & Nyquist ---
def save_root_locus_nyquist():
    K = 5
    G = control.tf([K], [1, 4, 5, K])
    plt.figure()
    control.root_locus(G)
    plt.title("Root Locus")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("figures/root_locus_example.png", dpi=300)
    plt.close()
    plt.figure()
    control.nyquist_plot(G)
    plt.title("Nyquist Plot")
    plt.tight_layout()
    plt.savefig("figures/nyquist_example.png", dpi=300)
    plt.close()

# --- PM/GM Bode Plot ---
def save_pm_gm_bode():
    G = control.tf([1], [1, 2, 1])
    gm, pm, wg, wp = control.margin(G)
    mag, phase, omega = control.bode(G, dB=True, deg=True, Plot=False)
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.semilogx(omega, 20*np.log10(mag), label='Gain')
    plt.axhline(0, color='gray', linestyle='--')
    plt.axvline(wg, color='r', linestyle=':', label='PM freq')
    plt.ylabel("Gain [dB]")
    plt.grid(True)
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.semilogx(omega, phase * 180/np.pi, label='Phase')
    plt.axhline(-180, color='gray', linestyle='--')
    plt.axvline(wp, color='r', linestyle=':', label='GM freq')
    plt.xlabel("Frequency [rad/s]")
    plt.ylabel("Phase [deg]")
    plt.grid(True)
    plt.legend()
    plt.suptitle("Bode Plot with Gain/Phase Margins")
    plt.tight_layout()
    plt.savefig("figures/phase_gain_margin_example.png", dpi=300)
    plt.close()

# --- 実行 ---
save_pid_step_response()
save_transient_response()
save_bode_example()
save_root_locus_nyquist()
save_pm_gm_bode()

print("✅ All figures saved in ./figures/")
