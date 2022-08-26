import asyncio
import time
import aiohttp

from django.shortcuts import render, reverse

from apipokemones.api.api_async_aio import get_pokemons_async_aio, get_imagen_async_aio, get_pokemon_async_aio, \
    get_idtipo_async_aio, get_pokemonstype_async_aio


async def pokemon_list_async_aio_paralel(request):
    inicio_tiempo = time.time()
    id = 0
    contexto2 = {}
    task = []
    async with aiohttp.ClientSession() as session:
        contexto = await get_pokemons_async_aio(session)
        for pokemon in contexto:
            id += 1
            task.append(get_imagen_async_aio(session, pokemon['url']))
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
            'detail_url': 'pokemon_detallefuncion_async_aio_paralel',
            'cantidad': cantidad,
            'titulo': 'LISTA DE POKEMONES ASYNC AIO PARALEL'
        })


async def pokemon_detail_async_aio_paralel(request, id_pokemon):
    inicio_tiempo = time.time()
    async with aiohttp.ClientSession() as session:
        contexto = await get_pokemon_async_aio(session, id_pokemon)
        idtipos = {}
        n = 0
        task_idtipo = []
        for tipo in contexto.get('types'):
            url = tipo.get('type').get('url')
            task_idtipo.append(get_idtipo_async_aio(session, url))
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
            'listar_tipo': 'pokemon_listartipofuncion_async_aio_paralel',
            'titulo': 'Información del pokemon (Async, Aio, Paralel)'
        })


async def pokemon_listtype_async_aio_paralel(request, id_tipo):
    inicio_tiempo = time.time()
    async with aiohttp.ClientSession() as session:
        contexto, tipo = await get_pokemonstype_async_aio(session, id_tipo)
        id = 0
        contexto2 = {}
        task = []
        for pokemon in contexto:
            id += 1
            poke = pokemon['pokemon']
            task.append(get_imagen_async_aio(session, poke['url']))
            # loop = asyncio.get_event_loop()
            # task.append(loop.create_task(get_imagen_async(session, poke['url'])))
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
            'detail_url': 'pokemon_detallefuncion_async_aio_paralel',
            'tipo': tipo,
            'cantidad': cantidad,
            'titulo': 'LISTA DE POKEMONES ASYNC AIO PARALEL'
        })
