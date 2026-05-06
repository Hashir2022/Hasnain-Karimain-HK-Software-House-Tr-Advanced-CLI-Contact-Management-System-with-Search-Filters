import json
from datetime import datetime

def save_history(email, subject, status):
    record = {
        "email": email,
        "subject": subject,
        "status": status,
        "time": str(datetime.now())
    }

    try:
        with open("history.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(record)

    with open("history.json", "w") as f:
        json.dump(data, f, indent=4)