---
layout: clean
title: ChatGPTプロンプトテンプレート：PID制御器の Verilog 変換
permalink: /hdl/pid_prompt_template/
---

---

# 🤖 ChatGPTプロンプトテンプレート：PID制御器の Verilog 変換  
Prompt Template for Converting a PID Controller from C to Verilog HDL

このテンプレートは、**C言語で記述されたPID制御ロジック**を  
**Verilog HDL**に変換するために、ChatGPTやGPT-4oへ与える指示例を示します。  
This template is for instructing ChatGPT/GPT-4o to convert a PID controller written in C into synthesizable Verilog HDL.

---

## 📥 入力例（Cコード / Example C Code）

```c
// PID Controller in C
double Kp = 1.0, Ki = 0.1, Kd = 0.01;
double integral = 0.0, prev_error = 0.0;

double pid(double setpoint, double measured, double dt) {
    double error = setpoint - measured;
    integral += error * dt;
    double derivative = (error - prev_error) / dt;
    double output = Kp * error + Ki * integral + Kd * derivative;
    prev_error = error;
    return output;
}
```

---

## 🤖 ChatGPTプロンプト例（英語 / Example Prompt in English）

```
You are an HDL expert. Please convert the following PID control algorithm written in C into Verilog HDL.

- Target: Fixed-point implementation (e.g. Q8.8)
- Sampling time: Assume 'dt' is constant
- Avoid any floating-point operation
- Output should be synthesizable Verilog

Here is the C code:
[Paste the C code here]
```

---

## 📝 出力例（簡易 / Example Verilog Output）

```verilog
module pid_controller (
    input wire clk,
    input wire reset,
    input wire signed [15:0] setpoint,   // Q8.8
    input wire signed [15:0] measured,   // Q8.8
    output reg signed [15:0] output_signal // Q8.8
);
// Constants: Kp = 1.0 (256), Ki = 0.1 (26), Kd = 0.01 (3)

reg signed [15:0] error, derivative, prev_error;
reg signed [31:0] integral;

always @(posedge clk or posedge reset) begin
    if (reset) begin
        integral <= 0;
        prev_error <= 0;
        output_signal <= 0;
    end else begin
        error <= setpoint - measured;
        integral <= integral + error;
        derivative <= error - prev_error;
        output_signal <= (error * 256 >>> 8) +
                         (integral * 26 >>> 8) +
                         (derivative * 3 >>> 8);
        prev_error <= error;
    end
end

endmodule
```

---

## 🔗 関連リンク / Related Links

- [`hdl_implementation/pid_controller.v`](../hdl_implementation/pid_controller.v) — 実装版  
- [`testbench/pid_testbench.v`](../testbench/pid_testbench.v) — 動作確認用テストベンチ  
