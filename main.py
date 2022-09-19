import json
from urllib.request import urlopen

terminado = 1

# Para que el usuario tome la decision si quiere ver otra opcion de viaje o sino que finalice el programa.
while terminado == 1:

    print("--- CLIMA ---")

    print("Seleccione el viaje que desea realizar para saber el clima de cada ciudad (origen y destino):")

    ciudades_archivo_csv = open("dataset1.csv","r")

    actuliza_dicc = open("lista.txt","a+")

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

    # Ordenamos lista.
    lista_coordenadas.sort()    
    
    # Creacion de una lista para el usuario para que pueda ver cual opcion escoger.
    lista_ciudades = []
   
    for iter in range(len(lista_coordenadas)):
        
        ciudades_org_des = [lista_coordenadas[iter][0:3] , lista_coordenadas[iter][4:7]]
        lista_ciudades.append(ciudades_org_des)

    # Para manejar las excepciones.
    '''
        La función manejor de errores nos ayuda a que cuando se elija un viaje, este exista dentro de la lista de
        disponibles, y si no, que nos desplegue un mensaje de que no eligió un valor aceptable.
        @param el número de ciudades que se tienen disponibles.

    '''
    def manejo_errores(canti_ciudades):
        
        verif = False

        while not verif:

            try:

                ciudad_selec = int(input("Escoge un viaje (revisa la lista):\n"))

                if ciudad_selec > 0 and ciudad_selec <= canti_ciudades:

                    verif = True   

                else:

                    print("ERROR : Solo se puede introducir valores entre 1 - " + str(canti_ciudades) + ".")
                    verif = False             

            except ValueError:
                print("ERROR : Solo se pueden introducir valores numéricos.")

        return ciudad_selec

    print( lista_coordenadas[int(indice_prop) - 1][lista_coordenadas[int(indice_prop) - 1].index(coord_lat_origen) + coord_lat_origen.index(',') + 1:lista_coordenadas[int(indice_prop) - 1].index(coord_long_origen)])
    print(lista_coordenadas[int(indice_prop) - 1].index(coord_lat_origen))
    print( str(coord_lat_origen.index(',')) + "DFFFFFFFFFFFF")
    print(lista_coordenadas[int(indice_prop) - 1].index(coord_long_origen))

    print(lista_coordenadas[int(indice_prop) - 1][8:15])

    print( lista_coordenadas[int(indice_prop) - 1][lista_coordenadas[int(indice_prop) - 1].index(coord_long_origen) + coord_long_origen.index(',') + 1:lista_coordenadas[int(indice_prop) - 1].index(coord_lat_destino) + 1])
    
    print( lista_coordenadas[int(indice_prop) - 1][16:23])    
    print("laadkljalks" + str(coord_lat_destino.index(',')) )
    print(lista_coordenadas[indice_prop - 1][lista_coordenadas[int(indice_prop) - 1].index(coord_lat_origen) + coord_lat_origen.index(',') + 1:lista_coordenadas[int(indice_prop) - 1].index(coord_long_origen)+1])
    print(lista_coordenadas[int(indice_prop) - 1][lista_coordenadas[int(indice_prop) - 1].index(coord_long_origen) + coord_long_origen.index(',') + 1:lista_coordenadas[int(indice_prop) - 1].index(coord_lat_destino) + coord_lat_destino.index(',')])
    print(lista_coordenadas[int(indice_prop) - 1][lista_coordenadas[int(indice_prop) - 1].index(coord_lat_destino) + coord_lat_destino.index(',') + 1:lista_coordenadas[int(indice_prop) - 1].index(coord_long_destino) + coord_long_destino.index(',')])#-11])
    print( lista_coordenadas[int(indice_prop) - 1][lista_coordenadas[int(indice_prop) - 1].index(coord_long_destino) + coord_long_destino.index(',') + 1:-1])
    print(lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7])
    iata_codes = {

        lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7] : {

    # Obtener las coordenadas de la ciudad de origen
    long_org = iata_codes [lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7]] ['Longitud de origen']
    lat_org = iata_codes [lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7]] ['Latitud de origen']

    # Obtener las coordenadas de la ciudad de destino
    long_des = iata_codes [lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7]] ['Longitud de destino']
    lat_des = iata_codes [lista_coordenadas[int(indice_prop) - 1][0:3] and lista_coordenadas[int(indice_prop) - 1][4:7]] ['Latitud de destino']
    
    ciudad_org_cache = False

    ciudad_des_cache = False

    historial = open("lista.txt","r+")

    if len(historial.readlines()) == 0:
        diccionario_guardar = { 
            "Ciudad" : {
                
            }
        }        
    else:
        diccionario_guardar = {}

        historial.seek(0)
        diccionario_guardar = eval(historial.readline())               

        ciudad1 = diccionario_guardar["Ciudad"].get(lista_coordenadas[int(indice_prop) - 1][0:3])
        print(ciudad1)
        ciudad2 = diccionario_guardar["Ciudad"].get(lista_coordenadas[int(indice_prop) - 1][4:7])
        print(ciudad2)
        if ciudad1 != None and ciudad2 != None:

            ciudad_org_cache = True
            ciudad_des_cache = True
        elif ciudad1 != None and ciudad2 == None:

            ciudad_org_cache = True
        elif ciudad1 == None and ciudad2 != None:

            ciudad_des_cache = True             

    if not ciudad_org_cache and not ciudad_des_cache:

        # Llamada Api de ciudad de origen
        url_modif_org = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat_org) + "&lon=" + str(long_org) + "&units=metric" +"&appid=b2844c1e815b5b3dde610589df05cad2"
        url_org = url_modif_org
        
        with urlopen(url_org) as json_dicc_org:
            json_data_org = json_dicc_org.read()

        # Imprime el clima de la ciudad de origen (diccionario).
        clima_org = json.loads(json_data_org)        
        
        # Llamada Api de ciudad de destino
        url_modif_des = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat_des) + "&lon=" + str(long_des) + "&units=metric" + "&appid=b2844c1e815b5b3dde610589df05cad2"
        url_des = url_modif_des

        with urlopen(url_des) as json_dicc_des:
            json_data_des = json_dicc_des.read()

        # Imprime el clima de la ciudad de origen (diccionario).
        clima_des = json.loads(json_data_des)        

        # Clima de la ciudad de origen:
        print("- Clima de la ciudad de origen -\n    Condición actual : " + clima_org ['weather'][0]['main'] + "\n    Descripción : " + clima_org ['weather'][0]['description'] + "\n    Temperatura : " , clima_org ['main']['temp'] , "\n    Temperatura mínima : " , clima_org ['main']['temp_min'] , "\n    Temperatura máxima : " , clima_org ['main']['temp_max'] , "\n    Humedad (%) : " , clima_org ['main']['humidity'] , "\n    Velocidad del viento : " , clima_org ['wind']['speed'] , "\n    Nubes : " , clima_org ['clouds']['all'] , "\n    Nombre : " , clima_org ['name'] , "\n\n")

        # Clima de la ciudad de destino:
        print("- Clima de la ciudad de destino -\n    Condición actual : " + clima_des ['weather'][0]['main'] + "\n    Descripción : " + clima_des ['weather'][0]['description'] + "\n    Temperatura : " , clima_des ['main']['temp'] , "\n    Temperatura mínima : " , clima_des ['main']['temp_min'] , "\n    Temperatura máxima : " , clima_des ['main']['temp_max'] , "\n    Humedad (%) : " , clima_des ['main']['humidity'] , "\n    Velocidad del viento : " , clima_des ['wind']['speed'] , "\n    Nubes : " , clima_des ['clouds']['all'] , "\n    Nombre : " , clima_des ['name'])
        
        diccionario_guardar["Ciudad"][lista_coordenadas[int(indice_prop) - 1][0:3]] = { "Nombre" : clima_org ['name'] , "Clima" : clima_org['weather'][0]['main'] , "Descripcion" : clima_org ['weather'][0]['description'] , "Temperatura" : clima_org ['main']['temp'] , "Temperatura minima" : clima_org ['main']['temp_min'] , "Temperatura maxima" : clima_org ['main']['temp_max'] , "Humedad" : clima_org ['main']['humidity'] , "Velocidad del viento" : clima_org ['wind']['speed'] , "Nubes" : clima_org ['clouds']['all']}

        diccionario_guardar["Ciudad"][lista_coordenadas[int(indice_prop) - 1][4:7]] = { "Nombre" : clima_des ['name'] , "Clima" : clima_des['weather'][0]['main'] , "Descripcion" : clima_des ['weather'][0]['description'] , "Temperatura" : clima_des ['main']['temp'] , "Temperatura minima" : clima_des ['main']['temp_min'] , "Temperatura maxima" : clima_des ['main']['temp_max'] , "Humedad" : clima_des ['main']['humidity'] , "Velocidad del viento" : clima_des ['wind']['speed'] , "Nubes" : clima_des ['clouds']['all']}
        
    elif ciudad_org_cache and not ciudad_des_cache:

        clima_org = diccionario_guardar["Ciudad"].get(lista_coordenadas[int(indice_prop) - 1][0:3])

        # Llamada Api de ciudad de destino
        url_modif_des = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat_des) + "&lon=" + str(long_des) + "&units=metric" + "&appid=b2844c1e815b5b3dde610589df05cad2"
        url_des = url_modif_des

        with urlopen(url_des) as json_dicc_des:
            json_data_des = json_dicc_des.read()

        # Imprime el clima de la ciudad de origen (diccionario).
        clima_des = json.loads(json_data_des)

        # Clima de la ciudad de origen:
        print("-- Clima de la ciudad de origen -\n    Condición actual : " + clima_org ['Clima'] + "\n    Descripción : " + clima_org ['Descripcion'] + "\n    Temperatura : " , clima_org ['Temperatura'] , "\n    Temperatura mínima : " , clima_org ['Temperatura minima'] , "\n    Temperatura máxima : " , clima_org ['Temperatura maxima'] , "\n    Humedad (%) : " , clima_org ['Humedad'] , "\n    Velocidad del viento : " , clima_org ['Velocidad del viento'] , "\n    Nubes : " , clima_org ['Nubes'] , "\n    Nombre : " , clima_org ['Nombre'] , "\n\n")

        # Clima de la ciudad de destino:
        print("- Clima de la ciudad de destino -\n    Condición actual : " + clima_des ['weather'][0]['main'] + "\n    Descripción : " + clima_des ['weather'][0]['description'] + "\n    Temperatura : " , clima_des ['main']['temp'] , "\n    Temperatura mínima : " , clima_des ['main']['temp_min'] , "\n    Temperatura máxima : " , clima_des ['main']['temp_max'] , "\n    Humedad (%) : " , clima_des ['main']['humidity'] , "\n    Velocidad del viento : " , clima_des ['wind']['speed'] , "\n    Nubes : " , clima_des ['clouds']['all'] , "\n    Nombre : " , clima_des ['name'])

        diccionario_guardar["Ciudad"][lista_coordenadas[int(indice_prop) - 1][4:7]] = { "Nombre" : clima_des ['name'] , "Clima" : clima_des['weather'][0]['main'] , "Descripcion" : clima_des ['weather'][0]['description'] , "Temperatura" : clima_des ['main']['temp'] , "Temperatura minima" : clima_des ['main']['temp_min'] , "Temperatura maxima" : clima_des ['main']['temp_max'] , "Humedad" : clima_des ['main']['humidity'] , "Velocidad del viento" : clima_des ['wind']['speed'] , "Nubes" : clima_des ['clouds']['all']}

    elif not ciudad_org_cache and ciudad_des_cache:

        clima_des = diccionario_guardar["Ciudad"].get(lista_coordenadas[int(indice_prop) - 1][4:7])

        # Llamada Api de ciudad de origen
        url_modif_org = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat_org) + "&lon=" + str(long_org) + "&units=metric" + "&appid=b2844c1e815b5b3dde610589df05cad2"
        url_org = url_modif_org

        with urlopen(url_org) as json_dicc_org:
            json_data_org = json_dicc_org.read()

        # Imprime el clima de la ciudad de origen (diccionario).
        clima_org = json.loads(json_data_org)

        # Clima de la ciudad de origen:
        print("- Clima de la ciudad de origen -\n    Condición actual : " + clima_org ['weather'][0]['main'] + "\n    Descripción : " + clima_org ['weather'][0]['description'] + "\n    Temperatura : " , clima_org ['main']['temp'] , "\n    Temperatura mínima : " , clima_org ['main']['temp_min'] , "\n    Temperatura máxima : " , clima_org ['main']['temp_max'] , "\n    Humedad (%) : " , clima_org ['main']['humidity'] , "\n    Velocidad del viento : " , clima_org ['wind']['speed'] , "\n    Nubes : " , clima_org ['clouds']['all'] , "\n    Nombre : " , clima_org ['name'] , "\n\n")

        # Clima de la ciudad de destino:
        print("-- Clima de la ciudad de origen -\n    Condición actual : " + clima_des ['Clima'] + "\n    Descripción : " + clima_des ['Descripcion'] + "\n    Temperatura : " , clima_des ['Temperatura'] , "\n    Temperatura mínima : " , clima_des ['Temperatura minima'] , "\n    Temperatura máxima : " , clima_des ['Temperatura maxima'] , "\n    Humedad (%) : " , clima_des ['Humedad'] , "\n    Velocidad del viento : " , clima_des ['Velocidad del viento'] , "\n    Nubes : " , clima_des ['Nubes'] , "\n    Nombre : " , clima_des ['Nombre'])

        diccionario_guardar["Ciudad"][lista_coordenadas[int(indice_prop) - 1][0:3]] = { "Nombre" : clima_org ['name'] , "Clima" : clima_org['weather'][0]['main'] , "Descripcion" : clima_org ['weather'][0]['description'] , "Temperatura" : clima_org ['main']['temp'] , "Temperatura minima" : clima_org ['main']['temp_min'] , "Temperatura maxima" : clima_org ['main']['temp_max'] , "Humedad" : clima_org ['main']['humidity'] , "Velocidad del viento" : clima_org ['wind']['speed'] , "Nubes" : clima_org ['clouds']['all']}

    else:

        clima_org = diccionario_guardar["Ciudad"].get(lista_coordenadas[int(indice_prop) - 1][0:3])

        clima_des = diccionario_guardar["Ciudad"].get(lista_coordenadas[int(indice_prop) - 1][4:7])

        # Clima de la ciudad de origen:
        print("-- Clima de la ciudad de origen -\n    Condición actual : " + clima_org ['Clima'] + "\n    Descripción : " + clima_org ['Descripcion'] + "\n    Temperatura : " , clima_org ['Temperatura'], " °C", "\n    Temperatura mínima : " , clima_org ['Temperatura minima'] , "\n    Temperatura máxima : " , clima_org ['Temperatura maxima'] , "\n    Humedad (%) : " , clima_org ['Humedad'] , "\n    Velocidad del viento : " , clima_org ['Velocidad del viento'] , "\n    Nubes : " , clima_org ['Nubes'] , "\n    Nombre : " , clima_org ['Nombre'] , "\n\n")

    actuliza_dicc.truncate(0)
    
    actuliza_dicc.write(str(diccionario_guardar))    

    def finaliza():
        
        verif = False

        while not verif:

            try:

                termina = int(input("** Para regresar al menu de opciones presiona 1.\n** Para finalizar programa presiona 0.\n"))

                if termina == 0 or termina == 1:

                    verif = True   

                else:

                    print("ERROR : Solo se puede introducir valores 0 o 1")
                    verif = False             

            except ValueError:
                print("ERROR : Solo se pueden introducir valores numéricos.")

        return termina

    # El usuario decide si se finaliza el programa o no.
    terminado = finaliza()

    ciudades_archivo_csv.close()

    historial.close()