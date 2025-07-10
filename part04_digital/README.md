# 💻 Part 04: デジタル制御と信号処理（Digital Control & Signal Processing）

本章では、ディジタル実装を意識した制御設計と信号処理技術を体系的に学びます。  
Z変換、離散PID、デジタルフィルタ、FFT解析など、実機マイコン制御にも直結する内容を扱います。

---

## 🎯 学習目標

- サンプリング理論を理解し、離散制御の基礎を習得する  
- Z変換による離散伝達関数を構築できる  
- 離散PID制御器を設計し、連続系と比較できる  
- FIR/IIRフィルタを設計し、信号処理応用を体験する  
- FFTを用いた信号の周波数解析・雑音除去を実施する

---

## 📘 theory/

| ファイル名                 | 内容 |
|----------------------------|------|
| 01_sampling_theory.md      | サンプリング定理とZOHの基礎 |
| 02_z_transform.md          | Z変換と離散時間伝達関数の構成 |
| 03_digital_pid.md          | 離散PID制御器の設計と比較 |
| 04_fir_iir_filter.md       | FIR/IIRフィルタの構造と設計法 |
| 05_fft_analysis.md         | FFTによる信号の周波数分析と雑音除去 |

---

## 🧪 simulation/

| スクリプト名              | 内容 |
|----------------------------|------|
| digital_pid.py             | 離散PIDと連続PIDの比較シミュレーション |
| iir_fir_filter_demo.py (*) | FIR/IIR通過特性と応答の比較（予定） |
| fft_noise_removal.py       | FFTを用いた周波数成分除去と信号再構成 |

---

## 🖼️ figures/

| ファイル名                  | 内容 |
|-----------------------------|------|
| digital_pid_response.png    | 離散PIDと連続PIDのステップ応答比較 |
| fft_spectrum.png            | FFTによる信号のスペクトルと除去後波形 |

---

## 🧩 応用展開例

| 分野 | 応用内容 |
|------|----------|
| マイコン制御 | 離散PIDやLPFを実装し、センサ信号処理 |
| 振動抑制 | FFTによる振動検出とアクティブ制御 |
| 通信処理 | 周波数帯域の整形とノイズ分離 |
| FPGA処理 | FIR/IIRフィルタのハードウェア化 |

---

## 🚧 今後の予定

- `iir_fir_filter_demo.py` の補完・可視化対応  
- `notebooks/`：インタラクティブNotebook版教材の追加  
- `README_jp.md`：日本語と英語の切替構成化（オプション）  
- `part05_implementation/` への接続準備
