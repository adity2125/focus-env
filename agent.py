import os
from openai import OpenAI

class Agent:
    def __init__(self):
        self.client = OpenAI(
            base_url=os.environ["API_BASE_URL"],
            api_key=os.environ["API_KEY"]
        )

    def choose_action(self, observation):
        prompt = f"""
You are an AI student assistant.

Observation:
Focus: {observation.focus}
Energy: {observation.energy}
Tasks left: {observation.tasks_left}
Distraction: {observation.distraction}

Choose ONE action from:
STUDY, BREAK, SCROLL, IGNORE

Only return the action.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        action_text = response.choices[0].message.content.strip()

        return type("Action", (), {"action": action_text})
