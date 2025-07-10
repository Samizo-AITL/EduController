{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 📊 Koopman vs DMD 可視化
",
    "
",
    "このNotebookでは、データ駆動型制御の代表手法である
",
    "**Koopman線形化** と **動的モード分解（DMD）** の比較を可視化します。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 必要なライブラリのインポート
",
    "import numpy as np
",
    "import matplotlib.pyplot as plt
",
    "from sklearn.linear_model import LinearRegression
",
    "from sklearn.preprocessing import PolynomialFeatures
",
    "from numpy.linalg import svd, eig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 非線形系の定義とデータ生成
",
    "def nonlinear_dynamics(x, u):
",
    "    return np.array([
",
    "        np.sin(x[0]) + 0.1 * x[1] + 0.05 * u,
",
    "        x[0] + 0.2 * np.tanh(u)
",
    "    ])
",
    "
",
    "N = 300
",
    "x_dim = 2
",
    "np.random.seed(0)
",
    "X, Y, U = [], [], []
",
    "x = np.random.randn(x_dim)
",
    "for _ in range(N):
",
    "    u = np.random.uniform(-1, 1)
",
    "    x_next = nonlinear_dynamics(x, u)
",
    "    X.append(x); Y.append(x_next); U.append([u])
",
    "    x = x_next
",
    "X, Y, U = np.array(X), np.array(Y), np.array(U)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Koopman近似
",
    "poly = PolynomialFeatures(degree=2, include_bias=False)
",
    "Phi_XU = poly.fit_transform(np.hstack([X, U]))
",
    "Phi_Y = poly.transform(np.hstack([Y, np.zeros_like(U)]))
",
    "model = LinearRegression().fit(Phi_XU, Phi_Y)
",
    "Y_pred_koopman = model.predict(Phi_XU)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# DMDによる予測
",
    "X1 = X[:-1].T
",
    "X2 = X[1:].T
",
    "U_svd, S_svd, Vh_svd = svd(X1, full_matrices=False)
",
    "r = 2
",
    "Ur, Sr, Vr = U_svd[:, :r], np.diag(S_svd[:r]), Vh_svd.conj().T[:, :r]
",
    "A_tilde = Ur.T @ X2 @ Vr @ np.linalg.inv(Sr)
",
    "eigvals, eigvecs = eig(A_tilde)
",
    "b = np.linalg.lstsq(eigvecs, Ur.T @ X1[:, 0], rcond=None)[0]
",
    "X_dmd = np.array([(eigvecs @ np.diag(eigvals**i) @ b).real for i in range(X1.shape[1])]).T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 比較プロット
",
    "plt.figure(figsize=(10, 4))
",
    "plt.plot(Y[:, 0], label='True x1')
",
    "plt.plot(Y_pred_koopman[:, 0], '--', label='Koopman x1')
",
    "plt.plot(X1[0, :], ':', label='DMD x1')
",
    "plt.legend(); plt.grid(); plt.title("Koopman vs DMD (x1)")
",
    "plt.tight_layout(); plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
