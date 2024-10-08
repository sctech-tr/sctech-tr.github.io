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

def fetch_random_quote():
<<<<<<< Updated upstream
    try:
        response = requests.get("https://en.wikiquote.org/w/api.php?action=query&format=json&list=random&rnlimit=1&rnnamespace=0")
        if response.status_code == 200:
            random_page = response.json()['query']['random'][0]
            page_id = random_page['id']

            # Fetch the quote from the specific Wikiquote page
            quote_response = requests.get(f"https://en.wikiquote.org/w/api.php?action=parse&pageid={page_id}&prop=text&format=json")
            if quote_response.status_code == 200:
                parsed_page = quote_response.json()
                # Extracting the first quote (This may need more parsing based on HTML)
                return parsed_page['parse']['text']['*']
            else:
                return "Error fetching quote"
        else:
            return "Error fetching random Wikiquote page"
    except Exception as e:
        return f"Exception occurred: {e}"
=======
    # category = 'happiness'  # You can change the category to anything supported by API Ninjas
    api_url = f'https://api.api-ninjas.com/v1/quotes'
    headers = {
        'X-Api-Key': 'l5kBs62MYeitKw5ckfhI8g==edZZbrUUIaMFAPIZ'
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == requests.codes.ok:
        quote_data = response.json()
        return quote_data[0]['quote']  # Extract the quote from the API response
    else:
        return f"Error fetching quote: {response.status_code}, {response.text}"
>>>>>>> Stashed changes

def update_json():
    # Read the existing JSON file
    try:
        with open('todays-overview.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, create a default structure
        data = {
            "name": "if you're seeing this, the workflow is broken.",
            "meal": "please contact sctech@national.shitposting.agency",
            "quote": "No quote available"
        }

    today = datetime.now()

    # Fetch a random meal, name, and quote
    data["meal"] = fetch_random_meal()
    data["name"] = fetch_random_name()  # Fetching only the first name
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
