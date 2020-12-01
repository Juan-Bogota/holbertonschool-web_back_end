# 0x0B. Redis basic
> ## Specializations - Web Stack programming ― Back-end

# Que es redis
Base de Datos no sql
clave: valor
se obtiene la informacion sabiendo la clave
base de datos cache
* string, list, set, mapa de bits

## Caracteristicas 
* Velocidad = obtener informacion en poco tiempo
* Persistencia
* Estructura de datos
* Operaciones atomicas
* Lenguajes Compatibles
* Replicacion maestro/ esclavo
* Sharding: fragmentar los datos en diferentes servidores
* Portatil


## Puerto
* 6379

## Archivo de configuracion Ubuntu
* / etc/redis/redis.conf
    
* config get obtener un valor de una llave
    - config get dir
    - config get dbfilename

* config set setear un valor de una llave
    - config get loglevel
    - config set loglevel verbose
    - config loglevel notice


## cambiar puerto 
redis-server --port 6380
