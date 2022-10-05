import InterfazGrafica.interfazGrafica as interfaz
import Entrada.datosEntrada as entrada
from Solicitud.Cache.CreaCache import Cache
from Solicitud.SolicitaAPI import SolicitaApi 

""" Aquí es donde ejecutamos los métodos para que nuestro programa funcione """

Entrada = entrada.datosEntrada()

ACache = Cache()

coordenadas = Entrada.listaVuelos

Solicitud = SolicitaApi(coordenadas)

diccionarioCoordenadas = Solicitud.identificarCoordenadasVuelos()

interfaz_grafica = interfaz.interfazGrafica(Entrada.listaAeropuertos, diccionarioCoordenadas)

interfaz_grafica.desplega_ventana()

#diccionarioCiudades = Entrada.obtenerCiudades()

ACache.cerrarCache()

Entrada.cerrarListaDatos()
