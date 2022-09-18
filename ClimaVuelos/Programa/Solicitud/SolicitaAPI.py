import json
from urllib.request import urlopen

class SolicitaApi:

    def __init__(self, lista_coordenadas, indice_proporcionado):
        self.lista_coordenadas = lista_coordenadas
        self.indice_proporcionado = indice_proporcionado  
    
    def solicitarAPI(self):
        print("aaa")

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

    



