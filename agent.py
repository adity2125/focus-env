from models import Action

class Agent:
    def choose_action(self, state):
        if state.distraction:
            return Action(action="IGNORE")
        elif state.energy < 30:
            return Action(action="BREAK")
        elif state.focus > 60:
            return Action(action="STUDY")
        else:
            return Action(action="SCROLL")