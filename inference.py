from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2",
    temperature=0.0,
    top_p=1.0,
    max_new_tokens=50
)

def build_prompt(input_text, difficulty="medium"):
    base = """You are solving a task in an evaluation environment.

Rules:
1. Think step by step internally
2. Be logically consistent
3. If unsure, choose the most reasonable answer
4. Return ONLY the final answer

"""

    if difficulty == "hard":
        examples = """Example:
Q: What is 2+2?
A: 4

Q: If x=3, what is x^2?
A: 9

"""
        return base + examples + f"Q: {input_text}\nA:"

    return base + f"Q: {input_text}\nA:"


def generate_response(prompt):
    try:
        output = generator(prompt)[0]["generated_text"]
        return output.split("A:")[-1].strip()
    except Exception:
        return ""


def self_correct(answer):
    check_prompt = f"""Check if this answer is correct:
{answer}

If incorrect, fix it.
Return ONLY final answer.
"""
    try:
        output = generator(check_prompt)[0]["generated_text"]
        return output.strip()
    except Exception:
        return answer


def predict(input_text, difficulty="medium"):
    prompt = build_prompt(input_text, difficulty)

    response1 = generate_response(prompt)
    response2 = self_correct(response1)

    final_answer = response2.strip()

    if not final_answer:
        final_answer = generate_response(prompt)

    return {
        "answer": final_answer.strip()
    }
