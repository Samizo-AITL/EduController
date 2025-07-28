# 🔧 Verilog HDL: PID制御器（Q8.8固定小数点形式）

本ファイルは、倒立振子などリアルタイム制御への応用を想定した **PID制御器のHDL記述例** です。  
固定小数点（Q8.8）による加算・乗算を用い、**合成可能なVerilog構文**で記述しています。

---

## 💡 仕様概要

- **入力**
  - `setpoint`, `measured`：16bit 符号付き Q8.8 形式
- **出力**
  - `control_out`：制御信号（Q8.8）
- **内部処理**
  - 比例、積分、微分項の加算
  - 過去エラー値保持（`prev_error`）

---

## 📄 Verilogソースコード

```verilog
// pid_controller.v
// 固定小数点Q8.8形式による簡易PID制御器（合成可能な構文）

module pid_controller (
    input wire clk,
    input wire rst,
    input wire signed [15:0] setpoint,   // Q8.8
    input wire signed [15:0] measured,   // Q8.8
    output reg signed [15:0] control_out // Q8.8
);

// 定数係数（例: Kp = 1.0, Ki = 0.1, Kd = 0.01）
parameter signed [15:0] Kp = 16'd256;  // 1.0 * 256
parameter signed [15:0] Ki = 16'd26;   // 0.1 * 256
parameter signed [15:0] Kd = 16'd3;    // 0.01 * 256

reg signed [15:0] error;
reg signed [31:0] integral;     // 拡張ビット幅
reg signed [15:0] derivative;
reg signed [15:0] prev_error;

always @(posedge clk or posedge rst) begin
    if (rst) begin
        error <= 0;
        integral <= 0;
        derivative <= 0;
        prev_error <= 0;
        control_out <= 0;
    end else begin
        error <= setpoint - measured;
        integral <= integral + error;
        derivative <= error - prev_error;
        control_out <= (Kp * error >>> 8) + (Ki * integral >>> 8) + (Kd * derivative >>> 8);
        prev_error <= error;
    end
end

endmodule
```
