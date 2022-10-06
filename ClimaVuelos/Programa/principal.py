import InterfazGrafica.interfazGrafica as interfaz
import Entrada.datosEntrada as entrada
from Solicitud.Cache.Cache import Cache
from Solicitud.SolicitaAPI import SolicitaApi 

""" Documento donde se hará la llamada a los demás métodos y correr el programa """

def corre():
    ''' Aquí es donde ejecutamos los métodos para que nuestro programa funcione '''
    Entrada = entrada.datosEntrada()

    ACache = Cache()

    coordenadas = Entrada.listaVuelos

    Solicitud = SolicitaApi(coordenadas)

    diccionarioCoordenadas = Solicitud.identificarCoordenadasVuelos()

    interfaz_grafica = interfaz.interfazGrafica(Entrada.listaAeropuertos, diccionarioCoordenadas)

    interfaz_grafica.desplega_ventana()
    
    ACache.cerrarCache()

    Entrada.cerrarListaDatos()

if __name__=='__main__':
    corre()
