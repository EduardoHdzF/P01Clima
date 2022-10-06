import json
from urllib.request import urlopen
import Solicitud.Cache.Cache as cache
import Entrada.datosEntrada as entrada
from cryptography.fernet import Fernet

class SolicitaApi:
    
    """ Nos representa una solicitud a la API.
        Atributos: 
            enlace(str): La base del link necesario para hacer la petición.
            clima_ciudad_origen (str): El clima del sitio de origen de cada petición que se haga.
            clima_ciudad_destino (str): El clima del sitio de destino de cada petición que se haga.
    """

    clima_ciudad_origen = ''
    clima_ciudad_destino = ''   
    enlace =  "https://api.openweathermap.org/data/2.5/weather?lat="    

    def __init__(self, lista_coordenadas): 
        """ Inicializa el objeto tipo SolicitaApi
            Argumentos: 
                listadeVuelos(List)
        """
        self.lista_coordenadas = lista_coordenadas
        self.terminado = False          
    
    def solicitarAPI(self,latitud, longitud):            
        """
            Nos hace la llamada en la API de la ciudad dada con las coordenadas proporcionadas
            como parámetros
            Args:
                latitud(str)
                longitud(str)
        """
        url_modif_org = self.enlace + str(latitud) + "&lon=" + str(longitud) + "&units=metric" +"&appid="+ self.obtenerId()
        return url_modif_org

    
    def obtenerId(self):
        """
            Nos devuelve la clave de la API para que podamos hacer la llamada.
            Esta clave se encuentra en el archivo encriptada, de tal manera que podamos desencriptar y leer.
        """ 
        with open('ClimaVuelos/Programa/Clave/llave.txt','rb') as arch_llave:
            llave = arch_llave.read()

        fernet = Fernet(llave)

        with open("ClimaVuelos/Programa/Clave/clave.txt", 'rb') as arch_encrip:
            encrip = arch_encrip.read()
        
        desencriptado = fernet.decrypt(encrip)

        return desencriptado.decode('utf-8')

   
    def identificarCoordenadasVuelos(self):                    
        """
            Nos devuelve un diccionario con los datos de los vuelos, es decir sus 
            claves correspondientes de origen y destino, así como sus coordenadas.
            Regresa: un diccionario con los datos.
        """
        dicionarioCoordenadasVuelos = {}

        for vuelo in range(len(self.lista_coordenadas)):

            coord_lat_origen = self.lista_coordenadas[int(vuelo)][6:]
            coord_long_origen = self.lista_coordenadas[int(vuelo)][14:]
            coord_lat_destino = self.lista_coordenadas[int(vuelo)][22:]    
            coord_long_destino = self.lista_coordenadas[int(vuelo)][30:]

            dicionarioCoordenadasVuelos[vuelo] = {
                "Latitud de origen" : self.lista_coordenadas[vuelo][self.lista_coordenadas[int(vuelo)].index(coord_lat_origen) + coord_lat_origen.index(',') + 1 : self.lista_coordenadas[int(vuelo)].index(coord_long_origen)],
                "Longitud de origen" : self.lista_coordenadas[int(vuelo)][self.lista_coordenadas[int(vuelo)].index(coord_long_origen) + coord_long_origen.index(',') + 1:self.lista_coordenadas[int(vuelo)].index(coord_lat_destino) + 1],            
                "Latitud de destino" : self.lista_coordenadas[int(vuelo)][self.lista_coordenadas[int(vuelo)].index(coord_lat_destino) + coord_lat_destino.index(',') + 1:-11],
                "Longitud de destino" : self.lista_coordenadas[int(vuelo)][self.lista_coordenadas[int(vuelo)].index(coord_long_destino) + coord_long_destino.index(',') + 1:-1]
            }

        return dicionarioCoordenadasVuelos                        

    
    def preguntaApi(self, diccionarioVuelos, indice):
        """
            Nos hace el proceso para poder hacer la solicitud a la API, es decir separa  las coordenadas y nos 
            genera los datos para mostrar al usuario.
        """
        Cache = cache.Cache()
        Cache.archivo.seek(0)
        lineasCache = Cache.archivo.readlines()
        
        diccionarioCache1 = {}
        diccionarioCache2 = {}
        Entrada = entrada.datosEntrada()
        listaCoordenadas = Entrada.listaVuelos

        iata1 = listaCoordenadas[indice][0:3]
        iata2 = listaCoordenadas[indice][4:7]
        lat_org = diccionarioVuelos[indice]["Latitud de origen"]
        long_org = diccionarioVuelos[indice]["Longitud de origen"]
        lat_des = diccionarioVuelos[indice]["Latitud de destino"]
        long_des = diccionarioVuelos[indice]["Longitud de destino"]

        
        if lineasCache.count(iata1+"\n") == 0:

           self.guardarJson(lat_org, long_org, diccionarioCache1, iata1,1)

        else:
            
            indiceDeCiudad = lineasCache.index(iata1+"\n")+1            
            for linea in range(10):

                self.clima_ciudad_origen += str(lineasCache[indiceDeCiudad+linea])
            
        if lineasCache.count(iata2+"\n") == 0:

          self.guardarJson(lat_des, long_des, diccionarioCache2, iata2,2)

        else:

            indiceDeCiudad = lineasCache.index(iata2+"\n")+1

            for linea in range(10):

                self.clima_ciudad_destino += str(lineasCache[indiceDeCiudad+linea])                           

        Cache.cerrarCache()          
    
    def guardarJson(self, latitud, longitud, diccionario, iata, num):
        """ 
            Nos ayuda a guardar la información obtenida por la llamada en el caché para utilizarla después. 
            Argumentos:
                latitud(str)
                longitud(str)
                diccionario(dict)
                iata(str)
                num(int)
        """

        Cache = cache.Cache()
        Cache.archivo.seek(0)
        
        url = self.solicitarAPI(latitud,longitud)

        diccionario[iata] = url

        with urlopen(url) as json_dicc:
            json_data = json_dicc.read()

        clima = json.loads(json_data)
        
        climaCd = "Nombre de la ciudad : " + str(clima ['name']) + "\n\n\n- Clima : " + clima ['weather'][0]['description'] + "\n- Temperatura : " + str(clima ['main']['temp']) + "°C"+ "\n    - Temperatura mínima : " + str(clima ['main']['temp_min']) + "°C" +"\n    - Temperatura máxima : " + str(clima ['main']['temp_max']) + "°C"+"\n- Humedad (%) : " + str(clima ['main']['humidity']) + "\n- Velocidad del viento : " + str(clima ['wind']['speed']) + "\n\n"
        if(num == 1):
            self.clima_ciudad_origen = climaCd
        else:
            self.clima_ciudad_destino = climaCd

        Cache.archivo.write(iata+"\n")
        Cache.archivo.write(climaCd) 
        
