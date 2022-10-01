"""
    Clase que nos abre el archivo del caché
"""
class Cache:

    def __init__(self):
    
        self.archivo = open("ClimaVuelos/Programa/Solicitud/Cache/Cache.txt","a+")

    """
        Nos cierra el archivo donde se guardará el caché
    """
    def cerrarCache(self):
        self.archivo.close()

    