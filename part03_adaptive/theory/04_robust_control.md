---
layout: clean
title: 04. ロバスト制御 / Robust Control
permalink: /part03_adaptive/theory/04_robust_control.html
---

---

# 🛡️ 04. ロバスト制御 / Robust Control

> ℹ️ **数式が正しく表示されない場合はGitHub版をご確認ください**  
> If equations do not render properly, see the [GitHub version](https://github.com/Samizo-AITL/EduController/blob/main/part03_adaptive/theory/04_robust_control.md)

---

制御対象には**モデル誤差**や**外乱・ノイズ**が必ず存在します。  
こうした**不確かさに対して性能を保証する制御**が「ロバスト制御（Robust Control）」です。  
Robust control ensures system performance even in the presence of uncertainties, disturbances, and noise.

---

## 🎯 学習目標 / Learning Goals

- **ロバスト制御の基本概念と必要性を理解する** / Understand the concept and necessity of robust control  
- **H∞制御の基本原理と数式構造を把握する** / Learn the principles and mathematical structure of H∞ control  
- **ゲイン余裕・位相余裕でのロバスト性評価を説明できる** / Explain robust stability via gain/phase margins  
- **μ解析など応用評価法を知る** / Get familiar with μ-analysis and advanced evaluation methods  

---

## ❓ なぜロバスト性が必要か？ / Why Robustness Matters

- **モデル化誤差 / Modeling errors**：実機とモデルは完全一致しない  
- **外乱・ノイズ / Disturbances & noise**：センサ雑音、遅延、環境変動  
- **パラメータばらつき / Parameter variations**：製品差、経年劣化  

ロバスト制御の目標は、**性能を保ちながら安定性を保証する**ことです。  
The goal is to **maintain performance while guaranteeing stability**.

---

## 📐 ロバスト性の定義 / Definition

- **内部安定性 (Internal Stability)**：全信号が有界入力で有界出力（BIBO）

- **感度関数 $S(s)$**
```math
S(s) = \frac{1}{1 + G(s)K(s)}
```

- **補償関数 $T(s)$**
```math
T(s) = \frac{G(s)K(s)}{1 + G(s)K(s)} = 1 - S(s)
```

---

## 🎯 H∞制御の目的 / Objective of H∞ Control

最大ゲイン（無限ノルム）を**最小化**し、最悪誤差に備える。  
Minimize the infinity norm to prepare for the worst-case error.

**目的関数 / Objective function**
```math
\| T_{zw}(s) \|_\infty < \gamma
```
- $T_{zw}(s)$：外乱 $w$ から性能出力 $z$ への伝達関数  
- $\| \cdot \|_\infty$：全周波数帯での最大ゲイン  

---

## 🧩 H∞制御と感度関数 / H∞ & Sensitivity

- $S(s)$ ↑ → 外乱に弱い / Sensitive to disturbances  
- $T(s)$ ↑ → センサノイズに弱い / Sensitive to sensor noise  
- 周波数帯ごとにトレードオフ設計 / Decide trade-off per frequency band

---

## 📈 ロバスト性評価指標 / Robustness Metrics

ロバスト性を定量的に評価する代表的な指標を以下に示します。  
ここで $\|S\|_\infty$ は、感度関数 $S(j\omega)$ の無限ノルム（全周波数帯での最大値）を意味します。

| 指標 / Metric        | 内容 / Description                                      | 目安 / Guideline | ロバスト性 / Robustness |
|----------------------|----------------------------------------------------------|------------------|--------------------------|
| ゲイン余裕 GM        | 増幅許容量 / Gain tolerance                              | > 6 dB           | ○                        |
| 位相余裕 PM          | 遅延許容量 / Phase tolerance                            | > 30°            | ○                        |
| $\|S\|_\infty$       | 感度関数 $S(j\omega)$ の最大値（無限ノルム） / Infinity norm of sensitivity function | < 2.0            | ◎                        |

> **補足 / Note**  
> - $\|S\|_\infty$ が小さいほど、外乱やモデル誤差に対する感度が低く、ロバスト性が高い。  
> - 目安値 2.0 は $6 \ \mathrm{dB}$ に相当し、一般的な設計基準として用いられる。  

---

## ⚙️ 実装ツール例 / Tools

| ツール / Tool | 機能例 / Features |
|---|---|
| MATLAB Robust Control Toolbox | `hinfsyn`, `musyn`, `robstab` |
| Python `slycot`, `robustcontrol` | H∞設計（機能限定） |
| Octave `control.matlab.hinfsyn` | 非公式対応 |

---

## 🛠️ MATLAB/Simulinkによるデジタル H∞ 制御設計例  
**MATLAB & Simulink Digital H∞ Design**

学部時代の **MATLAB/Simulink によるデジタル H∞ 制御設計**をテンプレ化。設計〜離散化〜検証までの最短ルートを示す。

### 1) モデル化と仕様 / Plant & Specs
- プラント：二次遅れ系 + 外乱モデル（例：外乱は低周波帯域）  
- 仕様例：  
  - 低周波域で外乱抑制：\|S(jω)\| < −20 dB  
  - 高周波域でノイズ抑制：\|T(jω)\| < −20 dB  
  - 位相余裕 PM > 40°

### 2) MATLAB による H∞ 設計
```matlab
% 状態空間モデル（例）
A = [...]; B = [...]; C = [...]; D = zeros(size(C,1), size(B,2));
P = ss(A,B,C,D);

% 重み付け（例：性能W1, 制御W2）
s = tf('s');
W1 = (s/10 + 1)/(s/100 + 1);   % 低周波でSを小さく
W2 = (s/100 + 1)/(s/1000 + 1); % 高周波で制御抑制
W1 = ss(W1); W2 = ss(W2);

% 拡大プラント（ブロック構成に応じて結線）
% ここでは概念テンプレ。実装時は series()/connect()/augw を使用。
Paug = augw(P, W1, W2);

% hinfsyn：nmeas=出力計測数, ncon=制御入力数
nmeas = 1; ncon = 1;
[K,CL,gamma] = hinfsyn(Paug, nmeas, ncon);

% 性能確認（特異値プロット）
sigma(CL); grid on
disp(gamma)
```

### 3) 離散化（デジタル実装） / Discretization
- サンプリング周期 $T_s$: 目標帯域の約 1/10  
- 双一次（Tustin）で安定性と位相特性を維持
```matlab
Ts = 0.001;                 % 例：1 ms
Kd = c2d(K, Ts, 'tustin');  % デジタル制御器
```

### 4) Simulink 検証 / Simulink Validation
- `hinf_digital_simulink.slx`：外乱入力・測定ノイズを含む閉ループ  
- 周波数応答：$S$, $T$ を Bode で確認  
- 時間応答：ステップ・外乱応答で過渡と定常を評価

```
(fig) figures/hinf_digital_step.png
(fig) figures/hinf_digital_bode.png
```

### 5) 実装ポイント / Implementation Notes
- **固定小数点化**：係数量子化で位相余裕が低下しやすい  
- **演算遅延**：I/O と演算の総遅延を PM で吸収できるか事前評価  
- **自動コード生成**：Simulink Coder → C → `SoC_DesignKit_by_ChatGPT/c_to_hdl/` で HDL 展開

> 📎 付随ファイル（提案）  
> `part03_adaptive/simulation/hinf_synthesis_matlab.m`  
> `part03_adaptive/simulation/hinf_digital_simulink.slx`  
> `part03_adaptive/figures/hinf_digital_step.png`  
> `part03_adaptive/figures/hinf_digital_bode.png`

---

## 🧠 AITL-H との接続 / Connection to AITL-H

| AITL層 / Layer | 役割 / Role | 関係 / Relation |
|---|---|---|
| 理性 / Reason (PID/Model) | 直接制御 | 設計時に H∞ 安定性を担保 |
| 知性 / Intelligence (LLM) | 制約補完 | 状況に応じ H∞ モードへ切替支援 |

---

**🔗 関連教材 / Related Material:**  
💻 [Part 04 デジタル制御と信号処理 - 06. デジタル H∞ 制御](https://samizo-aitl.github.io/EduController/part04_digital/theory/06_digital_hinf_control.html)  
→ デジタル実装に特化した H∞ 制御の詳細、MATLAB/Simulink モデル、周波数応答評価を解説しています。

---

## 📚 参考文献 / References

- Zhou & Doyle, *Essentials of Robust Control*  
- Skogestad & Postlethwaite, *Multivariable Feedback Control*  
- MATLAB Robust Control Toolbox Documentation  
- Farshad Khorrami, *Robust Control Theory*  

---

**⬅️ 前節 / Previous:** [03. ゲインスケジューリング制御](https://samizo-aitl.github.io/EduController/part03_adaptive/theory/03_gain_scheduling.html)  
**📚 第3章 README / Chapter Top:** [適応制御とロバスト制御](https://samizo-aitl.github.io/EduController/part03_adaptive/)
