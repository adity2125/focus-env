from fastapi import FastAPI
from env import FocusEnv
from agent import Agent
from tasks import TASKS
from grader import grade

app = FastAPI()

@app.get("/")
def run_env():
    results = []

    for task in TASKS:
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

        results.append({
            "task": task["name"],
            "reward": total_reward,
            "score": score
        })

    return {"results": results}
