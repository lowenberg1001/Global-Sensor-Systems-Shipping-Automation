
import os
import base64
import requests

def get_oauth_token():

    client_id = 'Your_Client_ID'
    client_secret = 'Your_Client_Secret'

    url = "https://wwwcie.ups.com/security/v1/oauth/token"
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {b64_auth_str}"
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Failed to get token:", response.text)
        return None


