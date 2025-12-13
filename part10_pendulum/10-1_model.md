---
title: "10-1 倒立振子モデル：非線形 → 線形化 → 状態空間"
emoji: "🎯"
type: "tech"
topics: ["制御", "倒立振子", "状態空間", "線形化"]
published: false
---

# 10-1 倒立振子モデル：非線形 → 線形化 → 状態空間

---

## 1. モデル定義（cart-pole）

- 台車質量：M [kg]
- 振子質量：m [kg]
- 振子長（支点〜重心）：l [m]
- 重力加速度：g [m/s^2]
- 台車位置：x [m]
- 振子角度（直立を0）：θ [rad]
- 入力（水平力）：u = F [N]

状態変数：

$$
\mathbf{x}=
\begin{bmatrix}
\theta \\
\dot{\theta} \\
x \\
\dot{x}
\end{bmatrix},
\qquad
u = F
$$

---

## 2. 非線形運動方程式

$$
(M+m)\ddot{x} + m l \ddot{\theta}\cos\theta - m l \dot{\theta}^2 \sin\theta = u
$$

$$
l\ddot{\theta} + \ddot{x}\cos\theta - g\sin\theta = 0
$$

---

## 3. 明示形（加速度）

分母を

$$
D(\theta)= (M+m) - m\cos^2\theta
$$

と定義すると，

$$
\ddot{x} =
\frac{
u + m l \dot{\theta}^2\sin\theta - m g \sin\theta\cos\theta
}{
D(\theta)
}
$$

$$
\ddot{\theta} =
\frac{
u\cos\theta - m l \dot{\theta}^2\sin\theta\cos\theta + (M+m)g\sin\theta
}{
l\,D(\theta)
}
$$

---

## 4. 線形化（直立平衡点）

近似条件：

$$
\theta \approx 0,\quad
\dot{\theta}\approx 0,\quad
x\approx 0,\quad
\dot{x}\approx 0
$$

$$
\sin\theta \approx \theta,\quad
\cos\theta \approx 1
$$

$$
D(0)= (M+m) - m = M
$$

線形化結果：

$$
\ddot{x} \approx \frac{1}{M}u - \frac{m g}{M}\theta
$$

$$
\ddot{\theta} \approx \frac{(M+m)g}{l M}\theta - \frac{1}{lM}u
$$

---

## 5. 状態空間表現

$$
\dot{\mathbf{x}} = A\mathbf{x} + B u
$$

$$
A=
\begin{bmatrix}
0 & 1 & 0 & 0 \\
\frac{(M+m)g}{lM} & 0 & 0 & 0 \\
0 & 0 & 0 & 1 \\
-\frac{mg}{M} & 0 & 0 & 0
\end{bmatrix},
\quad
B=
\begin{bmatrix}
0 \\
-\frac{1}{lM} \\
0 \\
\frac{1}{M}
\end{bmatrix}
$$

---

## 6. 出力例

$$
\mathbf{y}=
\begin{bmatrix}
\theta \\
x
\end{bmatrix}
$$

$$
C=
\begin{bmatrix}
1&0&0&0\\
0&0&1&0
\end{bmatrix},
\quad
D=
\begin{bmatrix}
0\\
0
\end{bmatrix}
$$

---
