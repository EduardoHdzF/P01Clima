import imp
from operator import pos


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
        "Longitud de destino" : lista_coordenadas[int(indice_prop) - 1][32:39]
    }

}

# Imprimir la ciudad seleccionada
print(iata_codes.get(lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7]))
# print(iata_codes.get(input()))
#'''

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