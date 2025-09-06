# Simulation README (Part09)

## Files
- `fsm_pid_llm_sim.py` — FSM × PID × LLM integrated PoC simulator.
- `goal_reasoning_agent.py` — Minimal goal reasoning agent with rule-based mock in place of LLM.

## Quick Run
```bash
python simulation/fsm_pid_llm_sim.py
```

## Headless Logs & Plot
```bash
python notebooks/run_demo.py
# outputs to notebooks/artifacts/{logs.csv, state_over_time.png}
```

## Contract Notes
- The simulator treats PID as the **only** real-time loop.
- FSM supervises modes; LLM (mock) only proposes transitions/goals under exceptions.
