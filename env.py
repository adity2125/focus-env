import random
from models import Observation, StepResult


class FocusEnv:
    def __init__(self, tasks=3):
        self.initial_tasks = tasks
        self.reset()

    def reset(self):
        self.focus = 70
        self.energy = 60
        self.tasks_left = self.initial_tasks
        self.step_count = 0
        self.max_steps = 15
        self.distraction = False

        return self._get_obs()

    def _get_obs(self):
        return Observation(
            focus=self.focus,
            energy=self.energy,
            tasks_left=self.tasks_left,
            distraction=self.distraction
        )

    def state(self):
        return {
            "step_count": self.step_count,
            "tasks_left": self.tasks_left,
            "focus": self.focus,
            "energy": self.energy
        }

    def step(self, action):
        self.step_count += 1

        
        self.distraction = random.random() < 0.4

        reward = 0

        # Step penalty
        reward -= 2

        # STUDY
        if action.action == "STUDY":
            if random.random() < 0.3:
                reward -= 5  # wasted effort
            else:
                if self.energy < 20:
                    reward -= 10
                elif self.focus < 30:
                    reward -= 6
                else:
                    self.energy -= 12
                    self.tasks_left -= 1
                    reward += 8

        # SCROLL
        elif action.action == "SCROLL":
            self.focus -= 25
            self.energy -= 8
            reward -= 15

        # BREAK
        elif action.action == "BREAK":
            self.energy += 8
            self.focus += 2
            reward += 1

        # IGNORE
        elif action.action == "IGNORE":
            if self.distraction:
                self.focus += 5
                reward += 4
            else:
                reward -= 5

        # Random fatigue
        if random.random() < 0.2:
            self.energy -= 5

        #  Penalties
        if self.energy < 15:
            reward -= 6

        if self.focus < 20:
            reward -= 6

        # Clamp
        self.focus = max(0, min(100, self.focus))
        self.energy = max(0, min(100, self.energy))

        done = self.tasks_left <= 0 or self.step_count >= self.max_steps

        # Bonus
        if done and self.tasks_left == 0:
            reward += 3

        return StepResult(
            observation=self._get_obs(),
            reward=reward,
            done=done,
            info={"step": self.step_count}
        )