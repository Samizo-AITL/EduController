---
layout: default
title: "📡 04. FIR/IIR フィルタ設計と応答特性（Digital Filters: FIR & IIR）"
permalink: /part04_digital/theory/04_fir_iir_filter.html
---

---

# 📡 04. FIR/IIR フィルタ設計と応答特性  
**Digital Filters: FIR & IIR**

> ℹ️ **Webで数式が表示されない場合 / If equations don't render:** [GitHub版はこちら](https://github.com/Samizo-AITL/EduController/blob/main/part04_digital/theory/04_fir_iir_filter.md)

---

ディジタル信号処理の要である **FIR/IIRフィルタ** は、  
制御系でも **ノイズ除去**・**信号平滑化**・**前処理** に広く応用されます。

---

## 🎯 学習目標 / Learning Goals

- **FIR** と **IIR** の構造・特性を理解する  
- 離散時間フィルタの数式表現を習得する  
- Pythonで設計・応答可視化を行える  
- 制御系における応用例を挙げられる

---

## 🔁 FIR vs IIR の比較表

| **項目 / Item**   | **FIRフィルタ** | **IIRフィルタ** |
|------------------|----------------|----------------|
| 応答 / Response  | 有限インパルス応答 | 無限インパルス応答 |
| 構造 / Structure | 遅延+加算のみ     | 遅延+加算+FB（フィードバック） |
| 安定性 / Stability | 常に安定         | 極が単位円内で安定 |
| 計算負荷 / Load   | 高（高次数必要）  | 低（低次数でも急峻） |
| 位相特性 / Phase  | 線形位相が容易    | 位相が複雑         |

---

## 🧮 数式表現 / Mathematical Formulation

**FIR:**

$$
y[k] = b_0 x[k] + b_1 x[k-1] + \dots + b_N x[k-N]
$$

**IIR:**

$$
y[k] = b_0 x[k] + \dots + b_N x[k-N] - a_1 y[k-1] - \dots - a_M y[k-M]
$$

---

## 🧩 Z変換表現 / Z-domain Representation

- **FIR:**
  
$$
H(z) = \sum_{i=0}^N b_i z^{-i}
$$

- **IIR:**

$$
H(z) = \frac{b_0 + \dots + b_N z^{-N}}{1 + a_1 z^{-1} + \dots + a_M z^{-M}}
$$

---

## 🧪 Python実装例 / Python Example

```python
from scipy.signal import firwin, lfilter
import numpy as np

# サンプル信号
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
x = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*300*t)

# FIR設計（カットオフ200Hz）
b = firwin(numtaps=51, cutoff=200, fs=fs)
y = lfilter(b, 1.0, x)
```

---

## 🧠 制御系での選択指針 / Filter Selection Guide

| **目的 / Purpose**   | **推奨 / Recommendation** | **理由 / Reason** |
|----------------------|---------------------------|-------------------|
| センサノイズ除去 | FIRまたはIIR-LPF | 高周波成分除去 |
| スパイク除去     | 移動平均FIR | 平滑化が効く |
| 位相遅れ低減     | FIR（線形位相） | 波形を忠実に保持 |

---

## 📚 参考文献 / References

- Proakis, *Digital Signal Processing*  
- Oppenheim & Schafer, *Discrete-Time Signal Processing*  
- [SciPy Signal Documentation](https://docs.scipy.org/doc/scipy/reference/signal.html)

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part04_digital/theory/03_digital_pid.html)**  
離散PID制御の設計と実装方法を解説。

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part04_digital/theory/05_fft_analysis.html)**  
FFTによる周波数解析とノイズ除去を学習。

**🏠 [Part 04 トップ / Back to Part 04 Top](https://samizo-aitl.github.io/EduController/part04_digital/)**
