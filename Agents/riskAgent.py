def detect_risk(clause: str, text: str):
    text = text.lower()

    if clause == "Data Sharing" and "may" in text:
        return "High"

    if clause == "Arbitration":
        return "High"

    if clause == "Auto Renewal":
        return "Medium"

    return "Low"
