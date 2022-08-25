import asyncio
import time
import aiohttp
import requests

from django.shortcuts import render, reverse
from apipokemones.api import get_pokemons, get_pokemon, get_imagen, get_idtipo, \
    get_pokemonstype, get_imagen_async, get_pokemon_async, get_idtipo_async, get_pokemons_async, get_pokemonstype_async


# Create your views here.


def pokemon_list(request):
    inicio_tiempo = time.time()
    contexto = {'pokemones': get_pokemons()}
    id = 0
    contexto2 = {}
    for pokemon in contexto['pokemones']:
        id += 1
        imagen = get_imagen(pokemon['url'])
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
        'detail_url': 'pokemon_detallefuncion',
        'cantidad': cantidad,
        'titulo': 'LISTA DE POKEMONES NORMAL'
    })


async def pokemon_list_async(request):
    inicio_tiempo = time.time()
    id = 0
    contexto2 = {}
    task = []
    async with aiohttp.ClientSession() as session:
        contexto = await get_pokemons_async(session)
        for pokemon in contexto:
            id += 1
            task.append(get_imagen_async(session, pokemon['url']))
            # loop = asyncio.get_event_loop()
            # task.append(loop.create_task(get_imagen_async(session, pokemon['url'])))
            contexto2[id] = {
                'nombre': pokemon['name'],
                'url': pokemon['url'],
            }
        imagenes_pokemon = await asyncio.gather(*task)
        id = 0
        for key, data in contexto2.items():
            data.update({
                'id': imagenes_pokemon[id].get('id'),
                'imagen': imagenes_pokemon[id].get('imagen'),
            })
            id += 1
        cantidad = len(contexto2)
        tiempo_carga = time.time() - inicio_tiempo
        tiempo_carga = "{0:.2f} Seg.".format(tiempo_carga)
        return render(request, 'pokemones/pokemon_list.html', {
            'pokemones': contexto2,
            'tiempo_carga': tiempo_carga,
            'detail_url': 'pokemon_detallefuncion_async',
            'cantidad': cantidad,
            'titulo': 'LISTA DE POKEMONES ASYNC'
        })


def pokemon_detail(request, id_pokemon):
    inicio_tiempo = time.time()
    contexto = get_pokemon(id_pokemon)
    idtipos = {}
    n = 0
    for tipo in contexto['types']:
        n += 1
        type = tipo.get('type')
        url = type.get('url')
        idtipos[n] = {'id': get_idtipo(url)}
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
        'listar_tipo': 'pokemon_listartipofuncion'
    })


async def pokemon_detail_async(request, id_pokemon):
    inicio_tiempo = time.time()
    async with aiohttp.ClientSession() as session:
        contexto = await get_pokemon_async(session, id_pokemon)
        idtipos = {}
        n = 0
        task_idtipo = []
        for tipo in contexto.get('types'):
            url = tipo.get('type').get('url')
            task_idtipo.append(get_idtipo_async(session, url))
        response_idtipo = await asyncio.gather(*task_idtipo)
        for response in response_idtipo:
            idtipos[n] = {'id': response}
            n += 1
        contexto2 = {
            'id': contexto.get('id'),
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
            'listar_tipo': 'pokemon_listartipofuncion_async'
        })


def pokemon_listtype(request, id_tipo):
    inicio_tiempo = time.time()
    contexto, tipo = get_pokemonstype(id_tipo)
    id = 0
    contexto2 = {}
    for pokemon in contexto:
        id += 1
        poke = pokemon['pokemon']
        imagen = get_imagen(poke['url'])
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
        'detail_url': 'pokemon_detallefuncion',
        'tipo': tipo,
        'cantidad': cantidad,
        'titulo': 'LISTA DE POKEMONES NORMAL'
    })


async def pokemon_listtype_async(request, id_tipo):
    inicio_tiempo = time.time()
    async with aiohttp.ClientSession() as session:
        contexto, tipo = await get_pokemonstype_async(session, id_tipo)
        id = 0
        contexto2 = {}
        task = []
        for pokemon in contexto:
            id += 1
            poke = pokemon['pokemon']
            task.append(get_imagen_async(session, poke['url']))
            contexto2[id] = {
                'nombre': poke['name'],
                'url': poke['url'],
            }
        imagenes_pokemon = await asyncio.gather(*task)
        cantidad = len(contexto2)
        id = 0
        for key, data in contexto2.items():
            data.update({
                'id': imagenes_pokemon[id].get('id'),
                'imagen': imagenes_pokemon[id].get('imagen'),
            })
            id += 1
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

