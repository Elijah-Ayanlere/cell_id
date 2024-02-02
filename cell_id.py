import requests
import os

def get_cell_tower_info():
    # Provide cell tower information manually for your laptop
    cell_id = 12345  # Replace with your cell ID
    lac = 67890  # Replace with your location area code

    # Get API key from environment variable
    api_key = os.getenv("UNWIREDLABS_API_KEY")

    if not api_key:
        print("API key is missing. Please set UNWIREDLABS_API_KEY environment variable.")
        return

    api_url = "https://us1.unwiredlabs.com/v2/process.php"

    # Prepare payload for the API request
    payload = {
        "token": api_key,
        "radio": "gsm",
        "mcc": 310,
        "mnc": 404,
        "cells": [{
            "lac": lac,
            "cid": cell_id
        }],
        "wifi": []
    }

    try:
        # Make the API request
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        
        # Parse the JSON response
        data = response.json()

        if "status" in data and data["status"] == "ok":
            if "lat" in data and "lon" in data:
                latitude = data["lat"]
                longitude = data["lon"]
                print(f"Location: {latitude}, {longitude}")
            else:
                print("Location data not available.")
        else:
            print("Failed to track the device.")
    except requests.RequestException as e:
        print(f"Error making API request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Manually set cell tower information for the laptop
get_cell_tower_info()
