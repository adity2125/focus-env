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

    while not done:
        action = agent.choose_action(obs)
        result = env.step(action)

        obs = result.observation
        total_reward += result.reward
        done = result.done

    score = grade(env.state())

    return total_reward, score


def main():
    for task in TASKS:
        reward, score = run_task(task)
        print(f"{task['name']} → Reward: {reward}, Score: {score}")


if __name__ == "__main__":
    main()
