class GoalReasoningAgent:
    def __init__(self, initial_goal="IDLE"):
        self.current_goal = initial_goal

    def decide_next_goal(self, observation_text):
        print(f"🧠 Observation: {observation_text}")
        # LLMの模擬推論（キーワードに応じて目標を切り替える）
        if "battery low" in observation_text:
            next_goal = "CHARGE"
        elif "obstacle" in observation_text:
            next_goal = "AVOID"
        elif "destination" in observation_text:
            next_goal = "NAVIGATE"
        else:
            next_goal = self.current_goal  # 変更なし

        if next_goal != self.current_goal:
            print(f"🎯 Goal updated: {self.current_goal} → {next_goal}")
            self.current_goal = next_goal
        else:
            print(f"✔️ Goal remains: {self.current_goal}")
        return self.current_goal

# デモ実行
if __name__ == "__main__":
    agent = GoalReasoningAgent("IDLE")
    observations = [
        "task started, moving toward destination",
        "obstacle detected on path",
        "battery low warning",
        "clear path ahead"
    ]

    for obs in observations:
        goal = agent.decide_next_goal(obs)
