## Paso 1: Ejegir carpeta para el proyecto y el entorno
## Paso 2: En la carpeta para el proyecto hacer git clone
    git clone https://github.com/miguelsantos-wh/asyncpoke.git
## Paso 3: Crear entorno en la carpeta para el entorno
    mkvirtualenv asyncpokeenv -p=3.6
    o 
    mkvirtualenv asyncpokeenv /path/pyhton3.6/
#### Confirmar que sea en python 3.6
    python -V
## Paso 4: Desactivar e iniciar entorno
#### Para desactivar podemos hacer:
    deactivate
#### Para iniciar podemos hacer
    workon asyncpokeenv
#### o estando en la carpeta del entorno
    source bin/activate
## Paso 5: instalamos dependencias con el entorno iniciado
    pip install  -r requirements.txt
## Paso 6: Iniciar el proyecto:
    ./manage.py runserver
## Paso 7: Para desactivar el proyecto:
    Ctrl+c
