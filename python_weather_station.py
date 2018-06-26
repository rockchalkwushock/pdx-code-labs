import requests


def get_weather(loc, units):
    params = {
        "APPID": 'a8f99f131280a03b5f5f76c9644fc956',
    }
    # Check if by city or by zip.
    if type(loc) == 'int':
        params['zip'] = loc
    else:
        params['q'] = loc
    # Check if by imperial or by metric.
    if units == '1':
        params['units'] = 'imperial'
    elif units == '2':
        params['units'] = 'metric'
    # Make request.
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather', params=params)
    # Parse from JSON to Python dictonary.
    res = r.json()
    # Get data.
    temp = res['main']['temp']
    hum = res['main']['temp']
    # Display based on chosen units.
    if units == '1':
        print(
            f'Current weather for {loc}:\n\tTemp: {round(temp)}F\n\tHumidity: {round(hum)}%')
    elif units == '2':
        print(
            f'Current weather for {loc}:\n\tTemp: {round(temp)}C\n\tHumidity: {round(hum)}%')


while True:
    query = input('1. By City\n2. By Zipcode\n3. Quit\n\n')
    if query == '1':
        loc = input('Enter a City: ')
        u = input('1. Imperial\n2. Metric\n\n')
        get_weather(loc, u)
    elif query == '2':
        loc = int(input('Enter Zipcode: '))
        u = input('1. Imperial\n2. Metric\n\n')
        get_weather(loc, u)
    elif query == '3':
        quit()
    else:
        print('Please enter one of the options.')
        continue
