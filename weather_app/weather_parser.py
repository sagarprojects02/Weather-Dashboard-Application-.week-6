from datetime import datetime


def parse_current_weather(data):

    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "condition": data["weather"][0]["description"]
    }

    return weather


def parse_forecast(data):

    forecast_list = []

    for item in data["list"][:5]:

        forecast = {
            "date": datetime.fromtimestamp(item["dt"]).strftime("%Y-%m-%d %H:%M"),
            "temperature": item["main"]["temp"],
            "condition": item["weather"][0]["description"]
        }

        forecast_list.append(forecast)

    return forecast_list


def celsius_to_fahrenheit(temp):

    return (temp * 9/5) + 32
