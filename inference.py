from env import FocusEnv
from agent import Agent
from tasks import TASKS
from grader import grade


def run_task(task):
    env = FocusEnv(tasks=task["tasks"])
    env.max_steps = task["max_steps"]

    agent = Agent()
    obs = env.reset()

    done = False
    total_reward = 0
    step_count = 0

    # 🔥 START block
    print(f"[START] task={task['name']}", flush=True)

    while not done:
        step_count += 1

        action = agent.choose_action(obs)
        result = env.step(action)

        obs = result.observation
        total_reward += result.reward
        done = result.done

        # 🔥 STEP block
        print(f"[STEP] step={step_count} reward={result.reward}", flush=True)

    score = grade(env.state())

    # 🔥 END block
    print(
        f"[END] task={task['name']} score={score} steps={step_count}",
        flush=True
    )


def main():
    for task in TASKS:
        run_task(task)


if __name__ == "__main__":
    main()
