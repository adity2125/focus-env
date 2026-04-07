from pydantic import BaseModel

class Observation(BaseModel):
    focus: int
    energy: int
    tasks_left: int
    distraction: bool

class Action(BaseModel):
    action: str

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict