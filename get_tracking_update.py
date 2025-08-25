import requests
from gettoken import get_oauth_token
import json


def tracking_update(trackingnum, client_id, client_secret): #remove tracking number and add in variable
    version = "v2403"
    url = f"https://wwwcie.ups.com/api/track/v1/details/{trackingnum}" # move to production
    
    payload = {
        "trackingNumber": [trackingnum]  # UPS expects an array, even if it's one number
    }

    headers = {
        "Authorization": f"Bearer {get_oauth_token(client_id, client_secret)}",
        "Content-Type": "application/json",
        "transId": "testing",
        "transactionSrc": "testing"
    }

    response = requests.get(url, headers=headers, json=payload)
    if response.status_code != 200:
        data = {
            "error": f"UPS API error: {response.status_code} - {response.text}"
        }
    else:
        data = response.json()
        return data["trackResponse"]["shipment"][0]["package"][0]["activity"][3]["status"]["description"] #get rid of 2 or just get whole json data and troubleshoot from there









