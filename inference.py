from env import FocusEnv
from agent import Agent
from tasks import TASKS
from grader import grade


def run_task(task):
    try:
        env = FocusEnv(tasks=task["tasks"])
        env.max_steps = task["max_steps"]

        agent = Agent()
        obs = env.reset()

        done = False
        total_reward = 0
        step_count = 0

        # ✅ START block (required)
        print(f"[START] task={task['name']}", flush=True)

        while not done:
            step_count += 1

            try:
                action = agent.choose_action(obs)
            except Exception as e:
                # 🔥 fallback if agent fails
                print(f"[ERROR] agent failed: {e}", flush=True)
                action = type("Action", (), {"action": "BREAK"})

            try:
                result = env.step(action)
            except Exception as e:
                # 🔥 fallback if env fails
                print(f"[ERROR] env step failed: {e}", flush=True)
                break

            obs = result.observation
            total_reward += result.reward
            done = result.done

            # ✅ STEP block (required)
            print(
                f"[STEP] step={step_count} reward={result.reward}",
                flush=True
            )

        try:
            score = grade(env.state())
        except Exception as e:
            print(f"[ERROR] grading failed: {e}", flush=True)
            score = 0.0

        # ✅ END block (required)
        print(
            f"[END] task={task['name']} score={score} steps={step_count}",
            flush=True
        )

    except Exception as e:
        # 🔥 NEVER crash whole script
        print(f"[FATAL] task {task['name']} failed: {e}", flush=True)


def main():
    for task in TASKS:
        run_task(task)


if __name__ == "__main__":
    main()
