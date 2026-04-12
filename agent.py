from inference import predict

class Agent:
    def __init__(self):
        pass

    def act(self, observation):
        input_text = observation.get("input", "")
        difficulty = observation.get("difficulty", "medium")

        result = predict(input_text, difficulty)

        return result
