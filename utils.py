def clean_text(text):
    return str(text).strip().lower()


def safe_compare(pred, gt):
    return clean_text(pred) == clean_text(gt)
