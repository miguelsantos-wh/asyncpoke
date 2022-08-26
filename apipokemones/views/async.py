import asyncio
import time
import aiohttp

from django.shortcuts import render, reverse

from apipokemones.api.api_async import get_imagen_async, get_pokemons_async, get_pokemon_async, get_idtipo_async, \
    get_pokemonstype_async


async def pokemon_list_async(request):
    inicio_tiempo = time.time()
    contexto = await get_pokemons_async()
    id = 0
    contexto2 = {}
    for pokemon in contexto:
        id += 1
        imagen = await get_imagen_async(pokemon['url'])
        contexto2[id] = {
            'id': imagen.get('id'),
            'nombre': pokemon['name'],
            'url': pokemon['url'],
            'imagen': imagen.get('imagen'),
        }
    cantidad = len(contexto2)
    tiempo_carga = time.time() - inicio_tiempo
    tiempo_carga = "{0:.2f} Seg.".format(tiempo_carga)
    return render(request, 'pokemones/pokemon_list.html', {
        'pokemones': contexto2,
        'tiempo_carga': tiempo_carga,
        'detail_url': 'pokemon_detallefuncion_async',
        'cantidad': cantidad,
        'titulo': 'LISTA DE POKEMONES AYNC'
    })


async def pokemon_detail_async(request, id_pokemon):
    inicio_tiempo = time.time()
    contexto = await get_pokemon_async(id_pokemon)
    idtipos = {}
    n = 0
    for tipo in contexto['types']:
        n += 1
        type = tipo.get('type')
        url = type.get('url')
        idtipos[n] = {'id': await get_idtipo_async(url)}
    contexto2 = {
        'id': contexto['id'],
        'name': contexto.get('name'),
        'sprites': contexto.get('sprites'),
        'base_experience': contexto.get('base_experience'),
        'weight': contexto.get('weight'),
        'height': contexto.get('height'),
        'abilities': contexto.get('abilities'),
        'moves': contexto.get('moves'),
        'types': contexto.get('types'),
        'idtipos': idtipos,
    }
    tiempo_carga = time.time() - inicio_tiempo
    tiempo_carga = "{0:.2f} Seg.".format(tiempo_carga)
    return render(request, 'pokemones/pokemon_detail.html', {
        'object': contexto2,
        'tiempo_carga': tiempo_carga,
        'listar_tipo': 'pokemon_listartipofuncion_async',
        'titulo': 'Información del pokemon (Async)'
    })


async def pokemon_listtype_async(request, id_tipo):
    inicio_tiempo = time.time()
    contexto, tipo = await get_pokemonstype_async(id_tipo)
    id = 0
    contexto2 = {}
    for pokemon in contexto:
        id += 1
        poke = pokemon['pokemon']
        imagen = await get_imagen_async(poke['url'])
        contexto2[id] = {
            'id': imagen.get('id'),
            'nombre': poke['name'],
            'url': poke['url'],
            'imagen': imagen.get('imagen'),
        }
    cantidad = len(contexto2)
    tiempo_carga = time.time() - inicio_tiempo
    tiempo_carga = "{0:.2f} Seg.".format(tiempo_carga)
    return render(request, 'pokemones/pokemon_list.html', {
        'pokemones': contexto2,
        'tiempo_carga': tiempo_carga,
        'detail_url': 'pokemon_detallefuncion_async',
        'tipo': tipo,
        'cantidad': cantidad,
        'titulo': 'LISTA DE POKEMONES ASYNC'
    })
