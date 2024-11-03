import requests

def get_public_ip():
    response = requests.get('https://ident.me')
    if response.status_code == 200:
        return response.text
    else:
        return None

public_ip = get_public_ip()
if public_ip:
    print(f"Your public IP address is: {public_ip}")
else:
    print("Failed to retrieve public IP address.")