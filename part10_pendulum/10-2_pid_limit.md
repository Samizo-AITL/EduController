---
layout: clean
title: 📉 10-2 PID制御の限界：なぜ倒立振子は安定しないのか
permalink: /part10_pendulum/10-2_pid_limit.html
---

# 📉 10-2 PID制御の限界  
## なぜ倒立振子は安定しないのか  
*Limits of PID Control: Why the Inverted Pendulum Cannot Be Stabilized*

---

## 📌 本章のスタンス  
*Position of This Chapter*

本章では、**10-1 で導出した線形モデル**に対して、  
「**PID制御だけを適用すると何が起きるのか**」を  
**ごまかさず、逃げずに示します。**

*In this chapter, we honestly examine what happens when only PID control is applied to the linearized model derived in 10-1.*

最初に、結論を明示します。

*The conclusion is stated upfront.*

> **倒立振子は、PID制御で  
> 「たまたま立つ」ことはあっても、  
> 安定性を保証することはできない。**

> *With PID control, an inverted pendulum may stand “by chance,”  
> but its stability cannot be guaranteed.*

---

## 1️⃣ 対象モデル（再掲）  
*Target Model (Recap)*

### 状態変数  
*State Vector*

$$
\mathbf{x}=
\begin{bmatrix}
\theta \\
\dot{\theta} \\
x \\
\dot{x}
\end{bmatrix}
$$

### 線形化モデル  
*Linearized Model*

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

## 2️⃣ 制御対象の本質：不安定極  
*Essence of the Plant: Unstable Pole*

角度系のみを抜き出すと、次式になります。

*Extracting only the angular dynamics yields:*

$$
\ddot{\theta} =
\frac{(M+m)g}{lM}\theta - \frac{1}{lM}u
$$

制御入力が存在しない場合：

*Without control input:*

$$
\ddot{\theta} =
\frac{(M+m)g}{lM}\theta
$$

この解は、

*The solution behaves as:*

$$
\theta(t) \sim e^{\lambda t}, \quad
\lambda = \sqrt{\frac{(M+m)g}{lM}} > 0
$$

すなわち、**指数的に発散する系**です。

*That is, the system is exponentially unstable.*

➡️ **元々不安定な対象である**  
*➡️ The plant is inherently unstable.*

---

## 3️⃣ PID制御の構成  
*PID Control Structure*

角度のみを制御対象とし、誤差を定義します。

*The control target is the angle only.*

$$
e(t) = \theta_{\text{ref}} - \theta(t)
$$

PID制御則は次式です。

*The PID control law is:*

$$
u(t) =
K_p e(t)
+ K_i \int e(t)\,dt
+ K_d \frac{de(t)}{dt}
$$

直立保持問題では、

*For upright stabilization:*

$$
\theta_{\text{ref}} = 0
$$

---

## 4️⃣ PIDを入れても何が起きるか  
*What Actually Happens with PID*

### 4.1 🌈 理想連続時間（幻想）  
*Ideal Continuous-Time World (Fantasy)*

- ノイズ無し  
- 飽和無し  
- 遅延無し  

*No noise, no saturation, no delay.*

この **理想世界** では、

*In this idealized world,*

- 適切な \(K_p, K_d\) を選べば  
- **一応は安定** します  

*the system can be stabilized by tuning gains.*

👉 しかし、**これは現実の制御ではありません。**  
*👉 This has little educational or practical value.*

---

### 4.2 ⚠️ 現実1：入力飽和  
*Reality 1: Input Saturation*

実機では、必ず制約があります。

*Real systems always have limits.*

$$
|u| \le u_{\max}
$$

角度が大きくなると、

*As the angle grows:*

$$
K_p \theta \gg u_{\max}
$$

結果として、

*As a result:*

$$
u \rightarrow \text{飽和}
$$

➡️ **線形設計は即座に破綻**  
*➡️ Linear control assumptions collapse immediately.*

---

### 4.3 📡 現実2：微分項のノイズ増幅  
*Reality 2: Noise Amplification by Derivative Term*

微分項

*The derivative term*

$$
K_d \dot{\theta}
$$

は、以下を **そのまま増幅** します。

*directly amplifies:*

- センサノイズ  
- 量子化誤差  
- サンプリング遅延  

結果として：

*This leads to:*

- 制御入力の振動  
- 実効的に \(K_d\) を下げざるを得ない  
- 位相余裕の消失  

---

### 4.4 ⏱ 現実3：離散時間化  
*Reality 3: Discretization*

サンプリング周期 \(T_s\) を導入すると、

*With sampling period \(T_s\):*

$$
u[k] =
K_p e[k]
+ K_i \sum e[k] T_s
+ K_d \frac{e[k]-e[k-1]}{T_s}
$$

ここで致命的なのは、

*The critical issue is:*

> **倒立振子の発散速度は非常に速い**

*The divergence speed of the inverted pendulum is very high.*

$$
\theta(t+T_s) \approx \theta(t)e^{\lambda T_s}
$$

$$
\lambda T_s \gtrsim 1
$$

となった瞬間、

*Once this condition is met:*

➡️ **制御が入る前に倒れる**  
*➡️ The pendulum falls before control reacts.*

---

## 5️⃣ シミュレーションで必ず起きる典型例  
*Typical Simulation Outcomes*

PID単体で必ず観測されるパターン：

*Typical behaviors with PID alone:*

1. 小さな初期角 → 立つ  
   *Small initial angle → stable*
2. やや大きな初期角 → 飽和 → 発散  
   *Larger angle → saturation → divergence*
3. ノイズ追加 → 微分暴走  
   *Noise added → derivative blow-up*
4. サンプリング周期増大 → 不安定化  
   *Larger sampling time → instability*

➡️ **条件付きでしか成立しない制御**  
*➡️ Control works only under limited conditions.*

---

## 6️⃣ 本章の結論（重要）  
*Conclusion of This Chapter*

PID制御は：

*PID control:*

- ❌ 不安定系を根本的に救えない  
- ❌ 動作範囲を自律的に判断できない  
- ❌ 飽和やモード遷移を扱えない  

PIDが悪いのではありません。

*PID itself is not the problem.*

> **役割を超えた使い方をしている**

> *It is being used beyond its intended role.*

---

## 7️⃣ 次章への必然  
*Why the Next Chapter Is Necessary*

ここで、自然に次の問いが生まれます。

*This naturally raises new questions:*

- 今は大振幅か？  
- 小振幅か？  
- 制御を切り替えるべきか？  
- もう回復不能か？  

PIDは **これらを判断できません。**

*PID cannot make these decisions.*

➡️ そこで、**FSM（Finite State Machine）** を  
**PIDの上位に載せます。**

*➡️ This motivates introducing an FSM above PID.*

---

## 8️⃣ 次章予告  
*Preview of the Next Chapter*

### **10-3 FSMオーバレイ制御**

- PIDは捨てない  
- 上位で「使い分けるだけ」  
- **それでも効かないケースも正直に示す**

*PID remains, FSM supervises, and remaining limitations are openly discussed.*

---

## ✅ チェックリスト  
*Checklist*

- [x] 不安定極を明示した  
- [x] PIDの幻想と現実を切り分けた  
- [x] 飽和・離散化を外さなかった  
- [x] FSM導入の必然を構造的に示した  
