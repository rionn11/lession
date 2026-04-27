import requests


def geocode_coords(geocode):
    server_address = 'zxc'
    api_key = 'zxc'
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
