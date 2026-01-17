---
layout: clean
title: 🧭 10-3 FSMオーバレイ制御：効いた点と効かなかった点
permalink: /part10_pendulum/10-3_fsm_overlay.html
---

# 🧭 10-3 FSMオーバレイ制御  
## 効いた点と効かなかった点  
*FSM Overlay Control: What Worked and What Did Not*

---

## 📌 本章の立ち位置  
*Position of This Chapter*

本章では、**PID制御の上に FSM（Finite State Machine）を重ねます**。  
ただし、目的は「賢い制御」を作ることではありません。

*In this chapter, an FSM (Finite State Machine) is overlaid on top of PID control.  
The goal is not to make the controller “smart.”*

> **PIDに判断をさせないために、  
> 判断だけを切り出す**

> *To prevent PID from making decisions,  
> we isolate decision-making itself.*

それ以上でも、それ以下でもありません。

*Nothing more, nothing less.*

---

## 1️⃣ なぜFSMが必要か（再確認）  
*Why FSM Is Needed (Recap)*

前章で示した通り、PID制御は以下を **判断できません**。

*As shown in the previous chapter, PID cannot determine:*

- 今は小振幅か？  
  *Is the motion small-amplitude?*
- すでに大振幅か？  
  *Has it already become large-amplitude?*
- 入力が飽和しているか？  
  *Is the actuator saturated?*
- もはや回復不能か？  
  *Is recovery impossible?*

そこで、**役割を構造的に分離**します。

*Therefore, we separate roles structurally:*

- 🔁 **PID**：連続量制御（角度・角速度）  
  *Continuous control of angle and velocity*
- 🧭 **FSM**：状態判定とモード切替  
  *State judgment and mode switching*

---

## 2️⃣ FSMの状態定義（最小構成）  
*FSM State Definition (Minimal Design)*

今回は、**最低限の3状態** のみを定義します。

*We intentionally limit the FSM to the minimal three states.*

### 状態集合  
*State Set*

$$
\mathcal{S} = \{ S_1, S_2, S_3 \}
$$

| 状態 / State | 意味 / Meaning |
|---|---|
| $$S_1$$ | Swing-up（振り上げ）<br>*Swing-up mode* |
| $$S_2$$ | Balance（直立保持）<br>*Balance mode* |
| $$S_3$$ | Fail-safe（脱出）<br>*Fail-safe mode* |

---

## 3️⃣ 状態遷移条件  
*State Transition Conditions*

### 3.1 📐 角度しきい値  
*Angle Thresholds*

$$
|\theta| < \theta_{\text{bal}}
\quad \Rightarrow \quad S_2
$$

$$
|\theta| \ge \theta_{\text{bal}}
\quad \Rightarrow \quad S_1
$$

### 3.2 🚨 回復不能条件  
*Unrecoverable Condition*

$$
|\theta| > \theta_{\text{fail}}
\quad \Rightarrow \quad S_3
$$

ここで、

*Where:*

$$
0 < \theta_{\text{bal}} < \theta_{\text{fail}} < \pi
$$

---

## 4️⃣ 各状態での制御則  
*Control Law in Each State*

### 4.1 🔄 Swing-up（ $$S_1$$ ）

例として、単純なエネルギー制御を用います。

*As an example, a simple energy-based controller is used.*

$$
u =
K_e \left(
E_{\text{ref}} - E(\theta,\dot{\theta})
\right)\mathrm{sgn}(\dot{\theta}\cos\theta)
$$

※ 詳細は本教材の範囲外です。  
**重要なのは「PIDを使わない」ことです。**

*Details are outside the scope of this material.  
What matters is that PID is not used here.*

---

### 4.2 ⚖️ Balance（ $$S_2$$ ）

前章と同一の PID 制御を用います。

*The same PID controller as in the previous chapter is applied.*

$$
u =
K_p (-\theta)
+ K_d (-\dot{\theta})
+ K_i \int (-\theta)\,dt
$$

FSMは **ゲインを調整しません**。  
「使うか／使わないか」だけを判断します。

*The FSM does not tune gains; it only decides whether to use PID or not.*

---

### 4.3 🛑 Fail-safe（ $$S_3$$ ）

最も単純な選択は：

*The simplest choice is:*

$$
u = 0
$$

あるいは、

*Alternatively:*

$$
u = -K_x \dot{x}
$$

➡️ **倒れることを前提に、安全に逃がす**  
*➡️ The system safely gives up, assuming failure.*

---

## 5️⃣ FSMを入れて「何が改善したか」  
*What FSM Actually Improved*

### 改善①：適用範囲の明確化  
*Improvement 1: Explicit Validity Region*

PIDが使われるのは：

*PID is applied only when:*

$$
|\theta| < \theta_{\text{bal}}
$$

➡️ **線形設計の前提が守られる**  
*➡️ Linear assumptions are preserved.*

---

### 改善②：飽和破綻の回避  
*Improvement 2: Avoiding Saturation Collapse*

- Swing-up：  
  大入力・飽和前提  
  *Large inputs, saturation allowed*
- Balance：  
  小入力・線形前提  
  *Small inputs, linear regime*

➡️ **役割分離が成立**  
*➡️ Clear separation of roles.*

---

### 改善③：失敗を定義できる  
*Improvement 3: Ability to Declare Failure*

FSMを入れることで、

*With FSM:*

> **「これは失敗です」**

をシステム自身が宣言できます。

*The system can explicitly declare failure.*

PID単体では不可能です。

---

## 6️⃣ それでも効かなかった点（重要）  
*What FSM Could Not Fix (Important)*

ここを **隠しません**。

*These limitations are not hidden.*

---

### 6.1 🔁 状態境界のチャタリング  
*Chattering at State Boundaries*

$$
|\theta| \approx \theta_{\text{bal}}
$$

付近で：

*Near the boundary:*

$$
S_1 \leftrightarrow S_2
$$

が高速に切り替わります。

➡️ 入力がギザギザ  
➡️ 実機では危険  

*This causes oscillatory inputs and can be dangerous in real systems.*

---

### 6.2 📡 ノイズに弱い  
*Sensitivity to Noise*

判定条件が

*If decisions rely only on:*

$$
\theta,\ \dot{\theta}
$$

の場合、

- センサノイズ  
- 推定誤差  

によって **誤遷移** が発生します。

*Sensor noise and estimation errors cause false transitions.*

FSMは **離散的に壊れる**。

*FSMs fail discretely.*

---

### 6.3 📉 本質的な性能は向上しない  
*No Fundamental Performance Gain*

FSMは：

*FSM:*

- 安定性を「作らない」  
- 最適性を「改善しない」  

あくまで：

> **使い分けの整理役**

> *A coordinator, not a controller.*

---

## 7️⃣ 本章の結論（重要）  
*Conclusion of This Chapter*

FSMは：

- ✅ PIDの限界を隠さない  
- ✅ 動作条件を明文化する  
- ❌ 魔法ではない  

> **FSMは「制御」ではなく「構造」**

> *FSM is not control — it is structure.*

---

## 8️⃣ EduController への接続  
*Connection to EduController*

この構造は、そのまま次の三層構造につながります。

*This structure naturally leads to a three-layer architecture:*

- 🔽 内側：PID（連続制御）  
  *Inner loop: PID*
- 🔁 中間：FSM（判断・切替）  
  *Middle layer: FSM*
- 🌐 外側：再設計・再同定（将来）  
  *Outer layer: redesign and re-identification*

---

## ✅ チェックリスト  
*Checklist*

- [x] FSMの役割を限定した  
- [x] 効いた点／効かなかった点を分離した  
- [x] PIDを過大評価しなかった  
- [x] 次の層（拡張）への接続を残した  
