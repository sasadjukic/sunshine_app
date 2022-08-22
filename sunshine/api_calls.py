
import requests
from sunshine import KEY, MONTHS, DAYS
from datetime import datetime

def info_home(home_location, temp) -> tuple:
    find_home = requests.get(f'http://api.weatherapi.com/v1/current.json?key={KEY}&q={home_location}&aqi=no')
    data_home = find_home.json()

    home_time = data_home['location']['localtime'].split()[1]
    home_raw_month = data_home['location']['localtime'].split()[0][5:7]
    home_month = MONTHS[home_raw_month]
    home_day = data_home['location']['localtime'].split()[0][8:]
    home_icon = data_home['current']['condition']['icon']
    home_temp = round(data_home['current'][temp])

    return (home_location, home_time, home_month, home_day, home_icon, home_temp)

def info_city_one(city_one, temp) -> tuple:
    find_city_one = requests.get(f'http://api.weatherapi.com/v1/current.json?key={KEY}&q={city_one}&aqi=no')
    data_city_one = find_city_one.json()

    city_one_icon = data_city_one['current']['condition']['icon']
    city_one_temp = round(data_city_one['current'][temp])

    return (city_one, city_one_icon, city_one_temp)

def info_city_two(city_two, temp) -> tuple:
    find_city_two = requests.get(f'http://api.weatherapi.com/v1/current.json?key={KEY}&q={city_two}&aqi=no')
    data_city_two = find_city_two.json()

    city_two_icon = data_city_two['current']['condition']['icon']
    city_two_temp = round(data_city_two['current'][temp])

    return (city_two, city_two_icon, city_two_temp)

def info_city_three(city_three, temp) -> tuple:
    find_city_three = requests.get(f'http://api.weatherapi.com/v1/current.json?key={KEY}&q={city_three}&aqi=no')
    data_city_three = find_city_three.json()

    city_three_icon = data_city_three['current']['condition']['icon']
    city_three_temp = round(data_city_three['current'][temp])

    return (city_three, city_three_icon, city_three_temp)

def three_day_info(search, temp) -> tuple:

    find = requests.get(f'http://api.weatherapi.com/v1/current.json?key={KEY}&q={search}&aqi=no')
    new_data = find.json()
    new_location = new_data['location']['name']
    local_time = new_data['location']['localtime'].split()[1]
    local_raw_month = new_data['location']['localtime'].split()[0][5:7]
    local_month = MONTHS[local_raw_month]
    local_day = new_data['location']['localtime'].split()[0][8:]
    local_icon = new_data['current']['condition']['icon']
    local_temp = round(new_data['current'][temp])
    wind = new_data['current']['wind_mph']
    pressure = new_data['current']['pressure_mb']
    humidity = new_data['current']['humidity']

    return (new_location, local_time, local_month, local_day, 
            local_icon, local_temp, wind, pressure, humidity)

def three_day_forecast(search, maxtemp, mintemp) -> tuple:

    weekly = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={KEY}&q={search}&days=6&aqi=no&alerts=no')
    weekly_data = weekly.json()
    d_one_forecast = weekly_data['forecast']['forecastday'][0]['day']['condition']['icon']
    d_one_high = round(weekly_data['forecast']['forecastday'][0]['day'][maxtemp])
    d_one_low = round(weekly_data['forecast']['forecastday'][0]['day'][mintemp])
    d_two_forecast = weekly_data['forecast']['forecastday'][1]['day']['condition']['icon']
    d_two_high = round(weekly_data['forecast']['forecastday'][1]['day'][maxtemp])
    d_two_low = round(weekly_data['forecast']['forecastday'][1]['day'][mintemp])
    d_three_forecast = weekly_data['forecast']['forecastday'][2]['day']['condition']['icon']
    d_three_high = round(weekly_data['forecast']['forecastday'][2]['day'][maxtemp])
    d_three_low = round(weekly_data['forecast']['forecastday'][2]['day'][mintemp])

    return (d_one_forecast, d_one_high, d_one_low, d_two_forecast, d_two_high, 
            d_two_low, d_three_forecast, d_three_high, d_three_low)


def sort_calendar() -> tuple:
    today = datetime.now().weekday()
    tomorrow = datetime.now().weekday() + 1
    if tomorrow > 6:
        tomorrow = tomorrow - 7
    after_tomorrow = datetime.now().weekday() + 2
    if after_tomorrow > 6:
        after_tomorrow = after_tomorrow - 7
    find_today = DAYS[today]
    find_tomorrow = DAYS[tomorrow]
    find_after_tomorrow = DAYS[after_tomorrow]

    return (find_today, find_tomorrow, find_after_tomorrow)

