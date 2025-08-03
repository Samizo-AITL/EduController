```markdown
# 💻 Part 04: デジタル制御と信号処理  
# 💻 Part 04: Digital Control & Signal Processing

本章では、**ディジタル実装**を意識した制御設計と信号処理技術を体系的に学びます。  
**Z変換、離散PID、デジタルフィルタ、FFT解析**など、実機マイコン制御にも直結する内容を扱います。

This chapter systematically covers **control and signal processing techniques** for digital implementation,  
including **Z-transform, discrete PID, digital filters, and FFT analysis**—all applicable to real embedded control.

---

## 🎯 **学習目標 / Learning Objectives**

- サンプリング理論を理解し、**離散制御の基礎**を習得する  
  Understand **sampling theory** and the fundamentals of discrete control  
- Z変換による**離散伝達関数**を構築できる  
  Construct **discrete transfer functions** using Z-transform  
- **離散PID制御器**を設計し、連続系と比較できる  
  Design **discrete PID controllers** and compare them with continuous counterparts  
- **FIR/IIRフィルタ**を設計し、信号処理応用を体験する  
  Design **FIR/IIR filters** and experience their use in signal processing  
- **FFT**を用いた信号の**周波数解析・雑音除去**を実施する  
  Apply **FFT** to analyze **frequency components** and remove noise

---

## 📘 **教材ファイル / Theory Materials** [`theory/`](theory/)

| **ファイル名 / File** | **内容 / Description** |
|------------------------|-------------------------|
| [`01_sampling_theory.md`](theory/01_sampling_theory.md) | サンプリング定理とZOHの基礎<br>Sampling theorem and ZOH |
| [`02_z_transform.md`](theory/02_z_transform.md) | Z変換と離散時間伝達関数<br>Z-transform and discrete-time transfer functions |
| [`03_digital_pid.md`](theory/03_digital_pid.md) | 離散PID制御器の設計と比較<br>Design and comparison of discrete PID |
| [`04_fir_iir_filter.md`](theory/04_fir_iir_filter.md) | FIR/IIRフィルタの構造と設計法<br>FIR/IIR structure and design |
| [`05_fft_analysis.md`](theory/05_fft_analysis.md) | FFTによる信号の周波数分析と雑音除去<br>FFT for spectrum analysis and noise removal |

---

## 🧪 **シミュレーション / Simulation Scripts** [`simulation/`](simulation/)

| **スクリプト名 / Script** | **内容 / Description** |
|----------------------------|-------------------------|
| [`digital_pid.py`](simulation/digital_pid.py) | 離散PIDと連続PIDの比較シミュレーション<br>Simulate and compare digital vs. continuous PID |
| [`iir_fir_filter_demo.py`](simulation/iir_fir_filter_demo.py) (*) | FIR/IIRフィルタの通過特性比較（予定）<br>Planned: FIR/IIR filter response demo |
| [`fft_noise_removal.py`](simulation/fft_noise_removal.py) | FFTによる雑音除去と信号再構成<br>Noise removal and reconstruction using FFT |

---

## 🖼️ **図・可視化 / Figures** [`figures/`](figures/)

| **ファイル名 / Figure** | **内容 / Description** |
|--------------------------|-------------------------|
| [`digital_pid_response.png`](figures/digital_pid_response.png) | 離散PIDと連続PIDのステップ応答比較<br>Step response: discrete vs. continuous PID |
| [`fft_spectrum.png`](figures/fft_spectrum.png) | FFTによるスペクトル解析と除去後波形<br>FFT spectrum and filtered waveform |

---

## 🧩 **応用展開例 / Application Examples**

| **分野 / Field** | **応用内容 / Application** |
|------------------|----------------------------|
| マイコン制御 / Microcontroller | 離散PIDやLPFを用いたセンサ信号処理<br>Sensor processing with PID/LPF |
| 振動抑制 / Vibration Control | FFTによる振動検出とアクティブ制御<br>FFT-based vibration analysis & control |
| 通信処理 / Communication | 周波数帯域の整形とノイズ分離<br>Band shaping and noise separation |
| FPGA処理 / FPGA Systems | FIR/IIRフィルタのハードウェア実装<br>Hardware implementation of digital filters |

---

## 🚧 **今後の予定 / Upcoming Tasks**

- [`iir_fir_filter_demo.py`](simulation/iir_fir_filter_demo.py) の補完とプロット整備  
  **Complete FIR/IIR simulation and plotting**  
- [`notebooks/`](./notebooks/) ディレクトリに Jupyter Notebook 版を追加  
  **Add interactive Jupyter Notebook versions**  
- `README_jp.md` の英日切替対応（GitHub Pages対応構想）  
  **Add EN/JP toggle-ready structure for public view**  
- 次章 [`part05_implementation/`](../part05_implementation/) との連携準備  
  **Connect with next section: Implementation on real systems**

---

## 👤 **著者・ライセンス / Author & License**

| **項目 / Item** | **内容 / Details** |
|------------------|---------------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo）<br>Shinshu University / Ex-Epson |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

📎 **[トップに戻る / Back to Home](../README.md)**
```
