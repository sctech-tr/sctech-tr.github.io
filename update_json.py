import os
import json
from datetime import datetime
from github import Github

def update_json():
    # Read the existing JSON file
    try:
        with open('todays-overview.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, create a default structure
        data = {
            "name": "if you're seeing this, the workflow is broken.",
            "meal": "please contact sctech@national.shitposting.agency"
        }

    today = datetime.now()

    # Update only the date, day, and special_message
    data["date"] = today.strftime("%Y-%m-%d")
    data["day"] = today.strftime("%A")

    # Add Pride Month message in June
    if today.month == 6:
        data["special_message"] = "Happy Pride Month!"
    else:
        data["special_message"] = ""

    return data

# Update the JSON file
new_data = update_json()
with open('todays-overview.json', 'w') as f:
    json.dump(new_data, f, indent=2)

# Commit and push the changes
g = Github(os.environ['GITHUB_TOKEN'])
repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
contents = repo.get_contents("todays-overview.json")
repo.update_file(
    contents.path,
    f"Update overview for {new_data['date']}",
    json.dumps(new_data, indent=2),
    contents.sha
)
