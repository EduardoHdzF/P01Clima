import InterfazGrafica.interfazGrafica as interfaz
import Entrada.datosEntrada as entrada
from Solicitud.Cache.CreaCache import Cache
from Solicitud.SolicitaAPI import SolicitaApi 

Entrada = entrada.datosEntrada()

ACache = Cache()

coordenadas = Entrada.listaVuelos

Clase = SolicitaApi(coordenadas)

diccionarioCoordenadas = Clase.identificarCoordenadasVuelos()

interfaz_grafica = interfaz.interfazGrafica(Entrada.listaAeropuertos, diccionarioCoordenadas)

interfaz_grafica.desplega_ventana()

diccionarioCiudades = Entrada.listaAeropuertos

ACache.cerrarCache()

Entrada.cerrarListaDatos()
