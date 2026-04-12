from utils import clean_text

def grade(prediction, ground_truth):
    pred = clean_text(prediction.get("answer", ""))
    gt = clean_text(ground_truth)

    if pred == gt:
        return 1.0
    return 0.0
