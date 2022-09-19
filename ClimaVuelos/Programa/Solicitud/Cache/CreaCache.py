
class Cache:

    def __init__(self):
        self.archivo = open("ClimaVuelos\Programa\Solicitud\Cache\Cache.txt","a+")
       
    def cerrarCache(self):
        self.archivo.close()

    