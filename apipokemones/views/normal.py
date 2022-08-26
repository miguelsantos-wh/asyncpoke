import asyncio
import time
import aiohttp

from django.shortcuts import render, reverse

from apipokemones.api.api_normal import get_pokemonstype, get_idtipo, get_pokemons, get_imagen, get_pokemon


def pokemon_list(request):
    inicio_tiempo = time.time()
    contexto = get_pokemons()
    id = 0
    contexto2 = {}
    for pokemon in contexto:
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
        'listar_tipo': 'pokemon_listartipofuncion',
        'titulo': 'Información del pokemon (Normal)'
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
