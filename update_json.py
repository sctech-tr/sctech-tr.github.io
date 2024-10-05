import os
import json
import requests
from datetime import datetime
from github import Github

def fetch_random_meal():
    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    if response.status_code == 200:
        meal_data = response.json()
        return meal_data['meals'][0]['strMeal']
    else:
        return "Error fetching meal"

def fetch_random_name():
    response = requests.get("https://randomuser.me/api")
    if response.status_code == 200:
        user_data = response.json()
        return user_data['results'][0]['name']['first']  # Correctly extracting the first name
    else:
        return "Error fetching name"

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

    # Fetch a random meal and name
    data["meal"] = fetch_random_meal()
    data["name"] = fetch_random_name()  # Fetching only the first name

    # Update only the date and day
    data["date"] = today.strftime("%Y-%m-%d")
    data["day"] = today.strftime("%A")

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
