import time
import random

class FSM_PID_LLM_Simulator:
    def __init__(self):
        # 状態定義
        self.states = ['IDLE', 'MOVE', 'AVOID', 'CHARGE']
        self.current_state = 'IDLE'
        self.logs = []

    # PID制御（簡易P制御）
    def pid_control(self, setpoint, measurement):
        error = setpoint - measurement
        control_signal = 0.5 * error  # 本来は P+I+D の組合せ
        return control_signal

    # LLM模擬関数
    def llm_decision(self, state, context):
        if "battery low" in context:
            return 'CHARGE'
        elif "obstacle" in context:
            return 'AVOID'
        elif "task start" in context:
            return 'MOVE'
        else:
            return 'IDLE'

    # 1ステップの更新
    def step(self, t):
        context = random.choice([
            "normal", "battery low", "obstacle ahead", "task start"
        ])
        next_state = self.llm_decision(self.current_state, context)

        log = {
            "time": t,
            "state": self.current_state,
            "context": context,
            "llm_suggest": next_state
        }

        # 状態遷移（FSM）
        if next_state != self.current_state:
            log["transition"] = f"{self.current_state} → {next_state}"
            self.current_state = next_state

        # 制御動作
        if self.current_state == 'MOVE':
            setpoint = 10.0
            measurement = random.uniform(7.0, 12.0)
            control = self.pid_control(setpoint, measurement)
            log["pid"] = {
                "target": setpoint,
                "measured": measurement,
                "output": control
            }
        elif self.current_state == 'AVOID':
            log["action"] = "Avoiding obstacle"
        elif self.current_state == 'CHARGE':
            log["action"] = "Charging"
        else:
            log["action"] = "System idle"

        self.logs.append(log)
        return log

    # シミュレーション実行
    def run(self, steps=10, delay=0.5):
        for t in range(steps):
            log = self.step(t)
            print(f"[t={log['time']}] State: {log['state']} | Context: {log['context']} | Next: {log['llm_suggest']}")
            if "transition" in log:
                print(f"  FSM Transition: {log['transition']}")
            if "pid" in log:
                pid = log["pid"]
                print(f"  PID control: target={pid['target']}, measured={pid['measured']:.2f}, output={pid['output']:.2f}")
            if "action" in log:
                print(f"  {log['action']}")
            time.sleep(delay)

if __name__ == "__main__":
    sim = FSM_PID_LLM_Simulator()
    sim.run(steps=10, delay=0.3)
