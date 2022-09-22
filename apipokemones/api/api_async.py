import requests


async def get_pokemons_async():
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=10'
    response = requests.get(url)
    if response.ok:
        payload = response.json()
        results = payload.get('results', [])
    return results


async def get_pokemonstype_async(id_tipo):
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


async def get_pokemon_async(id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(id)
    response = requests.get(url)
    results = {}
    if response.ok:
        payload = response.json()
        results = payload
    return results


async def get_imagen_async(url):
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


async def get_idtipo_async(url):
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
