import json
from urllib.request import urlopen

import Solicitud.Cache.CreaCache as cache

class SolicitaApi:

    enlace =  "https://api.openweathermap.org/data/2.5/weather?lat="    

    def __init__(self, lista_coordenadas, indice_proporcionado):
        self.lista_coordenadas = lista_coordenadas
        self.indice_proporcionado = indice_proporcionado  
    

    def solicitarAPI(self,latitud, longitud):
        print("aaa")
        # Llamada Api de ciudad de origen
        url_modif_org = self.enlace + str(latitud) + "&lon=" + str(longitud) + "&units=metric" +"&appid="+ self.obtenerId()
        return url_modif_org

    def obtenerId(self):
        archivoID = open("ClimaVuelos\Programa\Clave\clave.txt")
        clave = archivoID.readline()
        archivoID.close()
        return clave

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

    def preguntaApi(self, diccionarioVuelos, indice):

        Cache = cache.Cache()
        
        lat_org = diccionarioVuelos[indice-1]["Latitud de origen"]
        long_org = diccionarioVuelos[indice-1]["Longitud de origen"]
        lat_des = diccionarioVuelos[indice-1]["Latitud de destino"]
        long_des = diccionarioVuelos[indice-1]["Longitud de destino"]
        
        url_org = self.solicitarAPI(lat_org,long_des)

        with urlopen(url_org) as json_dicc_org:
            json_data_org = json_dicc_org.read()

        # Imprime el clima de la ciudad de origen (diccionario).
        clima_org = json.loads(json_data_org)
        print(json.dumps(clima_org,indent = 2))
        print(clima_org, "Seguro sosial")
        
        # Llamada Api de ciudad de destino
        url_des = self.solicitarAPI(lat_des,long_des)

        print(lat_org + " --- " + long_org)
        print(lat_des + " --- " + long_des)
        with urlopen(url_des) as json_dicc_des:
            json_data_des = json_dicc_des.read()

        # Imprime el clima de la ciudad de destino (diccionario).
        clima_des = json.loads(json_data_des)
        print(json.dumps(clima_des,indent = 2))
       
    
        # Clima de la ciudad de origen:
        print("- Clima de la ciudad de origen -\n    Condición actual : " + clima_org ['weather'][0]['main'] + "\n    Descripción : " + clima_org ['weather'][0]['description'] + "\n    Temperatura : " , clima_org ['main']['temp'] , "°C", "\n    Temperatura mínima : " , clima_org ['main']['temp_min'] , "°C","\n    Temperatura máxima : " , clima_org ['main']['temp_max'] , "°C","\n    Humedad (%) : " , clima_org ['main']['humidity'] , "\n    Velocidad del viento : " , clima_org ['wind']['speed'] , "\n    Nubes : " , clima_org ['clouds']['all'] , "\n    Nombre : " , clima_org ['name'] , "\n\n")

        # Clima de la ciudad de destino:
        print("- Clima de la ciudad de destino -\n    Condición actual : " + clima_des ['weather'][0]['main'] + "\n    Descripción : " + clima_des ['weather'][0]['description'] + "\n    Temperatura : " , clima_des ['main']['temp'] ,"°C","\n    Temperatura mínima : " , clima_des ['main']['temp_min'] , "°C","\n    Temperatura máxima : " , clima_des ['main']['temp_max'] , "°C","\n    Humedad (%) : " , clima_des ['main']['humidity'] , "\n    Velocidad del viento : " , clima_des ['wind']['speed'] , "\n    Nubes : " , clima_des ['clouds']['all'] , "\n    Nombre : " , clima_des ['name'])

        #diccionario_guardar["Ciudad"][lista_coordenadas[int(indice_prop) - 1][0:3]] = { "Nombre" : clima_org ['name'] , "Clima" : clima_org['weather'][0]['main'] , "Descripcion" : clima_org ['weather'][0]['description'] , "Temperatura" : clima_org ['main']['temp'] , "Temperatura minima" : clima_org ['main']['temp_min'] , "Temperatura maxima" : clima_org ['main']['temp_max'] , "Humedad" : clima_org ['main']['humidity'] , "Velocidad del viento" : clima_org ['wind']['speed'] , "Nubes" : clima_org ['clouds']['all']}

        #diccionario_guardar["Ciudad"][lista_coordenadas[int(indice_prop) - 1][4:7]] = { "Nombre" : clima_des ['name'] , "Clima" : clima_des['weather'][0]['main'] , "Descripcion" : clima_des ['weather'][0]['description'] , "Temperatura" : clima_des ['main']['temp'] , "Temperatura minima" : clima_des ['main']['temp_min'] , "Temperatura maxima" : clima_des ['main']['temp_max'] , "Humedad" : clima_des ['main']['humidity'] , "Velocidad del viento" : clima_des ['wind']['speed'] , "Nubes" : clima_des ['clouds']['all']}
        
        
        
        Cache.archivo.write(str(clima_org)+"\n") 
        Cache.archivo.write(str(clima_des)+"\n")
        
        Cache.archivo.seek(0)

        lineasCache = Cache.archivo.readlines()

        print(lineasCache, len(lineasCache))


        #Cache.archivo.truncate(0)

        if lineasCache.count(clima_org):
            #haces una función para literal pedir eso            
            Cache.archivo.write("seguro")
        else:
            Cache.archivo.write("Subasta\n")

        keke = "Luis"
        print(keke.count("Lu"), "perrre")
        print(True)
        Cache.archivo.seek(0)
        print(Cache.archivo.readlines())
        

        print("WE")

        Cache.cerrarCache()         

         
