import requests


def get_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=1500'
    response = requests.get(url)
    if response.ok:
        payload = response.json()
        results = payload.get('results', [])
    return results


def get_pokemonstype(id_tipo):
    url = 'https://pokeapi.co/api/v2/type/' + str(id_tipo)
    response = requests.get(url)
    results, type = [], ''
    if response.ok:
        payload = response.json()
        results = payload.get('pokemon', [])
        languages = payload.get('names', [])
        for lang in languages:
            if lang.get('language').get('name') == 'en':
                type = lang.get('name')
    return results, type


def get_pokemon(id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(id)
    response = requests.get(url)
    results = {}
    if response.ok:
        payload = response.json()
        results = payload
    return results


def get_imagen(url):
    response = requests.get(url)
    if response.ok:
        response_json = response.json()
        sprite = response_json['sprites']
        id = response_json['id']
        nombre = response_json['name']
        data = {
            'imagen': sprite['front_default'],
            'id': id,
            'nombre': nombre,
        }
        return data


def get_idtipo(url):
    response = requests.get(url)
    if response.ok:
        response_json = response.json()
        id = response_json['id']
        name = response_json['name']
        data = {
            'id': id,
            'name': name,
        }
        return data
