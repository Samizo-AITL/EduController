# 🤖 ChatGPTプロンプトテンプレート：PID制御器の Verilog 変換

このテンプレートは、**C言語で記述されたPID制御ロジック**を**Verilog HDL**に変換するために、ChatGPTやGPT-4oに与えるプロンプトの例です。

---

## 📥 入力例（Cコード）

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

## 🤖 ChatGPTプロンプト例（英語）

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

## 📝 出力例（簡易）

```verilog
module pid_controller (
    input wire clk,
    input wire reset,
    input wire signed [15:0] setpoint,
    input wire signed [15:0] measured,
    output reg signed [15:0] output_signal
);
// Fixed-point: Q8.8
// Constants: Kp = 1.0 (256), Ki = 0.1 (26), Kd = 0.01 (3)

reg signed [15:0] error, integral, derivative, prev_error;

always @(posedge clk or posedge reset) begin
    if (reset) begin
        integral <= 0;
        prev_error <= 0;
        output_signal <= 0;
    end else begin
        error <= setpoint - measured;
        integral <= integral + error;
        derivative <= error - prev_error;
        output_signal <= (error <<< 8) + (integral * 26 >>> 8) + (derivative * 3 >>> 8);
        prev_error <= error;
    end
end

endmodule
```

---

## 🔗 関連

- `hdl_implementation/pid_controller.v` にて生成結果を実装
- `testbench/pid_testbench.v` にて動作確認を推奨
