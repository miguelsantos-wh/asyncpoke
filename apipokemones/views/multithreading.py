import asyncio
import time
import aiohttp
import requests

from django.shortcuts import render, reverse
from concurrent.futures import ThreadPoolExecutor

from apipokemones.api.api_mltthr import (
    get_pokemons_mltthr, get_imagen_mltthr, get_pokemon_mltthr, get_idtipo_mltthr, get_pokemonstype_mltthr)


def pokemon_list_mltthr(request):
    inicio_tiempo = time.time()
    id = 0
    contexto2 = {}
    task, urls = [], []
    with ThreadPoolExecutor(max_workers=50) as executor:
        with requests.Session() as session:
            contexto = [pokemon for pokemon in executor.map(get_pokemons_mltthr, [session] * 1)]
            contexto = contexto[0]
            # for contexto in executor.map(get_pokemons_mltthr, [session] * 1):
            #     pass
            for pokemon in contexto:
                id += 1
                urls.append(pokemon['url'])
                contexto2[id] = {
                    'nombre': pokemon['name'],
                    'url': pokemon['url'],
                }
            imagenes_pokemon = [imagen_pokemon for imagen_pokemon in executor.map(get_imagen_mltthr, [session] * len(urls), [*urls] * len(urls))]
            # for imagen_pokemon in executor.map(get_imagen_mltthr, [session] * len(urls), [*urls] * len(urls)):
            #     imagenes_pokemon.append(imagen_pokemon)
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
                'detail_url': 'pokemon_detallefuncion_mltthr',
                'cantidad': cantidad,
                'titulo': 'LISTA DE POKEMONES MULTI THREADING'
            })


def pokemon_detail_mltthr(request, id_pokemon):
    inicio_tiempo = time.time()
    with ThreadPoolExecutor(max_workers=50) as executor:
        with requests.Session() as session:
            # contexto = await get_pokemon_mltthr(session, id_pokemon)
            contexto = [pokemon for pokemon in executor.map(get_pokemon_mltthr, [session] * 1)]
            contexto = contexto[0]
            idtipos = {}
            n = 0
            task_idtipo = []
            for tipo in contexto.get('types'):
                url = tipo.get('type').get('url')
                task_idtipo.append(get_idtipo_mltthr(session, url))
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


async def pokemon_listtype_async_aio_paralel_mltthd(request, id_tipo):
    inicio_tiempo = time.time()
    async with aiohttp.ClientSession() as session:
        contexto, tipo = await get_pokemonstype_mltthr(session, id_tipo)
        id = 0
        contexto2 = {}
        task = []
        for pokemon in contexto:
            id += 1
            poke = pokemon['pokemon']
            task.append(get_imagen_mltthr(session, poke['url']))
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
