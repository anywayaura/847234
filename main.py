import requests


places = ['London', 'Аэропорт Шереметьево', 'Череповец']

def get_weather(place):
    params = {'nTqum':'', 'lang': 'ru'}
    result = requests.get(f'https://wttr.in/{place}', params=params)
    result.raise_for_status()
    return result.text


if __name__ == '__main__':
    for place in places:
        print(get_weather(place))
