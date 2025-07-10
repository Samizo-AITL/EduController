# 🔍 fft_noise_removal.py
# FFTを用いて周波数成分を解析・除去し、信号を再構成するデモ

import numpy as np
import matplotlib.pyplot as plt

# --- パラメータ設定 ---
fs = 1000  # サンプリング周波数 [Hz]
T = 1.0    # 信号長 [s]
N = int(T * fs)  # サンプル数
t = np.linspace(0, T, N, endpoint=False)

# --- 合成信号（50Hz信号 + 300Hzノイズ）---
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 300 * t)

# --- FFT解析 ---
X = np.fft.fft(signal)
freqs = np.fft.fftfreq(N, d=1/fs)

# --- 高周波成分の除去（100Hz以上をカット）---
X_filtered = X.copy()
X_filtered[np.abs(freqs) > 100] = 0

# --- IFFTで信号再構成 ---
signal_filtered = np.fft.ifft(X_filtered).real

# --- 結果の可視化 ---
plt.figure(figsize=(12, 8))

# 時系列（元信号とフィルタ後）
plt.subplot(2, 1, 1)
plt.plot(t, signal, label="Original Signal")
plt.plot(t, signal_filtered, label="Filtered Signal", linestyle='--')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Time Domain Signal")
plt.legend()
plt.grid()

# 周波数スペクトル
plt.subplot(2, 1, 2)
plt.plot(freqs[:N//2], np.abs(X[:N//2]), label="Original Spectrum")
plt.plot(freqs[:N//2], np.abs(X_filtered[:N//2]), label="Filtered Spectrum", linestyle='--')
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.title("Frequency Domain (FFT)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig("../figures/fft_spectrum.png", dpi=300)
plt.show()
