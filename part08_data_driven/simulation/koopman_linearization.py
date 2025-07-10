import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 状態遷移関数（非線形系の例）
def nonlinear_dynamics(x, u):
    return np.array([
        np.sin(x[0]) + 0.1 * x[1] + 0.05 * u,
        x[0] + 0.2 * np.tanh(u)
    ])

# シミュレーションパラメータ
N = 500  # データ数
x_dim = 2
u_dim = 1

# データ生成
np.random.seed(0)
X = []
Y = []
U = []

x = np.random.randn(x_dim)
for _ in range(N):
    u = np.random.uniform(-1.0, 1.0)
    x_next = nonlinear_dynamics(x, u)
    X.append(x)
    Y.append(x_next)
    U.append([u])
    x = x_next

X = np.array(X)
Y = np.array(Y)
U = np.array(U)

# 観測関数（多項式特徴）で φ(x, u) を構成
poly = PolynomialFeatures(degree=2, include_bias=False)
Phi_XU = poly.fit_transform(np.hstack([X, U]))
Phi_Y = poly.transform(np.hstack([Y, np.zeros_like(U)]))  # u不要だがshape合わせ

# 線形回帰で Koopman 近似
model = LinearRegression()
model.fit(Phi_XU, Phi_Y)

K = model.coef_.T
print("Koopman近似行列 K の形状:", K.shape)

# 可視化：予測 vs 真値（1次元目）
Y_pred = model.predict(Phi_XU)
plt.figure()
plt.plot(Y[:, 0], label="True x1")
plt.plot(Y_pred[:, 0], '--', label="Koopman Predicted x1")
plt.legend()
plt.title("Koopman-based Prediction (x1)")
plt.xlabel("Time Step")
plt.grid()
plt.tight_layout()
plt.show()
