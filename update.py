import json
import os
import subprocess
from datetime import datetime

REPO = "/home/elias/HasTheDayHappend"
os.chdir(REPO)

FILE = "days.json"

# date
today = datetime.now().strftime("%-m/%-d/%Y")

# load file
if os.path.exists(FILE):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except Exception:
        data = {}
else:
    data = {}

# is Empty?
if not isinstance(data, dict):
    data = {}

# check if already exits
if today not in data:
    data[today] = True

    # Save
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

    # Git
    subprocess.run(["git", "add", "days.json"], check=True)
    subprocess.run(["git", "commit", "-m", f"Add {today}"], check=True)
    subprocess.run(["git", "push"], check=True)

    print(f"Added {today}")
else:
    print(f"{today} already exists.")
