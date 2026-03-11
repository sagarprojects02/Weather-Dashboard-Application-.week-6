from weather_app.weather_api import get_current_weather


def test_api_response():

    city = "London"

    data = get_current_weather(city)

    assert "main" in data
