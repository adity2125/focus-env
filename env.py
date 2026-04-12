class Env:
    def __init__(self):
        pass

    def reset(self):
        return {"input": "What is 2+2?", "difficulty": "easy"}

    def step(self, action):
        return {}, 1.0, True, {}
