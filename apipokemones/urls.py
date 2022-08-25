from django.urls import path

from apipokemones.views import (
    pokemon_list, pokemon_detail, pokemon_listtype, pokemon_list_async, pokemon_detail_async, pokemon_listtype_async)

urlpatterns = [
    path('listar/', pokemon_list, name="pokemon_listarfuncion"),
    path('listar-async/', pokemon_list_async, name="pokemon_listarfuncion_async"),
    path('tipo/<int:id_tipo>/', pokemon_listtype, name="pokemon_listartipofuncion"),
    path('tipo-async/<int:id_tipo>/', pokemon_listtype_async, name="pokemon_listartipofuncion_async"),
    path('pokemon/<int:id_pokemon>/', pokemon_detail, name="pokemon_detallefuncion"),
    path('pokemon-async/<int:id_pokemon>/', pokemon_detail_async, name="pokemon_detallefuncion_async"),
    path('', pokemon_list, name="index"),
]
