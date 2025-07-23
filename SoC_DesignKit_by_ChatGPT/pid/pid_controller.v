// pid_controller.v
// 固定小数点（Q4.4）によるPID制御器（Verilog RTL）

module pid_controller (
    input clk,
    input rst,
    input signed [7:0] ref,     // 目標値 (Q4.4)
    input signed [7:0] meas,    // 測定値 (Q4.4)
    output signed [7:0] ctrl_out // 出力 (Q4.4)
);

    // ゲイン係数（定数として記述）
    parameter signed [7:0] Kp = 8'sd16;  // 1.0 in Q4.4
    parameter signed [7:0] Ki = 8'sd4;   // 0.25 in Q4.4

    reg signed [7:0] error;
    reg signed [15:0] integral; // 積分項（8.8bit幅）

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            error    <= 0;
            integral <= 0;
        end else begin
            error    <= ref - meas;
            integral <= integral + error;
        end
    end

    wire signed [15:0] p_term = Kp * error;
    wire signed [15:0] i_term = Ki * integral[15:8]; // 上位8bitを抽出（Q4.4）

    wire signed [15:0] pid_raw = p_term + i_term;
    assign ctrl_out = pid_raw[15:8]; // Q4.4スケーリング

endmodule
