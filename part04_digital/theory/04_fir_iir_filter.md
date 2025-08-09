---
layout: default
title: "📡 04. FIR/IIR フィルタ設計と応答特性（Digital Filters: FIR & IIR）"
permalink: /part04_digital/theory/04_fir_iir_filter.html
---

---

# 📡 04. FIR/IIR フィルタ設計と応答特性（Digital Filters: FIR & IIR）

> ℹ️ **Webで数式が正しく表示されない場合 / If equations don't render:** [GitHub版はこちら](https://github.com/Samizo-AITL/EduController/blob/main/part04_digital/theory/04_fir_iir_filter.md)

---

ディジタル信号処理の中心的技術である **FIR/IIRフィルタ**は、  
制御系でも **ノイズ除去** や **信号平滑化**、**前処理** などに広く応用されます。

---

## 🎯 学習目標

- **FIR（有限インパルス応答）** と **IIR（無限インパルス応答）** の違いを理解する  
- 離散時間でのフィルタ構造と数式表現を習得  
- PythonでFIR/IIRを設計・可視化できる  
- 雑音除去や帯域制限の実例を体験する

---

## 🔁 FIR vs IIR フィルタの比較

| 項目        | FIRフィルタ | IIRフィルタ |
|-------------|-------------|-------------|
| 応答        | 有限インパルス応答 | 無限インパルス応答 |
| 構造        | 遅延と加算のみ | 遅延・加算 + フィードバック |
| 安定性      | 常に安定 | 極が単位円内なら安定 |
| 計算負荷    | 多め（高次数） | 少なめ（低次数でも急峻） |
| 設計容易性  | 線形位相が容易 | 位相特性が複雑 |

---

## 🧮 離散時間フィルタの数式表現

**FIRフィルタ：**
$$
y[k] = b_0 x[k] + b_1 x[k-1] + \dots + b_N x[k-N]
$$

**IIRフィルタ：**
$$
y[k] = b_0 x[k] + \dots + b_N x[k-N] - a_1 y[k-1] - \dots - a_M y[k-M]
$$

---

## 🧩 Z変換での表現

- **FIR:**  
  $$
  H(z) = \sum_{i=0}^N b_i z^{-i}
  $$

- **IIR:**  
  $$
  H(z) = \frac{b_0 + \dots + b_N z^{-N}}{1 + a_1 z^{-1} + \dots + a_M z^{-M}}
  $$

---

## 🧪 Pythonによる設計例

```python
from scipy.signal import firwin, lfilter

# FIRフィルタ設計（窓関数法）
b = firwin(numtaps=51, cutoff=0.2)  # カットオフ正規化0.2
y = lfilter(b, 1.0, x)  # 信号xに適用
```

---

## 🧠 制御用途での選択目安

| 目的 | 推奨 | 理由 |
|------|------|------|
| センサノイズ除去 | FIRまたはIIR-LPF | 高周波成分除去 |
| スパイク除去 | 移動平均FIR | 簡易平滑化 |
| 位相遅れ低減 | FIR（線形位相） | 波形維持 |

---

## 📚 参考資料

- Proakis, *Digital Signal Processing*  
- Oppenheim & Schafer, *Discrete-Time Signal Processing*  
- [SciPy Signal Documentation](https://docs.scipy.org/doc/scipy/reference/signal.html)

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part04_digital/theory/03_digital_pid.html)**  
離散PID制御の設計と実装方法を解説。

**➡️➡️ [次節 / Next](https://samizo-aitl.github.io/EduController/part04_digital/theory/05_fft_analysis.html)**  
FFTによる周波数解析とノイズ除去を学習。

**🏠 [Part 04 トップ / Back to Part 04 Top](https://samizo-aitl.github.io/EduController/part04_digital/)**
