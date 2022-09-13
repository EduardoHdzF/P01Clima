#import imp
#from operator import pos
from asyncore import read
import json
from urllib.request import urlopen

print("--- CLIMA ---")

print("Seleccione las ciudades de origen y destino donde se quiere saber su clima de cada uno:")

ciudades_archivo_csv = open("dataset1.csv","r")

print("- Ciudad de origen -")

print("- Ciudad de destino -")

#ciudades_archivo = open("ciudades.csv","r+")

lista_coordenadas = []

# Agregar las ciudades a mi lista (sin repeticiones).
for iter in range(len(ciudades_archivo_csv.readlines())):
    
    if iter == 1:
        ciudades_archivo_csv.seek(0)
        ciudades_archivo_csv.readline()
        lista_coordenadas.append(ciudades_archivo_csv.readline())
        
    elif iter > 1:                    
        ciudades_archivo_csv.seek(0)

        if not lista_coordenadas.count(ciudades_archivo_csv.readlines()[iter]):                                                
            ciudades_archivo_csv.seek(0)
            lista_coordenadas.append(ciudades_archivo_csv.readlines()[iter])                                
            ciudades_archivo_csv.seek(0)          

print(lista_coordenadas)
print("** Tamanio de la lista: " , len(lista_coordenadas) , "\n")

# Ordenamos lista.
lista_coordenadas.sort()
print(lista_coordenadas)

# Creacion de una lista para el usuario para que pueda ver cual opcion escoger.
lista_ciudades = []
posicion = 1

for iter in range(len(lista_coordenadas)):
    
    ciudades_org_des = [lista_coordenadas[iter][0:3] , lista_coordenadas[iter][4:7]]
    lista_ciudades.append(ciudades_org_des)

print(lista_ciudades)

# Despliega la lista de viajes disponibles.
for viaje in range(len(lista_ciudades)):
        
    for ciudad in range(1):

        print(str(posicion) + ".- " , lista_ciudades[viaje][ciudad] , " -> " , lista_ciudades[viaje][ciudad + 1])
        posicion += 1

# Creacion de diccionario.
#'''
indice_prop = input("Escoge un viaje:")

iata_codes = {

    lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7] : {
        "Latitud de origen" : lista_coordenadas[int(indice_prop) - 1][8:15],
        "Longitud de origen" : lista_coordenadas[int(indice_prop) - 1][16:23],
        "Latitud de destino" : lista_coordenadas[int(indice_prop) - 1][24:31],
        "Longitud de destino" : lista_coordenadas[int(indice_prop) - 1][32:39],        
    }

}

# Imprimir la ciudad seleccionada
print(iata_codes.get(lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7]))
# print(iata_codes.get(input()))

# Obtener las coordenadas de la ciudad de origen
long_org = iata_codes [lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7]] ['Longitud de origen']
lat_org = iata_codes [lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7]] ['Latitud de origen']

# Obtener las coordenadas de la ciudad de destino
long_des = iata_codes [lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7]] ['Longitud de destino']
lat_des = iata_codes [lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7]] ['Latitud de destino']
#'''

# Llamada Api de ciudad de origen
url_modif_org = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat_org) + "&lon=" + str(long_org) + "&appid=b2844c1e815b5b3dde610589df05cad2"
url_org = url_modif_org

with urlopen(url_org) as json_dicc_org:
    json_data_org = json_dicc_org.read()

# Imprime el clima de la ciudad de origen (diccionario).
clima_org = json.loads(json_data_org)
print(json.dumps(clima_org,indent = 2))

# Llamada Api de ciudad de destino
url_modif_des = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat_des) + "&lon=" + str(long_des) + "&appid=b2844c1e815b5b3dde610589df05cad2"
url_des = url_modif_des

with urlopen(url_des) as json_dicc_des:
    json_data_des = json_dicc_des.read()

# Imprime el clima de la ciudad de origen (diccionario).
clima_des = json.loads(json_data_des)
print(json.dumps(clima_des,indent = 2))

# Clima de la ciudad de origen:
print("- Clima de la ciudad de origen -\n    Condición actual : " + clima_org ['weather'][0]['main'] + "\n    Descripción : " + clima_org ['weather'][0]['description'] + "\n    Temperatura : " , clima_org ['main']['temp'] , "\n    Temperatura mínima : " , clima_org ['main']['temp_min'] , "\n    Temperatura máxima : " , clima_org ['main']['temp_max'] , "\n    Humedad (%) : " , clima_org ['main']['humidity'] , "\n    Velocidad del viento : " , clima_org ['wind']['speed'] , "\n    Nubes : " , clima_org ['clouds']['all'] , "\n\n")

# Clima de la ciudad de destino:
print("- Clima de la ciudad de destino -\n    Condición actual : " + clima_des ['weather'][0]['main'] + "\n    Descripción : " + clima_des ['weather'][0]['description'] + "\n    Temperatura : " , clima_des ['main']['temp'] , "\n    Temperatura mínima : " , clima_des ['main']['temp_min'] , "\n    Temperatura máxima : " , clima_des ['main']['temp_max'] , "\n    Humedad (%) : " , clima_des ['main']['humidity'] , "\n    Velocidad del viento : " , clima_des ['wind']['speed'] , "\n    Nubes : " , clima_des ['clouds']['all'])

## Creacion de un diccionario con una ciudad en particular.
'''
iata_codes_ejemplo = {

    lista_ciudades[0][0:3] and lista_ciudades[0][4:7] : {
        "Latitud de origen" : lista_ciudades[0][8:15],
        "Longitud de origen" : lista_ciudades[0][16:23],
        "Latitud de destino" : lista_ciudades[0][24:31],
        "Longitud de destino" : lista_ciudades[0][32:39]
        }

}

print(lista_ciudades[0][0:3])
print(iata_codes_ejemplo.get(lista_ciudades[0][0:3] and lista_ciudades[0][4:7]))
print(iata_codes_ejemplo.get("ACA" and "MEX"))
print(len(iata_codes_ejemplo))
'''

## Imprimir el tamanio de la lista
'''
print(len(lista_ciudades))
'''

## Prueba de comparaciones hace caso omiso del segundo que se esta comparando cuando se utilizan dos readlines.
## Imprime el siguiente si se utiliza solo una vez.
'''
lista_ciudades.append(ciudades_archivo_csv.readline())

#if ciudades_archivo_csv.readline() != ciudades_archivo_csv.readline:
#    print(ciudades_archivo_csv.readline())

if lista_ciudades[0] != ciudades_archivo_csv.readline:
    print(ciudades_archivo_csv.readline())
'''

## Reiniciar leer las lineas del archivo.
'''
ciudades_archivo_csv.seek(0)
'''

## Aniadir una ciudad en particular a mi lista.
'''
ciudad = ciudades_archivo_csv.readlines()[1][0:3]
print(ciudad[0])
#print(ciudad[1])
lista_ciudades.append(ciudad)
print(lista_ciudades)
'''

## Comparar dos ciudades una en la lista y otra en el archivo
### - Iguales
'''
ciudades_archivo_csv.readline()
ciudades_archivo_csv.readline()
ciudades_archivo_csv.readline()
ciudades_archivo_csv.readline()
ciudades_archivo_csv.readline()


### - No iguales
"""
ciudades_archivo_csv.readline()
"""

ciudad1 = ciudades_archivo_csv.readline()
print(ciudad1)

ciudad2 = ciudades_archivo_csv.readline()
print(ciudad2)

lista_ciudades.append(ciudad1)
print(lista_ciudades)

if lista_ciudades[0] == ciudad2:
    print("-- Son iguales.")
else:
    print("-- No son iguales.")

if lista_ciudades[0] == ciudad2:
    print(ciudad2)
'''

ciudades_archivo_csv.close()

#ciudades_archivo.close()