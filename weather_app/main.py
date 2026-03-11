from weather_app.weather_api import get_current_weather, get_forecast
from weather_app.weather_parser import parse_current_weather, parse_forecast
from weather_app.weather_display import display_current_weather, display_forecast


def menu():

    print("\nWeather Dashboard")
    print("1. Current Weather")
    print("2. 5 Day Forecast")
    print("3. Exit")


def main():

    while True:

        menu()

        choice = input("Enter choice: ")

        if choice == "1":

            city = input("Enter city: ")

            data = get_current_weather(city)

            weather = parse_current_weather(data)

            display_current_weather(weather)

        elif choice == "2":

            city = input("Enter city: ")

            data = get_forecast(city)

            forecast = parse_forecast(data)

            display_forecast(forecast)

        elif choice == "3":

            break


if __name__ == "__main__":
    main()
