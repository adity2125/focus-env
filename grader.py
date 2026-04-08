def grade(state):
    tasks_left = state["tasks_left"]
    total_tasks = state.get("initial_tasks", 5)

    completed = total_tasks - tasks_left

    # normalize score between 0 and 1
    raw_score = completed / total_tasks

    # 🔥 clamp strictly between (0,1)
    if raw_score >= 1.0:
        return 0.99
    elif raw_score <= 0.0:
        return 0.01
    else:
        return round(raw_score, 2)
