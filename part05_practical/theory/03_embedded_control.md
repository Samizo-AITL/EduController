---
layout: default
title: "🔧 03. 組み込み制御への展開（Embedded Control）"
permalink: /part05_practical/theory/03_embedded_control.html
---

---

# 🔧 03. 組み込み制御への展開（Embedded Control）

> ℹ️ **Webで数式が正しく表示されない場合はこちら** → [GitHub版を見る](https://github.com/Samizo-AITL/EduController/blob/main/part05_practical/theory/03_embedded_control.md)

---

本節では、制御理論を **マイコン・組込み環境（C/Arduino等）** へ展開するための考え方と設計法を解説します。  
離散時間制御・近似モデル・固定小数点演算など、実装面の注意点を押さえます。

This section explains how to implement control theory in **microcontroller / embedded environments** (C/Arduino),  
covering discrete-time control, approximation models, and fixed-point arithmetic considerations.

---

## 🎯 学習目標 / Learning Objectives

- 離散化された制御則をC言語・Arduinoで実装できる  
- サンプリング周期とリアルタイム処理の関係を理解する  
- PID制御の離散時間近似を用いたループ制御を構成できる  
- センサ/アクチュエータとのインタフェース原理を理解する  

---

## 🧮 離散PID制御の実装形式 / Discrete PID Implementation

### 離散化の基本形（Tustin法） / Basic Discretization (Tustin Method)

連続時間PID：
$$
u(t) = K_p e(t) + K_i \int e(t)dt + K_d \frac{de(t)}{dt}
$$

離散化例（C/Arduino）:
```c
// Discrete PID for C/Arduino
float e = ref - y;
integral += e * dt;
derivative = (e - prev_e) / dt;
u = Kp * e + Ki * integral + Kd * derivative;
prev_e = e;
```
- `ref`：目標値 / Setpoint  
- `y`：現在値 / Current output  
- `dt`：サンプリング周期 / Sampling period  
- `Kp, Ki, Kd`：各ゲイン / Gains

---

## 🔌 ハードウェア構成例 / Hardware Setup Example

| 構成要素 / Component | 役割 / Role                   | 具体例 / Example              |
|----------------------|--------------------------------|--------------------------------|
| Arduino UNO / STM32  | 制御演算の実行 / Control calc  | PID計算・PWM出力               |
| モータ＋ドライバ     | アクチュエータ / Actuator      | DCモータ、TB6612FNG             |
| センサ               | 状態観測 / State sensing      | ホールIC、ロータリエンコーダ   |
| シリアル通信         | PC連携 / PC communication     | `Serial.print()` / Python link |

💡 センサ入力 → 制御演算 → アクチュエータ出力（PWM）のループを形成。

---

## 📏 タイミング設計の注意点 / Timing Design Considerations

| 項目 / Item         | 推奨・注意点 / Recommendation            |
|---------------------|------------------------------------------|
| サンプリング周期    | 10〜100ms（10Hz〜100Hz）                  |
| 実行時間            | 計算＋出力が周期内に収まること            |
| 割り込み制御        | `TimerInterrupt` 推奨                    |
| delay()の使用       | 非推奨（精度低下）                       |
| 周波数選定          | 応答速度に応じて決定                     |

⚠️ 高速応答モータでは1kHz以上が必要な場合あり。

---

## 💡 固定小数点演算 / Fixed-Point Arithmetic

8bit MCUではfloat演算が遅い場合、固定小数点＋スケーリング推奨。

```c
// 16bit fixed-point PID term
int16_t e = ref - y;
int32_t p_term = (int32_t)(Kp * e) >> scale;
```
- `>> scale` は高速除算の代替  
- 実効ゲイン = Kp / 2^scale

---

## 🛠️ 実装例ファイル / Implementation Files

| ファイル / File              | 内容 / Description               |
|------------------------------|-----------------------------------|
| `pid_embedded.ino`           | Arduino離散PID                    |
| `sensor_plotter.py`          | Pythonでセンサデータ可視化        |
| `arduino_serial_logger.py`   | シリアルログ取得                  |

💡 Pythonとの連携で可視化・デバッグが容易に。

---

## 📡 シリアル通信例 / Serial Communication Example

```python
import serial
import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 9600)
data = []

for _ in range(200):
    line = ser.readline().decode().strip()
    data.append(float(line))

plt.plot(data)
plt.title("Sensor Output from Arduino")
plt.grid()
plt.show()
```

---

## 📘 制御対象例 / Example Targets

| 制御対象 / Target    | 内容 / Feature                | 備考 / Note |
|----------------------|-------------------------------|-------------|
| DCモータ速度制御     | PWM＋エンコーダ                | 安定化・追従 |
| 温度制御             | サーミスタ＋ヒーター           | 恒温槽等    |
| 電流制御             | シャント抵抗＋スイッチング     | 電源系      |
| 2輪自律移動体        | 左右モータ制御＋姿勢安定化     | 倒立振子等 |
| LED輝度制御          | 照度センサ＋PWM                | 照明制御   |

---

## 📚 参考 / References

- [Arduino PID by Brett Beauregard](https://brettbeauregard.com/blog/2011/04/improving-the-beginners-pid-introduction/)  
- [ROS + STM32](https://wiki.ros.org/rosserial_arduino)  
- 丸善・CQ出版「組込み制御開発のための教科書」  

---

**⬅️ [前節 / Previous](https://samizo-aitl.github.io/EduController/part05_practical/theory/02_python_control.html)**  
Pythonによる制御設計の基礎を解説。  
Covers basics of control design in Python.

**🏠 [第5章トップ / Back to Part 5 Top](https://samizo-aitl.github.io/EduController/part05_practical/)**
