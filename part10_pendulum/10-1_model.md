---
layout: clean
title: 🎯10-1 倒立振子モデル：非線形 → 線形化 → 状態空間
permalink: /part10_pendulum/10-1_model.html
---

# 🎯 10-1 倒立振子モデル：非線形 → 線形化 → 状態空間  
*Inverted Pendulum Model: Nonlinear → Linearized → State-Space*

---

## 📌 本章の目的  
*Purpose of This Chapter*

本章では、**倒立振子（cart-pole 系）** を題材に、  
制御設計の出発点となる **数式モデルの構築プロセス** を整理します。

*This chapter introduces the mathematical modeling process of the inverted pendulum (cart-pole system), which serves as the foundation for control design.*

特に以下の流れを重視します。

*The focus is on the following sequence:*

1. ⚙️ 非線形運動方程式の確認  
   *Understanding the nonlinear equations of motion*
2. ✂️ 直立平衡点まわりでの線形化  
   *Linearization around the upright equilibrium*
3. 📐 状態空間モデルへの整理  
   *Reformulation into state-space representation*

---

## 1️⃣ モデル定義（Cart-Pole 系）  
*Model Definition (Cart-Pole System)*

以下の物理パラメータを定義します。

*The following physical parameters are defined.*

- 🚃 台車質量：\( M \) [kg]  
  *Cart mass*
- 🪄 振子質量：\( m \) [kg]  
  *Pendulum mass*
- 📏 振子長（支点〜重心）：\( l \) [m]  
  *Pendulum length (pivot to center of mass)*
- 🌍 重力加速度：\( g \) [m/s\(^2\)]  
  *Gravitational acceleration*
- ↔️ 台車位置：\( x \) [m]  
  *Cart position*
- 📐 振子角度（直立を 0）：\( \theta \) [rad]  
  *Pendulum angle (0 at upright position)*
- 🧲 入力（水平力）：\( u = F \) [N]  
  *Control input (horizontal force)*

### 状態変数  
*State Variables*

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

## 2️⃣ 非線形運動方程式  
*Nonlinear Equations of Motion*

運動方程式は以下の **非線形連立微分方程式** で与えられます。

*The dynamics are described by the following coupled nonlinear differential equations.*

$$
(M+m)\ddot{x} + m l \ddot{\theta}\cos\theta - m l \dot{\theta}^2 \sin\theta = u
$$

$$
l\ddot{\theta} + \ddot{x}\cos\theta - g\sin\theta = 0
$$

ここでは、台車と振子の **相互結合** が  
\(\cos\theta\)、\(\sin\theta\)、\(\dot{\theta}^2\) を通じて現れている点が重要です。

*Note that the coupling between the cart and the pendulum appears through \(\cos\theta\), \(\sin\theta\), and \(\dot{\theta}^2\).*

---

## 3️⃣ 明示形（加速度表現）  
*Explicit Form (Accelerations)*

分母を次のように定義します。

*Define the denominator as follows.*

$$
D(\theta)= (M+m) - m\cos^2\theta
$$

このとき、加速度は以下の **明示形** で表されます。

*The accelerations can then be written explicitly.*

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

この段階では、**強い非線形性** が残っており、  
単純な PID 制御が成立しにくいことが直感的に分かります。

*At this stage, strong nonlinearities remain, making simple PID control difficult.*

---

## 4️⃣ 線形化（直立平衡点）  
*Linearization Around Upright Equilibrium*

直立平衡点まわりで、次の近似を行います。

*The following approximations are applied around the upright equilibrium.*

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

分母は次のように簡略化されます。

*The denominator simplifies to:*

$$
D(0)= (M+m) - m = M
$$

### 線形化結果  
*Linearized Dynamics*

$$
\ddot{x} \approx \frac{1}{M}u - \frac{m g}{M}\theta
$$

$$
\ddot{\theta} \approx \frac{(M+m)g}{l M}\theta - \frac{1}{lM}u
$$

ここで、**角度 \(\theta\) が発散方向の力学を持つ** ことが明確になります。

*This clearly shows that the angle \(\theta\) has inherently unstable dynamics.*

---

## 5️⃣ 状態空間表現  
*State-Space Representation*

線形化されたモデルは、次の状態方程式で表されます。

*The linearized model can be expressed in state-space form.*

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

この形が、以降の **PID 制御・FSM 構造設計** の基盤となります。

*This form serves as the basis for subsequent PID control and FSM-based design.*

---

## 6️⃣ 出力例  
*Example Outputs*

代表的な出力として、角度と位置を選びます。

*A typical output selection includes the pendulum angle and cart position.*

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

## 🧭 次章へ  
*Next Chapter*

次章では、このモデルを用いて、

- ❓ **なぜ PID 制御が成立する場合と破綻する場合があるのか**
- ❓ **どの仮定が暗黙に置かれているのか**

を **構造的に分解** していきます。

*In the next chapter, we analyze when and why PID control succeeds or fails, based on this model.*
