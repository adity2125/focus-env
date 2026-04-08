import os
from openai import OpenAI

class Agent:
    def __init__(self):
        self.client = OpenAI(
            base_url=os.environ.get("API_BASE_URL"),
            api_key=os.environ.get("API_KEY")
        )

    def choose_action(self, observation):
        try:
            prompt = f"""
Focus: {observation.focus}
Energy: {observation.energy}
Tasks left: {observation.tasks_left}
Distraction: {observation.distraction}

Choose ONE: STUDY, BREAK, SCROLL, IGNORE
Only return the word.
"""

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                timeout=5  # 🔥 prevent hanging
            )

            action = response.choices[0].message.content.strip()

            if action not in ["STUDY", "BREAK", "SCROLL", "IGNORE"]:
                action = "BREAK"

        except Exception:
            # 🔥 FALLBACK (VERY IMPORTANT)
            if observation.energy < 30:
                action = "BREAK"
            elif observation.distraction:
                action = "IGNORE"
            elif observation.focus > 50:
                action = "STUDY"
            else:
                action = "BREAK"

        return type("Action", (), {"action": action})
