from weather_app.weather_parser import celsius_to_fahrenheit


def test_temperature_conversion():

    result = celsius_to_fahrenheit(0)

    assert result == 32
