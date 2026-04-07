from fastapi import FastAPI
from env import FocusEnv
from agent import Agent
from tasks import TASKS
from grader import grade

app = FastAPI()

env = None

@app.post("/reset")
def reset():
    global env
    env = FocusEnv(tasks=3)
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: dict):
    global env
    result = env.step(type("Action", (), action))
    return {
        "observation": result.observation.dict(),
        "reward": result.reward,
        "done": result.done,
        "info": result.info
    }

@app.get("/state")
def state():
    return env.state()
