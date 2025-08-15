---
layout: clean
title: Verilog HDL PID制御器（Q8.8固定小数点形式）
permalink: /hdl/pid_q8_8/
---

---

# 🔧 Verilog HDL: PID制御器（Q8.8固定小数点形式）  
Verilog HDL: PID Controller in Q8.8 Fixed-Point Format

本ファイルは、**倒立振子やモータ制御**などリアルタイム応用向けの  
**合成可能な固定小数点（Q8.8）PID制御器**の記述例です。  
This file provides a synthesizable Q8.8 fixed-point PID controller in Verilog HDL,  
suitable for real-time control such as inverted pendulum or motor systems.

---

## 💡 仕様概要 / Specifications

| 項目 / Item | 内容 / Details |
|-------------|----------------|
| **入力 / Inputs** | `setpoint`, `measured`：16-bit signed Q8.8 |
| **出力 / Output** | `control_out`：制御信号（Q8.8形式） |
| **内部演算 / Internal Ops** | 比例・積分・微分計算、誤差の過去値保持 |
| **合成可否 / Synthesizability** | ✅ 合成可能（FPGA / ASIC向け） |

---

## 📄 Verilog ソースコード / Source Code

```verilog
// ============================================================
// pid_controller.v
// 固定小数点Q8.8形式による合成可能なPID制御器
// PID Controller (Synthesizable) using Q8.8 Fixed-Point Format
// ============================================================

module pid_controller (
    input  wire clk,                              // クロック信号 / Clock
    input  wire rst,                              // 非同期リセット / Asynchronous Reset
    input  wire signed [15:0] setpoint,           // 目標値 / Setpoint (Q8.8)
    input  wire signed [15:0] measured,           // 測定値 / Measured value (Q8.8)
    output reg  signed [15:0] control_out         // 出力制御信号 / Control output (Q8.8)
);

    // ==============================================
    // 制御ゲイン定義（Q8.8形式）
    // Control gains in Q8.8 fixed-point format
    // 例: Kp = 1.0 → 256, Ki = 0.1 → 26, Kd = 0.01 → 3
    // ==============================================
    parameter signed [15:0] Kp = 16'd256;  // 比例ゲイン / Proportional Gain
    parameter signed [15:0] Ki = 16'd26;   // 積分ゲイン / Integral Gain
    parameter signed [15:0] Kd = 16'd3;    // 微分ゲイン / Derivative Gain

    // 内部信号定義 / Internal registers
    reg signed [15:0] error;               // 現在の誤差 / Current error
    reg signed [31:0] integral;            // 積分項（拡張ビット幅）/ Integral term (wider bit width)
    reg signed [15:0] derivative;          // 微分項 / Derivative term
    reg signed [15:0] prev_error;           // 前回の誤差 / Previous error

    // ==============================================
    // PID 演算部 / PID Calculation
    // ==============================================
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            error       <= 0;
            integral    <= 0;
            derivative  <= 0;
            prev_error  <= 0;
            control_out <= 0;
        end else begin
            // 誤差計算 / Calculate error
            error <= setpoint - measured;

            // 積分項更新（Windup防止は別途追加可能）
            // Update integral term (Anti-windup can be added separately)
            integral <= integral + error;

            // 微分項計算 / Calculate derivative term
            derivative <= error - prev_error;

            // PID 出力計算（Q8.8 → シフトでスケーリング）
            // PID output calculation with scaling via bit shift
            control_out <= (Kp * error      >>> 8) +
                           (Ki * integral   >>> 8) +
                           (Kd * derivative >>> 8);

            // 誤差更新 / Update previous error
            prev_error <= error;
        end
    end

endmodule
