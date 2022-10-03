'''
    Para que pueda ejecutarse correctamente el programa, debemos ejecutarlo desde la
    carpeta P01Clima
    En este archivo de lee la lista de datos, de igual manera tiene la función de enlistar cada ciudad existente en los
    vuelos, también nos hace una lista de las coordenadas de origen y destino de los vuelos distinguibles que 
    existen en la lista dada.
'''

ciudades_archivo_csv = open('ClimaVuelos\Programa\Entrada\dataset1.csv', 'r+')

listaCoordenadas = []

# Agregar las ciudades a mi lista (sin repeticiones).

for iter in range(len(ciudades_archivo_csv.readlines())):
    
    if iter == 0:
        ciudades_archivo_csv.seek(0)
        ciudades_archivo_csv.readline()
        listaCoordenadas.append(ciudades_archivo_csv.readline())
        
    elif iter > 0:                    
        ciudades_archivo_csv.seek(0)

        if listaCoordenadas.count(ciudades_archivo_csv.readlines()[iter]) == 0:                                                
            ciudades_archivo_csv.seek(0)
            listaCoordenadas.append(ciudades_archivo_csv.readlines()[iter])                                
            ciudades_archivo_csv.seek(0)   

listaCoordenadas.sort()


# Creacion de una lista para el usuario para que pueda ver cual opcion escoger.
lista_ciudades = []

for iter in range(len(listaCoordenadas)):
    
    ciudades_org_des = [listaCoordenadas[iter][0:3] , listaCoordenadas[iter][4:7]]
    lista_ciudades.append(ciudades_org_des)

"""
    Imprime los vuelos distinguibles para que el usuario lo pueda ver y elegir el suyo
"""
def imprimeVuelos():

    print("Seleccione el viaje que desea realizar para saber el clima de cada ciudad (origen y destino):")

    for viaje in range(len(lista_ciudades)):

        ciudad = 0
        print("Vuelo número " + str(viaje+1) + ".- " , lista_ciudades[viaje][ciudad] , " -> " , lista_ciudades[viaje][ciudad + 1])

"""
    Nos crea una lista con las distintas ciudades que están en los vuelos con sus coordenadas
    nos regresa la lista creada
"""
def obtenerCiudades():
        
    diccionarioAeropuertos = {}       

    for vuelo in range(len(listaCoordenadas)):
        
        iata1 = listaCoordenadas[vuelo][0:3]
        iata2 = listaCoordenadas[vuelo][4:7]

        coord_lat_origen = listaCoordenadas[vuelo][6:]
        coord_long_origen = listaCoordenadas[vuelo][14:]
        coord_lat_destino = listaCoordenadas[vuelo][22:]    
        coord_long_destino =listaCoordenadas[vuelo][30:]

        diccionarioAeropuertos[iata1] = {
             
            "Latitud" : listaCoordenadas[vuelo][listaCoordenadas[vuelo].index(coord_lat_origen) + coord_lat_origen.index(',') + 1 : listaCoordenadas[vuelo].index(coord_long_origen)],
            "Longitud" : listaCoordenadas[vuelo][listaCoordenadas[vuelo].index(coord_long_origen) + coord_long_origen.index(',') + 1:listaCoordenadas[vuelo].index(coord_lat_destino) + 1], 
           
        }
        diccionarioAeropuertos[iata2] = {

            "Latitud" : listaCoordenadas[vuelo][listaCoordenadas[vuelo].index(coord_lat_destino) + coord_lat_destino.index(',') + 1:-11],
            "Longitud" : listaCoordenadas[vuelo][listaCoordenadas[vuelo].index(coord_long_destino) + coord_long_destino.index(',') + 1:-1]           
        }

    return diccionarioAeropuertos


