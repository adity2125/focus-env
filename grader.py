def grade(state):
    total = state["tasks_left"]

    if total == 0:
        return 1.0
    elif total == 1:
        return 0.8
    elif total == 2:
        return 0.6
    elif total == 3:
        return 0.4
    elif total == 4:
        return 0.2
    else:
        return 0.0