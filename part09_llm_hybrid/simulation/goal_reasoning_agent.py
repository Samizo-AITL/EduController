# -*- coding: utf-8 -*-
"""
GoalReasoningAgent (revised)
- 目的（ゴール）を自然言語観測から更新する最小エージェント。
- 教材/PoC用：LLMの代わりに単純なキーワードルールで模擬推論。
- Notebookや他モジュールから再利用できるよう、入出力を構造化。

使い方:
    from goal_reasoning_agent import GoalReasoningAgent
    agent = GoalReasoningAgent(initial_goal="IDLE")
    goal, meta = agent.decide_next_goal("battery low warning")
    print(goal)  # -> 'CHARGE'
"""

from dataclasses import dataclass, field
from typing import Dict, Tuple

@dataclass
class GoalReasoningAgent:
    initial_goal: str = "IDLE"
    verbose: bool = True
    rules: Dict[str, str] = field(default_factory=lambda: {
        "battery low": "CHARGE",
        "obstacle": "AVOID",
        "destination": "NAVIGATE",
        "task start": "MOVE",
    })

    def __post_init__(self):
        self.current_goal = self.initial_goal

    def decide_next_goal(self, observation_text: str) -> Tuple[str, Dict]:
        """観測テキストから次のゴールを決定する。
        Returns:
            next_goal (str): 次の目標名
            meta (dict): マッチしたキーワードや理由などのメタ情報
        """
        obs_lc = (observation_text or "").lower()
        matched = None
        next_goal = self.current_goal

        for key, goal in self.rules.items():
            if key in obs_lc:
                matched = key
                next_goal = goal
                break  # 最初にマッチしたルールを採用

        changed = (next_goal != self.current_goal)
        if self.verbose:
            print(f"🧠 Observation: {observation_text}")
            if matched:
                print(f"🔎 Matched rule: '{matched}' -> goal='{next_goal}'")
            else:
                print("ℹ️  No rule matched; keeping current goal.")
            if changed:
                print(f"🎯 Goal updated: {self.current_goal} → {next_goal}")
            else:
                print(f"✔️ Goal remains: {self.current_goal}")

        meta = {
            "matched_rule": matched,
            "changed": changed
        }
        self.current_goal = next_goal
        return next_goal, meta


# デモ実行
if __name__ == "__main__":
    agent = GoalReasoningAgent(initial_goal="IDLE", verbose=True)
    observations = [
        "task started, moving toward destination",
        "obstacle detected on path",
        "battery low warning",
        "clear path ahead"
    ]
    for obs in observations:
        goal, meta = agent.decide_next_goal(obs)
        print({"goal": goal, **meta})
