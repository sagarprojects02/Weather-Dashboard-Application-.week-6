def display_current_weather(weather):

    print("\nCurrent Weather")
    print("-------------------")
    print("City:", weather["city"])
    print("Temperature:", weather["temperature"], "°C")
    print("Humidity:", weather["humidity"], "%")
    print("Wind Speed:", weather["wind_speed"], "m/s")
    print("Condition:", weather["condition"])


def display_forecast(forecast):

    print("\nWeather Forecast")
    print("-------------------")

    for day in forecast:

        print(day["date"])
        print("Temp:", day["temperature"], "°C")
        print("Condition:", day["condition"])
        print("-------------------")
