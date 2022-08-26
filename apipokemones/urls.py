from django.urls import path

from apipokemones.views.async import pokemon_list_async, pokemon_detail_async, pokemon_listtype_async
from apipokemones.views.async_aio import pokemon_list_async_aio, pokemon_listtype_async_aio, pokemon_detail_async_aio
from apipokemones.views.async_aio_paralel import pokemon_list_async_aio_paralel, pokemon_listtype_async_aio_paralel, \
    pokemon_detail_async_aio_paralel
from apipokemones.views.async_paralel import pokemon_list_async_paralel, pokemon_listtype_async_paralel, \
    pokemon_detail_async_paralel
from apipokemones.views.normal import pokemon_list, pokemon_listtype, pokemon_detail

urlpatterns = [
    #   listar
    path('listar/', pokemon_list, name="pokemon_listarfuncion"),
    path('listar-async/', pokemon_list_async, name="pokemon_listarfuncion_async"),
    path('listar-async-paralel/', pokemon_list_async_paralel, name="pokemon_listarfuncion_async_paralel"),
    path('listar-async-aio/', pokemon_list_async_aio, name="pokemon_listarfuncion_async_aio"),
    path('listar-async-aio-paralel/', pokemon_list_async_aio_paralel,
         name="pokemon_listarfuncion_async_aio_paralel"),

    #   listar por tipo
    path('tipo/<int:id_tipo>/', pokemon_listtype, name="pokemon_listartipofuncion"),
    path('tipo-async/<int:id_tipo>/', pokemon_listtype_async, name="pokemon_listartipofuncion_async"),
    path('tipo-async-paralel/<int:id_tipo>/', pokemon_listtype_async_paralel,
         name="pokemon_listartipofuncion_async_paralel"),
    path('tipo-async-aio/<int:id_tipo>/', pokemon_listtype_async_aio, name="pokemon_listartipofuncion_async_aio"),
    path('tipo-async-aio-paralel/<int:id_tipo>/', pokemon_listtype_async_aio_paralel,
         name="pokemon_listartipofuncion_async_aio_paralel"),

    #   obtener detalle del pokemon
    path('pokemon/<int:id_pokemon>/', pokemon_detail, name="pokemon_detallefuncion"),
    path('pokemon-async/<int:id_pokemon>/', pokemon_detail_async, name="pokemon_detallefuncion_async"),
    path('pokemon-async-paralel/<int:id_pokemon>/', pokemon_detail_async_paralel,
         name="pokemon_detallefuncion_async_paralel"),
    path('pokemon-async-aio/<int:id_pokemon>/', pokemon_detail_async_aio, name="pokemon_detallefuncion_async_aio"),
    path('pokemon-async-aio-paralel/<int:id_pokemon>/', pokemon_detail_async_aio_paralel,
         name="pokemon_detallefuncion_async_aio_paralel"),

    #   inicio
    path('', pokemon_list, name="index"),
]
