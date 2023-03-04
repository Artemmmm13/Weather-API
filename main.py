# Artem Fedorchenko
import requests
from requests.exceptions import HTTPError
from datetime import date


def get_weather_forecast():
    # separate variable to contain api key
    request_url = "http://api.openweathermap.org/data/2.5/weather?" \
                "q=London,uk&APPID=a85832b37caead62d04c4c7c701e6428"

    """In this block of code i cited code introduced during lecture to handle error
    that might be generated during response process"""

    try:
        response = requests.get(request_url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

        """in this block of code i convert JSON into dict and then i parse it 
        and output information which i need using f-string"""
    else:
        r_dict = dict(response.json())
        today = date.today()
        print(f"Weather forecast for the city of {r_dict['name']}\n")
        print(f'Today is {today}')
        print(f"Weather description: {r_dict['weather'][0]['description']}")
        print(f"Humidity: {r_dict['main']['humidity']}")
        print(f"Temperature (in Celsius): {int(r_dict['main']['temp']) - 273.15}")
        print(f"Wind speed: {r_dict['wind']['speed']} m/s")
        print(f"Max temperature (in Celsius): {int(r_dict['main']['temp_max']) - 273.15}")
        print(f"Min temperature (in Celsius): {int(r_dict['main']['temp_min']) - 273.15}")


if __name__ == '__main__':
    get_weather_forecast()
