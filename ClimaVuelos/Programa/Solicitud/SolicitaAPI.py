import json
from urllib.request import urlopen

import Solicitud.Cache.CreaCache as cache
import Entrada.datosEntrada as entrada


class SolicitaApi:

    enlace =  "https://api.openweathermap.org/data/2.5/weather?lat="    

    def __init__(self, lista_coordenadas, indice_proporcionado):
        self.lista_coordenadas = lista_coordenadas
        self.indice_proporcionado = indice_proporcionado  
    
    """
        Nos hace la llamada en la API de la ciudad dada con las coordenadas proporcionadas
        como parámetros
    """
    def solicitarAPI(self,latitud, longitud):

        url_modif_org = self.enlace + str(latitud) + "&lon=" + str(longitud) + "&units=metric" +"&appid="+ self.obtenerId()
        return url_modif_org

    """
        Nos devuelve la clave de la API para que podamos hacer la llamada.
        Esta clave se encuentra en el archivo, clave.txt que deberá estar dentro de la
        carpeta Clave
    """
    def obtenerId(self):
        archivoID = open("ClimaVuelos\Programa\Clave\clave.txt")
        clave = archivoID.readline()
        archivoID.close()
        return clave

    """
        Nos devuelve una lista con los datos de los vuelos, es decir sus 
        claves correspondientes de origen y destino, así como sus coordenadas        
    """
    def identificarCoordenadasVuelos(self):                    
        
        dicionarioCoordenadasVuelos = {}

        for vuelo in range(len(self.lista_coordenadas)):

            coord_lat_origen = self.lista_coordenadas[int(vuelo) - 1][6:]
            coord_long_origen = self.lista_coordenadas[int(vuelo) - 1][14:]
            coord_lat_destino = self.lista_coordenadas[int(vuelo) - 1][22:]    
            coord_long_destino = self.lista_coordenadas[int(vuelo) - 1][30:]

            dicionarioCoordenadasVuelos[vuelo] = {
                "Latitud de origen" : self.lista_coordenadas[vuelo - 1][self.lista_coordenadas[int(vuelo) - 1].index(coord_lat_origen) + coord_lat_origen.index(',') + 1 : self.lista_coordenadas[int(vuelo) - 1].index(coord_long_origen)+1],
                "Longitud de origen" : self.lista_coordenadas[int(vuelo) - 1][self.lista_coordenadas[int(vuelo) - 1].index(coord_long_origen) + coord_long_origen.index(',') + 1:self.lista_coordenadas[int(vuelo) - 1].index(coord_lat_destino) + coord_lat_destino.index(',')],            
                "Latitud de destino" : self.lista_coordenadas[int(vuelo) - 1][self.lista_coordenadas[int(vuelo) - 1].index(coord_lat_destino) + coord_lat_destino.index(',') + 1:self.lista_coordenadas[int(vuelo) - 1].index(coord_long_destino) + coord_long_destino.index(',')],#-11],
                "Longitud de destino" : self.lista_coordenadas[int(vuelo) - 1][self.lista_coordenadas[int(vuelo) - 1].index(coord_long_destino) + coord_long_destino.index(',') + 1:-1]
            }

        return dicionarioCoordenadasVuelos    

    """
        Nos hace el proceso para poder hacer la solicitud a la API, es decir separa  las coordenadas y nos 
        genera los datos para imprimir        
    """
    def preguntaApi(self, diccionarioVuelos, indice):

        Cache = cache.Cache()
        Cache.archivo.seek(0)
        lineasCache = Cache.archivo.readlines()


        diccionarioCache1 = {}
        diccionarioCache2 = {}

        listaCoordenadas = entrada.listaCoordenadas

        iata1 = listaCoordenadas[indice][0:3]
        iata2 = listaCoordenadas[indice][4:7]
        lat_org = diccionarioVuelos[indice-1]["Latitud de origen"]
        long_org = diccionarioVuelos[indice-1]["Longitud de origen"]
        lat_des = diccionarioVuelos[indice-1]["Latitud de destino"]
        long_des = diccionarioVuelos[indice-1]["Longitud de destino"]

        if lineasCache.count(iata1) != 0:
        
            url_org = self.solicitarAPI(lat_org,long_org)

            diccionarioCache1[iata1] = url_org        

            with urlopen(url_org) as json_dicc_org:
                json_data_org = json_dicc_org.read()


            # Imprime el clima de la ciudad de origen (diccionario).
            clima_org = json.loads(json_data_org)
            #print(json.dumps(clima_org,indent = 2))
            #print(clima_org, "Seguro sosial")
        
        if lineasCache.count(iata2) != 0:
            # Llamada Api de ciudad de destino
            url_des = self.solicitarAPI(lat_des,long_des)
            
            diccionarioCache2[iata2] = url_des

            #print(lat_org + " --- " + long_org)
            #print(lat_des + " --- " + long_des)

            with urlopen(url_des) as json_dicc_des:
                json_data_des = json_dicc_des.read()

            # Imprime el clima de la ciudad de destino (diccionario).
            clima_des = json.loads(json_data_des)
            print(json.dumps(clima_des,indent = 2))
       
    
        # Clima de la ciudad de origen:
        print("- Clima de la ciudad de origen -\n    Condición actual : " + clima_org ['weather'][0]['main'] + "\n    Descripción : " + clima_org ['weather'][0]['description'] + "\n    Temperatura : " , clima_org ['main']['temp'] , "°C", "\n    Temperatura mínima : " , clima_org ['main']['temp_min'] , "°C","\n    Temperatura máxima : " , clima_org ['main']['temp_max'] , "°C","\n    Humedad (%) : " , clima_org ['main']['humidity'] , "\n    Velocidad del viento : " , clima_org ['wind']['speed'] , "\n    Nubes : " , clima_org ['clouds']['all'] , "\n    Nombre : " , clima_org ['name'] , "\n\n")

        # Clima de la ciudad de destino:
        print("- Clima de la ciudad de destino -\n    Condición actual : " + clima_des ['weather'][0]['main'] + "\n    Descripción : " + clima_des ['weather'][0]['description'] + "\n    Temperatura : " , clima_des ['main']['temp'] ,"°C","\n    Temperatura mínima : " , clima_des ['main']['temp_min'] , "°C","\n    Temperatura máxima : " , clima_des ['main']['temp_max'] , "°C","\n    Humedad (%) : " , clima_des ['main']['humidity'] , "\n    Velocidad del viento : " , clima_des ['wind']['speed'] , "\n    Nubes : " , clima_des ['clouds']['all'] , "\n    Nombre : " , clima_des ['name'])

        
        Cache.archivo.write(str(clima_org)+"\n") 
        Cache.archivo.write(str(clima_des)+"\n")
        
        Cache.archivo.seek(0)

        #lineasCache = Cache.archivo.readlines()

        print(lineasCache, len(lineasCache))


        #Cache.archivo.truncate(0)

        if lineasCache.count(clima_org) == 0:
            #haces una función para literal pedir eso            
            Cache.archivo.write("seguro")
        else:
            Cache.archivo.write("Subasta\n")

        keke = "Luis come caca"
        print(keke.count("c"), "perrre")
        print(True)
        Cache.archivo.seek(0)
        print(Cache.archivo.readlines())
        

        print("WE")

        Cache.cerrarCache()         

         
