import requests


def get_weather(place):
    result = requests.get(f'https://wttr.in/{place}?nTqum&lang=ru')
    return result.text


if __name__ == '__main__':
    print(get_weather('London'))
    print(get_weather('Аэропорт Шеремеьтево'))
    print(get_weather('Череповец'))
