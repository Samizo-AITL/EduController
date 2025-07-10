import time
import random

# 状態定義（FSM）
states = ['IDLE', 'MOVE', 'AVOID', 'CHARGE']
current_state = 'IDLE'

# PID制御の模擬関数
def pid_control(setpoint, measurement):
    error = setpoint - measurement
    control_signal = 0.5 * error  # P制御のみの簡易版
    return control_signal

# LLM模擬関数（条件に応じて次の状態を返す）
def llm_decision(state, context):
    if "battery low" in context:
        return 'CHARGE'
    elif "obstacle" in context:
        return 'AVOID'
    elif "task start" in context:
        return 'MOVE'
    else:
        return 'IDLE'

# シミュレーションループ
for t in range(10):
    print(f"[t={t}] Current State: {current_state}")

    # 観測データの生成（模擬）
    context = random.choice([
        "normal", "battery low", "obstacle ahead", "task start"
    ])

    # LLMで次状態を決定（知性層）
    next_state = llm_decision(current_state, context)
    print(f"  LLM suggests: {next_state} (context: {context})")

    # 状態遷移（FSM）
    if next_state != current_state:
        print(f"  FSM Transition: {current_state} → {next_state}")
        current_state = next_state

    # 制御信号の生成（PID層：MOVEのみ）
    if current_state == 'MOVE':
        setpoint = 10.0
        measurement = random.uniform(7.0, 12.0)
        control = pid_control(setpoint, measurement)
        print(f"  PID control: target={setpoint:.1f}, measured={measurement:.2f}, output={control:.2f}")
    elif current_state == 'AVOID':
        print("  Avoiding obstacle...")
    elif current_state == 'CHARGE':
        print("  Charging...")
    else:
        print("  System idle...")

    time.sleep(0.5)
