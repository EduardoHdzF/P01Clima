import json
from logging import shutdown
from urllib.request import urlopen

import Solicitud.Cache.CreaCache as cache
import Entrada.datosEntrada as entrada

import threading 
import time


class SolicitaApi:

    Prueba = ''
    clima_ciudad_origen = ''
    clima_ciudad_destino = ''   
    borra_cache = '' 

    enlace =  "https://api.openweathermap.org/data/2.5/weather?lat="    

    def __init__(self, lista_coordenadas, indice_proporcionado):  
        self.Prueba = open("ClimaVuelos/Programa/Solicitud/Cache/Cache.txt","r+")

        self.clima_ciudad_origen = ''
        self.clima_ciudad_destino = ''      
        self.lista_coordenadas = lista_coordenadas
        self.indice_proporcionado = indice_proporcionado          
        self.borra_cache = threading.Timer(20, self.borraCache)
    
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

        archivoID = open("ClimaVuelos/Programa/Clave/clave.txt")

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

            coord_lat_origen = self.lista_coordenadas[int(vuelo)][6:]
            coord_long_origen = self.lista_coordenadas[int(vuelo)][14:]
            coord_lat_destino = self.lista_coordenadas[int(vuelo)][22:]    
            coord_long_destino = self.lista_coordenadas[int(vuelo)][30:]

            dicionarioCoordenadasVuelos[vuelo] = {
                #"Latitud de origen" : self.lista_coordenadas[vuelo][self.lista_coordenadas[int(vuelo)].index(coord_lat_origen) + coord_lat_origen.index(',') + 1 : self.lista_coordenadas[int(vuelo)].index(coord_long_origen)+1],
                "Latitud de origen" : self.lista_coordenadas[vuelo][self.lista_coordenadas[int(vuelo)].index(coord_lat_origen) + coord_lat_origen.index(',') + 1 : self.lista_coordenadas[int(vuelo)].index(coord_long_origen)],
                #"Longitud de origen" : self.lista_coordenadas[int(vuelo)][self.lista_coordenadas[int(vuelo)].index(coord_long_origen) + coord_long_origen.index(',') + 1:self.lista_coordenadas[int(vuelo)].index(coord_lat_destino) + coord_lat_destino.index(',')],            
                "Longitud de origen" : self.lista_coordenadas[int(vuelo)][self.lista_coordenadas[int(vuelo)].index(coord_long_origen) + coord_long_origen.index(',') + 1:self.lista_coordenadas[int(vuelo)].index(coord_lat_destino) + 1],            
                #"Latitud de destino" : self.lista_coordenadas[int(vuelo)][self.lista_coordenadas[int(vuelo)].index(coord_lat_destino) + coord_lat_destino.index(',') + 1:self.lista_coordenadas[int(vuelo)].index(coord_long_destino) + coord_long_destino.index(',')],
                "Latitud de destino" : self.lista_coordenadas[int(vuelo)][self.lista_coordenadas[int(vuelo)].index(coord_lat_destino) + coord_lat_destino.index(',') + 1:-11],
                "Longitud de destino" : self.lista_coordenadas[int(vuelo)][self.lista_coordenadas[int(vuelo)].index(coord_long_destino) + coord_long_destino.index(',') + 1:-1]
            }

        return dicionarioCoordenadasVuelos        

    def borraCache(self):
            print('Listo')        
            self.Prueba.truncate(0)
            self.Prueba.close()

    def terminaHilo(self):
        print("Terminado")
        if self.borra_cache.is_alive():
            self.borra_cache.cancel()
            self.Prueba.truncate(0)
            self.Prueba.close()
        #time.sleep(0)
        #self.borra_cache.cancel()

    """
        Nos hace el proceso para poder hacer la solicitud a la API, es decir separa  las coordenadas y nos 
        genera los datos para imprimir        
    """
    def preguntaApi(self, diccionarioVuelos, indice):
        
        #Prueba = open("ClimaVuelos/Programa/Solicitud/Cache/Cache.txt","r+")

        Cache = cache.Cache()
        Cache.archivo.seek(0)
        lineasCache = Cache.archivo.readlines()
        
        #print("Prueba : " , Prueba.readline())

        if self.Prueba.readline() == '':            
            print("Pasooo")                
            self.borra_cache.start()  

        diccionarioCache1 = {}
        diccionarioCache2 = {}

        listaCoordenadas = entrada.listaCoordenadas

        iata1 = listaCoordenadas[indice][0:3]
        iata2 = listaCoordenadas[indice][4:7]
        lat_org = diccionarioVuelos[indice]["Latitud de origen"]
        long_org = diccionarioVuelos[indice]["Longitud de origen"]
        lat_des = diccionarioVuelos[indice]["Latitud de destino"]
        long_des = diccionarioVuelos[indice]["Longitud de destino"]
        print("Lista de coordenadas: \n", listaCoordenadas)
        print(iata1 , " +++ " , iata2)

        if lineasCache.count(iata1+"\n") == 0:
        
            url_org = self.solicitarAPI(lat_org,long_org)

            diccionarioCache1[iata1] = url_org        

            with urlopen(url_org) as json_dicc_org:
                json_data_org = json_dicc_org.read()


            # Imprime el clima de la ciudad de origen (diccionario).
            clima_org = json.loads(json_data_org)
            
            # Clima de la ciudad de origen:

            #climaCdOrigen = "- Clima de la ciudad de origen " + iata1 + " -\n    Condición actual : " + clima_org ['weather'][0]['main'] + "\n    Descripción : " + clima_org ['weather'][0]['description'] + "\n    Temperatura : " + str(clima_org ['main']['temp']) + "°C"+ "\n    Temperatura mínima : " + str(clima_org ['main']['temp_min']) + "°C" +"\n    Temperatura máxima : " + str(clima_org ['main']['temp_max']) + "°C"+"\n    Humedad (%) : " + str(clima_org ['main']['humidity']) + "\n    Velocidad del viento : " + str(clima_org ['wind']['speed'])+ "\n    Nubes : " + str(clima_org ['clouds']['all']) + "\n    Nombre : " + str(clima_org ['name']) + "\n\n"
            climaCdOrigen = "Nombre de la ciudad : " + str(clima_org ['name']) + "\n\n\n- Clima : " + clima_org ['weather'][0]['description'] + "\n- Temperatura : " + str(clima_org ['main']['temp']) + "°C"+ "\n    - Temperatura mínima : " + str(clima_org ['main']['temp_min']) + "°C" +"\n    - Temperatura máxima : " + str(clima_org ['main']['temp_max']) + "°C"+"\n- Humedad (%) : " + str(clima_org ['main']['humidity']) + "\n- Velocidad del viento : " + str(clima_org ['wind']['speed']) + "\n\n"
                        
            self.clima_ciudad_origen = climaCdOrigen
            print("1--------CO: " , self.clima_ciudad_origen)

            print(climaCdOrigen)
            Cache.archivo.write(iata1+"\n")
            Cache.archivo.write(climaCdOrigen)            

        else:
            
            indiceDeCiudad = lineasCache.index(iata1+"\n")+1
            #indiceDeCiudad = lineasCache.index(iata1+"\n")
            
            for linea in range(10):

                self.clima_ciudad_origen += str(lineasCache[indiceDeCiudad+linea])

                print(str(lineasCache[indiceDeCiudad+linea]))

            print("2--------CO: " , self.clima_ciudad_origen)
            
        if lineasCache.count(iata2+"\n") == 0:
            # Llamada Api de ciudad de destino
            url_des = self.solicitarAPI(lat_des,long_des)
            
            diccionarioCache2[iata2] = url_des

            with urlopen(url_des) as json_dicc_des:
                json_data_des = json_dicc_des.read()

            # Imprime el clima de la ciudad de destino (diccionario).
            clima_des = json.loads(json_data_des)
            
            # Clima de la ciudad de destino:

            #climaCdDestino = "- Clima de la ciudad de destino " + iata2 + " -\n    Condición actual : " + clima_des ['weather'][0]['main'] + "\n    Descripción : " + clima_des ['weather'][0]['description'] + "\n    Temperatura : " + str(clima_des ['main']['temp']) +"°C"+"\n    Temperatura mínima : " + str(clima_des ['main']['temp_min']) + "°C"+"\n    Temperatura máxima : " + str(clima_des ['main']['temp_max']) + "°C"+"\n    Humedad (%) : " + str(clima_des ['main']['humidity']) + "\n    Velocidad del viento : " + str(clima_des ['wind']['speed']) + "\n    Nubes : " + str(clima_des ['clouds']['all']) + "\n    Nombre : " + str(clima_des ['name'])+ "\n\n"
            climaCdDestino = "Nombre de la ciudad : " + str(clima_des ['name']) + "\n\n\n- Clima : " + clima_des ['weather'][0]['description'] + "\n- Temperatura : " + str(clima_des ['main']['temp']) + "°C"+ "\n    - Temperatura mínima : " + str(clima_des ['main']['temp_min']) + "°C" +"\n    - Temperatura máxima : " + str(clima_des ['main']['temp_max']) + "°C"+"\n- Humedad (%) : " + str(clima_des ['main']['humidity']) + "\n- Velocidad del viento : " + str(clima_des ['wind']['speed']) + "\n\n"

            self.clima_ciudad_destino = climaCdDestino 
            print("1--------CD: " , self.clima_ciudad_destino)

            print(climaCdDestino)
            Cache.archivo.write(iata2+"\n")
            Cache.archivo.write(str(climaCdDestino))                                           

        else:

            indiceDeCiudad = lineasCache.index(iata2+"\n")+1
            #indiceDeCiudad = lineasCache.index(iata2+"\n")
            for linea in range(10):

                self.clima_ciudad_destino += str(lineasCache[indiceDeCiudad+linea])

                print(str(lineasCache[indiceDeCiudad+linea]))
            
            print("2--------CD: " , self.clima_ciudad_destino)
        
        Cache.cerrarCache()        