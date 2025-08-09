---
layout: default
title: 03. ゲインスケジューリング制御 / Gain Scheduling
permalink: /part03_adaptive/theory/03_gain_scheduling.html
---

---

# 🔀 03. ゲインスケジューリング制御 / Gain Scheduling

> ℹ️ **数式が正しく表示されない場合はGitHub版をご確認ください**  
> If equations do not render properly, see the [GitHub version](https://github.com/Samizo-AITL/EduController/blob/main/part03_adaptive/theory/03_gain_scheduling.md)

---

**ゲインスケジューリング（GS）**は、制御対象の状態や外部条件に応じて、  
**制御ゲイン（K）をリアルタイムで切り替える／補間する**手法です。

航空機、自動車、化学プラントなど、**非線形・広範囲な動作をするシステム**において、  
シンプルかつ実用的な適応戦略として広く用いられています。

---

## 🎯 学習目標 / Learning Goals

- **ゲインスケジューリングの基本的考え方を理解する**  
  Understand the basic concept of gain scheduling  
- **スケジューリング変数と局所モデルの関係を説明できる**  
  Explain the relationship between scheduling variables and local models  
- **補間／切替によるゲイン設計を行える**  
  Design gains via interpolation or switching  
- **Pythonで簡易GS制御器を構築できる**  
  Implement a basic GS controller in Python  

---

## 🔧 基本構造 / Basic Structure

1. **スケジューリング変数 $\rho(t)$** を選定（例：速度、温度、高度）  
   Select a scheduling variable (e.g., speed, temperature, altitude)  
2. 各 $\rho_i$ に対してローカル制御器 $K_i$ を設計  
   Design a local controller $K_i$ for each $\rho_i$  
3. 現在の $\rho(t)$ に基づき、$K(\rho)$ を選択／補間して適用  
   Select or interpolate $K(\rho)$ based on current $\rho(t)$  

---

## 📘 例：航空機の飛行モード切替 / Example: Flight Mode Switching

| **状態 / State $\rho$** | **モード / Mode** | **制御器設計 / Controller** | **コメント / Remarks** |
|-------------------------|-------------------|-----------------------------|------------------------|
| $\rho = 0$              | 巡航 / Cruise     | $K_1$                       | 中速安定 / Stable mid-speed |
| $\rho = 1$              | 上昇 / Climb      | $K_2$                       | 推力強化 / Increased thrust |
| $\rho = 2$              | 旋回 / Turn       | $K_3$                       | 応答性重視 / High responsiveness |

---

## ✅ 数学的モデル（線形補間） / Mathematical Model (Linear Interpolation)

$$
K(\rho) = (1 - \alpha) K_1 + \alpha K_2, \quad \alpha = \frac{\rho - \rho_1}{\rho_2 - \rho_1}
$$

- ゲインを連続的に変化させ、応答のスムーズさを確保  
  Ensure smooth response by continuously varying the gain  
- モデルも $\rho$ に依存： $A(\rho), B(\rho)$  
  Model matrices also depend on $\rho$: $A(\rho), B(\rho)$  

---

## 🧪 Python実装例（補間） / Python Implementation (Interpolation)

```python
def gain_schedule(rho):
    if rho < 1.0:
        K = (1 - rho) * K1 + rho * K2
    else:
        K = K2
    return K
```

- 状態や外部変数に応じて動的に制御器を切替  
  Switch controller dynamically according to system state or external variables  
- 補間により過渡応答を改善  
  Interpolation improves transient response  

---

## 🖼️ AITL-Hとの接続例 / Connection to AITL-H

| **AITL層 / Layer** | **対応 / Role** | **GSとの関係 / Relation to GS** |
|--------------------|-----------------|----------------------------------|
| 本能（FSM） / Instinct (FSM) | 状態遷移制御 / Mode switching | モードごとに異なるゲイン適用 / Apply different gains per mode |
| 理性（PID/状態FB） / Reason (PID/State FB) | 物理制御 / Physical control | ゲインを動的に補間 / Dynamically interpolate gains |
| 知性（LLM） / Intelligence (LLM) | 推論・予測 / Reasoning & prediction | スケジューリング変数の予測補助 / Assist in predicting scheduling variables |

---

## ⚠️ 注意点と限界 / Notes & Limitations

- 各動作点でのモデル妥当性確認が必要  
  Must validate the model at each operating point  
- 補間性を確保しないと不連続応答の可能性  
  Discontinuities may occur without smooth interpolation  
- 非線形系にはLPVや非線形GSが有効  
  LPV or nonlinear GS is effective for nonlinear systems  

---

## 📚 参考資料 / References

- Nise, *Control Systems Engineering*  
- Stevens & Lewis, *Aircraft Control and Simulation*  
- Takagi-Sugeno型ファジィ推論（非線形GS拡張）  
  Takagi-Sugeno fuzzy inference (extension to nonlinear GS)  

---

**⬅️ 前節 / Previous:** [02. MRAC](https://samizo-aitl.github.io/EduController/part03_adaptive/theory/02_mrac_design.html)  
モデル参照型適応制御の構造とMITルールを解説 / Structure of MRAC and MIT rule

**➡️➡️ 次節 / Next:** [04. L1適応制御](https://samizo-aitl.github.io/EduController/part03_adaptive/theory/04_l1_adaptive.html)  
高速かつ安定なパラメータ適応法 / Fast and stable parameter adaptation

**📚 第3章 README / Chapter Top:** [適応制御とロバスト制御](https://samizo-aitl.github.io/EduController/part03_adaptive/)  
第3章全体の構成と教材一覧 / Overview and chapter contents
