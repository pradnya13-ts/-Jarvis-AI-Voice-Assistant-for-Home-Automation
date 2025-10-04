import json
from datetime import datetime
import os

SCHEDULE_FILE = "Data/schedule.json"

# ✅ Ensure the file exists and has valid JSON
if not os.path.exists(SCHEDULE_FILE) or os.path.getsize(SCHEDULE_FILE) == 0:
    with open(SCHEDULE_FILE, "w") as f:
        json.dump({}, f)


def add_schedule(task):
    today = datetime.now().strftime("%Y-%m-%d")
    with open(SCHEDULE_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    if today not in data:
        data[today] = []

    formatted_task = f"you have to {task.lower().strip()}"
    data[today].append(formatted_task)

    with open(SCHEDULE_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return f"✅ Added: {formatted_task}"


def get_today_schedule():
    today = datetime.now().strftime("%Y-%m-%d")
    with open(SCHEDULE_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return "🗓️ You have nothing scheduled for today."

    tasks = data.get(today, [])
    if not tasks:
        return "🗓️ You have nothing scheduled for today."

    response = "📋 As per your schedule, "
    if len(tasks) == 1:
        response += tasks[0] + "."
    else:
        response += ", ".join(tasks[:-1]) + ", and " + tasks[-1] + "."
    return response


