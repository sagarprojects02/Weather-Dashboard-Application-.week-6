import requests
import json
import os
from .config import API_KEY, BASE_URL, CACHE_DIR


def get_current_weather(city):

    url = f"{BASE_URL}/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_forecast(city):

    url = f"{BASE_URL}/forecast"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def cache_weather(city, data):

    os.makedirs(CACHE_DIR, exist_ok=True)

    file_path = f"{CACHE_DIR}/{city}.json"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def load_cached_weather(city):

    file_path = f"{CACHE_DIR}/{city}.json"

    if os.path.exists(file_path):

        with open(file_path) as f:
            return json.load(f)

    return None
