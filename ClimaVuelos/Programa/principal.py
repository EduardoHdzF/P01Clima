import InterfazGrafica.interfazGrafica as interfaz
import Entrada.datosEntrada as entrada
from Solicitud.Cache.CreaCache import Cache
from Solicitud.SolicitaAPI import SolicitaApi 

ACache = Cache()

coordenadas = entrada.listaCoordenadas

Clase = SolicitaApi(coordenadas)

diccionarioCoordenadas = Clase.identificarCoordenadasVuelos()

interfaz_grafica = interfaz.interfazGrafica(entrada.lista_ciudades, diccionarioCoordenadas)

interfaz_grafica.desplega_ventana()

diccionarioCiudades = entrada.obtenerCiudades()

ACache.cerrarCache()

entrada.ciudades_archivo_csv.close()
