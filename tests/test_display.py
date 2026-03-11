from weather_app.weather_display import display_current_weather


def test_display():

    weather = {
        "city": "London",
        "temperature": 20,
        "humidity": 50,
        "wind_speed": 5,
        "condition": "clear sky"
    }

    display_current_weather(weather)
