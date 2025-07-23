> 💡 ChatGPTに直接渡す際は、「Verilogのモジュールとして出力して」なども追加可。

---

## ③ 📄 `verilog_output.v`（出力例）

```verilog
// verilog_output.v
// ChatGPTにより変換されたPID制御のVerilogコード例

module pid_from_c (
    input clk,
    input rst,
    input signed [7:0] ref,
    input signed [7:0] meas,
    input signed [7:0] Kp,
    input signed [7:0] Ki,
    output reg signed [7:0] output_val
);

    reg signed [7:0] error;
    reg signed [15:0] integral;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            error <= 0;
            integral <= 0;
            output_val <= 0;
        end else begin
            error <= ref - meas;
            integral <= integral + error;
            output_val <= (Kp * error + Ki * integral[15:8]) >>> 4;
        end
    end

endmodule
```
