"""
Module for getting weather info.
"""

import requests


def get_weather(city):
    """
    Get current weather info of given city.

    :param city: Location -- name of the city
    :return: Info about temperature and weather in the city
    """
    url = "http://api.openweathermap.org/data/2.5/weather"

    querystring = {
        "q": city,
        "appid": "b4a9d8e16b916107e741f1e84440c660"
    }

    response = requests.get(url, params=querystring)

    data = response.json()
    if response.text == '[]':
        raise Exception("Can't find given location!")
    else:
        return "Temperature is {} and {} in {}".format(data['main']['temp'], data['weather'][0]['description'], city)


def get_5_weather(city):
    """
    Get weather info for 5 days of given city.

    :param city: Location -- name of the city
    :return: Info about temperature and weather in the city
    """
    url = "http://api.openweathermap.org/data/2.5/forecast"

    querystring = {
        "q": city,
        "appid": "b4a9d8e16b916107e741f1e84440c660"
    }

    response = requests.get(url, params=querystring)
    data = response.json()

    if response.text == '[]':
        raise Exception("Can't find given location!")
    else:
        for d in data['list']:
            print(d['dt'])
            print(d['main']['temp'])
            print(d['weather'][0]['main'])


def get_coordinates(address):
    """
    Get coordinates(latitude and longitude) of given address.

    :param address: Address of location.
    :return: List with latitude and longitude.
    """
    url = "https://nominatim.openstreetmap.org/search"
    querystring = {"q": address,
                   "format": "json"
                   }
    coordinates_response = requests.get(url, params=querystring)
    if coordinates_response.text == '[]':
        raise Exception('There is no such address!')
    else:
        return [coordinates_response.json()[0]['lat'], coordinates_response.json()[0]['lon']]


def get_weather_by_coordinates(latitude, longitude):
    """
    Get weather information by coordinates.

    :param latitude: Latitude of the location
    :param longitude: Longitude of the location
    :return: Temperature and weather info
    """
    url = "http://api.openweathermap.org/data/2.5/weather"

    querystring = {
        "lat": latitude,
        "lon": longitude,
        "appid": "b4a9d8e16b916107e741f1e84440c660",
        "units": "metric"
    }

    response = requests.get(url, params=querystring)

    data = response.json()
    return data


def get_5days_weather_by_coordinates(latitude, longitude):
    """
    Get weather information for 5 days by coordinates.

    :param latitude: Latitude of the location
    :param longitude: Longitude of the location
    :return: Temperature and weather info for 5 days
    """
    url = "http://api.openweathermap.org/data/2.5/forecast"

    querystring = {
        "lat": latitude,
        "lon": longitude,
        "appid": "b4a9d8e16b916107e741f1e84440c660",
        "units": "metric"
    }

    response = requests.get(url, params=querystring)
    data = response.json()
    return data


if __name__ == '__main__':
    c = get_coordinates('Russia, Saint-Petersburg, Nevsky prospect, 22')
    get_5days_weather_by_coordinates(c[0], c[1])
