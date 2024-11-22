import os
import json
import requests
from datetime import datetime
from github import Github

API_KEY = "70e0c2020bdf4020b670925f6386df3d"

def fetch_random_meal():
    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    if response.status_code == 200:
        meal_data = response.json()
        return meal_data['meals'][0]['strMeal']
    else:
        return "Error fetching meal"

def fetch_random_name():
    headers = {
        'X-Api-Key': API_KEY
    }
    params = {
        'nameType': 'firstname',  # You can change to 'surname' or 'fullname'
        'quantity': 1
    }
    response = requests.get("https://randommer.io/api/Name", headers=headers, params=params)
    if response.status_code == 200:
        name_data = response.json()
        return name_data[0]  # Extract the first name
    else:
        return "Error fetching name"

def fetch_random_quote():
    # category = 'happiness'  # You can change the category to anything supported by API Ninjas
    api_url = f'https://api.api-ninjas.com/v1/quotes'
    headers = {
        'X-Api-Key': 'l5kBs62MYeitKw5ckfhI8g==edZZbrUUIaMFAPIZ' # i can include the api key for shitty websites right
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == requests.codes.ok:
        quote_data = response.json()
        return quote_data[0]['quote']  # Extract the quote from the API response
    else:
        return f"Error fetching quote: {response.status_code}, {response.text}"

def update_json():
    # Read the existing JSON file
    try:
        with open('todays-overview.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, create a default structure
        data = {
            "name": "if you're seeing this, the workflow is broken.",
            "meal": "please contact gamerselimiko@gmail.com",
            "quote": "No quote available"
        }

    today = datetime.now()

    # Fetch a random meal, name, and quote
    data["meal"] = fetch_random_meal()
    data["name"] = fetch_random_name()  # Fetching name from Randommer API
    data["quote"] = fetch_random_quote()  # Fetch a random quote

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
