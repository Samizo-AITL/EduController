// tb_pid_controller.v
// Verilog用 PID制御器のテストベンチ

`timescale 1ns/1ps

module tb_pid_controller;

  reg clk = 0;
  reg rst = 1;
  reg signed [7:0] ref = 8'sd32;    // 目標値 2.0（Q4.4）
  reg signed [7:0] meas = 8'sd0;    // 初期測定値
  wire signed [7:0] ctrl_out;

  // 被試験モジュールのインスタンス
  pid_controller uut (
    .clk(clk),
    .rst(rst),
    .ref(ref),
    .meas(meas),
    .ctrl_out(ctrl_out)
  );

  // クロック生成（50MHz相当）
  always #10 clk = ~clk;

  initial begin
    $dumpfile("wave.vcd");
    $dumpvars(0, tb_pid_controller);

    // 初期リセット
    #20 rst = 0;

    // シミュレーション時間制限
    #200 $finish;
  end

  // 測定値の変化（簡易）
  always @(posedge clk) begin
    if (!rst) begin
      meas <= meas + 8'sd2;  // 毎サイクル追従
    end
  end

endmodule
