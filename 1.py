import requests


def geocode_coords(geocode):
    server_address = 'http://geocode-maps.yandex.ru/1.x/?'
    api_key = '8013b162-6b42-4997-9691-77b7074026e0'
    geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode}&format=json'
    response = requests.get(geocoder_request)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    envelope = toponym['boundedBy']['Envelope']
    l, d = envelope['lowerCorner'].split()
    r, t = envelope['upperCorner'].split()
    dx = abs(float(r) - float(l)) / 2
    dy = abs(float(t) - float(d)) / 2
    span = f'{dx},{dy}'
    return toponym_coodrinates, span
