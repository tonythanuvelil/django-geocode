import requests

api_key = 'GDUGY0M2zbkHztqgYGdbxcoG4oknynpG'


def get_location_detail(lat, long):
    url = f'http://www.mapquestapi.com/geocoding/v1/reverse?key={api_key}&location={lat},{long}'
    r = requests.get(url)
    data = r.json()
    return data['results'][0]['locations'][0]
