import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import svd, eig

# サンプル非線形系：x_next = [x1 + x2; -0.5 x1 + 0.9 x2]
def simulate_dynamics(x0, N):
    x = x0
    states = [x]
    for _ in range(N):
        x_next = np.array([
            x[0] + x[1],
            -0.5 * x[0] + 0.9 * x[1]
        ])
        states.append(x_next)
        x = x_next
    return np.array(states)

# シミュレーションパラメータ
N = 100
x0 = np.array([1.0, 0.0])
X = simulate_dynamics(x0, N)

# DMDデータ行列構築
X1 = X[:-1].T  # x_1 to x_{m-1}
X2 = X[1:].T   # x_2 to x_m

# SVD分解
U, S, Vh = svd(X1, full_matrices=False)
r = 2  # ランク（状態次元）を2に固定
Ur = U[:, :r]
Sr = np.diag(S[:r])
Vr = Vh.conj().T[:, :r]

# DMD行列 Atilde の構築
A_tilde = Ur.T @ X2 @ Vr @ np.linalg.inv(Sr)

# 固有値・固有ベクトル
eigvals, eigvecs = eig(A_tilde)

# 予測
X_dmd = np.zeros_like(X1)
b = np.linalg.lstsq(eigvecs, Ur.T @ X1[:, 0], rcond=None)[0]
for i in range(N):
    X_dmd[:, i] = (eigvecs @ np.diag(eigvals**i) @ b).real

# 可視化
plt.figure()
plt.plot(X1[0, :], label='True x1')
plt.plot(X_dmd[0, :], '--', label='DMD x1')
plt.plot(X1[1, :], label='True x2')
plt.plot(X_dmd[1, :], '--', label='DMD x2')
plt.title("DMD vs True Dynamics")
plt.xlabel("Time Step")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
