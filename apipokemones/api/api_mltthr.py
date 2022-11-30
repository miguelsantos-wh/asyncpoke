def get_pokemons_mltthr(session):
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=2000'
    with session.get(url) as response:
        return response.json()['results']


def get_pokemonstype_mltthr(session, id_tipo):
    url = 'https://pokeapi.co/api/v2/type/' + str(id_tipo)
    with session.get(url) as resp:
        response = resp.json()
        results = response.get('pokemon', [])
        languages = response.get('names', [])
        for lang in languages:
            if lang.get('language').get('name') == 'en':
                type = lang.get('name')
        return results, type


def get_pokemon_mltthr(session, id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(id)
    with session.get(url) as resp:
        results = resp.json()
        return results


def get_imagen_mltthr(session, url):
    with session.get(url) as resp:
        response_json = resp.json()
        sprite = response_json['sprites']
        id = response_json['id']
        nombre = response_json['name']
        data = {
            'imagen': sprite['front_default'],
            'id': id,
            'nombre': nombre,
        }
        return data


def get_idtipo_mltthr(session, url):
    with session.get(url) as resp:
        response_json = resp.json()
        id = response_json.get('id')
        name = response_json.get('name')
        data = {
            'id': id,
            'name': name,
        }
        return data