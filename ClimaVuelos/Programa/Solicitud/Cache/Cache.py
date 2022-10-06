
class Cache:
    """
        Clase que nos representa el cache de la información del clima.
    """
    def __init__(self):
        """ Inicializa un objeto tipo caché y abre el documento donde será guardada la información """
        self.archivo = open("ClimaVuelos/Programa/Solicitud/Cache/Cache.txt","a+")

    
    def cerrarCache(self):
        """ Nos cierra el archivo donde se guardará el caché. """
        self.archivo.close()

    