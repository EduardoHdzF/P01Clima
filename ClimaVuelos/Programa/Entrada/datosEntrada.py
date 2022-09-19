'''Para que pueda ejecutarse correctamente el programa, debemos ejecutarlo desde la
    carpeta P01Clima
'''
'''
with open('ClimaVuelos\Programa\Entrada\dataset1.csv', 'r+') as ArchivoEntrada:

#ArchivoEntrada = open('ClimaVuelos\Programa\Entrada\dataset1.csv', 'r+')
    print(type(ArchivoEntrada))

    #print(ArchivoEntrada.readline())
    Lista = []

    for linea in range(len(ArchivoEntrada.readlines())):#ArchivoEntrada:
        ArchivoEntrada.seek(0)
        print(ArchivoEntrada.readline())
        print(ArchivoEntrada.readline())    
        Lista.append(ArchivoEntrada.readline())

    #print(ArchivoEntrada.readlines())
    print(Lista)
'''

#ciudades_archivo_csv = open('ClimaVuelos\Programa\Entrada\dataset1.csv', 'r+')#"dataset1.csv","r")
import json


ciudades_archivo_csv = open('ClimaVuelos/Programa/Entrada/dataset1.csv', 'r+')#"dataset1.csv","r")

listaCoordenadas = []

# Agregar las ciudades a mi lista (sin repeticiones).
for iter in range(len(ciudades_archivo_csv.readlines())):
    
    if iter == 1:
        ciudades_archivo_csv.seek(0)
        ciudades_archivo_csv.readline()
        listaCoordenadas.append(ciudades_archivo_csv.readline())
        
    elif iter > 1:                    
        ciudades_archivo_csv.seek(0)

        if listaCoordenadas.count(ciudades_archivo_csv.readlines()[iter]) == 0: #not listaCoordenadas.count(ciudades_archivo_csv.readlines()[iter]):   
            ciudades_archivo_csv.seek(0)
            listaCoordenadas.append(ciudades_archivo_csv.readlines()[iter])                                
            ciudades_archivo_csv.seek(0)        

listaCoordenadas.sort()

#print(listaCoordenadas)

 # Creacion de una lista para el usuario para que pueda ver cual opcion escoger.
lista_ciudades = []

for iter in range(len(listaCoordenadas)):
    
    ciudades_org_des = [listaCoordenadas[iter][0:3] , listaCoordenadas[iter][4:7]]
    lista_ciudades.append(ciudades_org_des)

#posicion = 1
for viaje in range(len(lista_ciudades)):

    #ciudad = 0
    for ciudad in range(1):

        print("Vuelo número " + str(viaje+1) + ".- " , lista_ciudades[viaje][ciudad] , " -> " , lista_ciudades[viaje][ciudad + 1])

def obtenerCiudades():
        
    listaCiudades = {}       
    
    for vuelo in range(len(listaCoordenadas)):

        iata1 = listaCoordenadas[vuelo][0:3]
        iata2 = listaCoordenadas[vuelo][4:7]

        coord_lat_origen = listaCoordenadas[int(vuelo)][6:]
        #print(coord_lat_origen)
        coord_long_origen = listaCoordenadas[int(vuelo)][14:]
        #print(coord_long_origen)
        coord_lat_destino = listaCoordenadas[int(vuelo)][22:]    
        #print(coord_lat_destino)
        coord_long_destino =listaCoordenadas[int(vuelo)][30:]
        #print(coord_long_destino)

        listaCiudades[iata1] = {

            #"Latitud" : listaCoordenadas[int(vuelo) - 1][listaCoordenadas[int(vuelo) - 1].index(coord_lat_origen) + coord_lat_origen.index(',') + 1 : listaCoordenadas[int(vuelo) - 1].index(coord_long_origen)],
            #"Longitud" : listaCoordenadas[int(vuelo) - 1][listaCoordenadas[int(vuelo) - 1].index(coord_long_origen) + coord_long_origen.index(',') + 1:listaCoordenadas[int(vuelo) - 1].index(coord_lat_destino) + 1],            
            "Latitud" : listaCoordenadas[int(vuelo)][listaCoordenadas[int(vuelo)].index(coord_lat_origen) + coord_lat_origen.index(',') + 1 : listaCoordenadas[int(vuelo)].index(coord_long_origen)],
            "Longitud" : listaCoordenadas[int(vuelo)][listaCoordenadas[int(vuelo)].index(coord_long_origen) + coord_long_origen.index(',') + 1:listaCoordenadas[int(vuelo)].index(coord_lat_destino) + 1],            

        }
        listaCiudades[iata2] = {

            #"Latitud" : listaCoordenadas[int(vuelo) - 1][listaCoordenadas[int(vuelo) - 1].index(coord_lat_destino) + coord_lat_destino.index(',') + 1:listaCoordenadas[int(vuelo) - 1].index(coord_long_destino) + coord_long_destino.index(',')],#-11],
            #"Longitud" : listaCoordenadas[int(vuelo) - 1][listaCoordenadas[int(vuelo) - 1].index(coord_long_destino) + coord_long_destino.index(',') + 1:-1]    
            "Latitud" : listaCoordenadas[int(vuelo)][listaCoordenadas[int(vuelo)].index(coord_lat_destino) + coord_lat_destino.index(',') + 1:-11],
            "Longitud" : listaCoordenadas[int(vuelo)][listaCoordenadas[int(vuelo)].index(coord_long_destino) + coord_long_destino.index(',') + 1:-1]    
        }
    
    #print("Número de ciudades distintas")
    #(len(listaCiudades.keys()))    
    #print(listaCiudades)
    #print(json.dumps(listaCiudades, indent=2))
    return listaCiudades


