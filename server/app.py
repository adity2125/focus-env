from fastapi import FastAPI
from env import FocusEnv

app = FastAPI()

env = None

def main():
    return app


@app.post("/reset")
def reset():
    global env
    env = FocusEnv(tasks=3)
    return env.reset().dict()


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


# 🔥 THIS IS THE MISSING PART
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)
