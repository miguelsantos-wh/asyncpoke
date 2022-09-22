async def get_pokemons_async_aio(session):
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=10'
    async with session.get(url) as resp:
        response = await resp.json()
        results = response.get('results', [])
        return results


async def get_pokemonstype_async_aio(session, id_tipo):
    url = 'https://pokeapi.co/api/v2/type/' + str(id_tipo)
    async with session.get(url) as resp:
        response = await resp.json()
        results = response.get('pokemon', [])
        languages = response.get('names', [])
        for lang in languages:
            if lang.get('language').get('name') == 'en':
                type = lang.get('name')
        return results, type


async def get_pokemon_async_aio(session, id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(id)
    async with session.get(url) as resp:
        results = await resp.json()
        return results


async def get_imagen_async_aio(session, url):
    async with session.get(url) as resp:
        response_json = await resp.json()
        sprite = response_json['sprites']
        id = response_json['id']
        nombre = response_json['name']
        data = {
            'imagen': sprite['front_default'],
            'id': id,
            'nombre': nombre,
        }
        return data


async def get_idtipo_async_aio(session, url):
    async with session.get(url) as resp:
        response_json = await resp.json()
        id = response_json.get('id')
        name = response_json.get('name')
        data = {
            'id': id,
            'name': name,
        }
        return data