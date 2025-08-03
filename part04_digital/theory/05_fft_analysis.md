# 🔍 05. FFTによる周波数解析とノイズ除去（Frequency Analysis with FFT）

制御対象の振動や信号の周期性を解析するには、**周波数領域の理解**が重要です。  
この章では、**高速フーリエ変換（FFT）**を用いた信号解析・ノイズ除去の方法を学びます。

---

## 🎯 学習目標

- FFT（高速フーリエ変換）の基本動作を理解する  
- 離散フーリエ変換（DFT）との関係を説明できる  
- 周波数スペクトルをPythonで可視化できる  
- 高周波ノイズ除去や特定帯域抽出を体験する

---

## 📐 離散フーリエ変換（DFT）の定義

$$
X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-j \frac{2\pi}{N}kn}, \quad k = 0, \dots, N-1
$$

- $x[n]$：時間領域の信号、$X[k]$：周波数領域のスペクトル  
- $N$：サンプル数（$2^n$ が理想）

---

## ⚡ FFT（Fast Fourier Transform）

- DFTを**高速に計算**するアルゴリズム  
- Pythonの `numpy.fft.fft()` や `scipy.fft` で簡単に使用可能

---

## 🧪 PythonでのFFT解析例（次章で実装）

- サンプリング周波数  $f_s = 1000$ Hz  
- 合成信号：50Hz（信号） + 300Hz（ノイズ）  
- スペクトルを可視化してノイズ成分を確認  
- 高周波成分を除去し、IFFTで再構成（フィルタリング）

---

## 🧩 実践応用例

| 用途 | 説明 |
|------|------|
| センサノイズ除去 | 高周波ピークを除去（ローパス相当） |
| モータ・振動診断 | 高調波・共振ピークを検出 |
| 通信解析 | 周波数帯域の干渉確認 |
| 変調解析 | AM/FM成分の復調などに応用可能 |

---

## 🎨 FFTスペクトルの読み方

- $X[k]$ の絶対値をプロット： $|X[k]|$  
- 周波数軸のスケーリング：
  $$
  f[k] = \frac{k \cdot f_s}{N}
  $$

- 対称性：実数信号なら **スペクトルは左右対称**

---

## 💡 周波数除去の基本アイデア（手動マスキング）

```python
X = np.fft.fft(x)
X_filtered = X.copy()
X_filtered[100:200] = 0  # 特定帯域を除去
x_filtered = np.fft.ifft(X_filtered).real
```

---

## 📚 参考資料
- Oppenheim & Schafer, Signals and Systems
- Lyons, Understanding Digital Signal Processing
- numpy/scipy の FFT 関数ドキュメント

---


