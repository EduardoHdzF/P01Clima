import unittest
import Solicitud.SolicitaAPI as solicitud 
import Entrada.datosEntrada as entrada 

class pruebasSolicitaApi(unittest.TestCase):

    def test_solicita(self):
        """ Nos verifica que la base del enlace sea el correcto para hacer la petición """
        Entra = entrada.datosEntrada()
        Entra.cerrarListaDatos()
        soli = solicitud.SolicitaApi(Entra.listaVuelos)
        self.assertEqual(soli.enlace, "https://api.openweathermap.org/data/2.5/weather?lat=")

    def test_diccVuelos(self):
        """ Nos verifica que el diccionario de vuelos con las coordenadas no sea vacío """
        Entra = entrada.datosEntrada()
        Entra.cerrarListaDatos()        
        soli = solicitud.SolicitaApi(Entra.listaVuelos)
        vuelos = soli.identificarCoordenadasVuelos()
        assert len(vuelos.keys()) != 0, "Vuelos vacíos"

    def test_ID(self):
        ''' Verificar que tengamos llave, también nos lanza un error de que no se encontró el archivo de nuestra clave'''
        Entra = entrada.datosEntrada()
        Entra.cerrarListaDatos()        
        soli = solicitud.SolicitaApi(Entra.listaVuelos)
        ID = soli.obtenerId()        
        self.assertNotEqual(ID, ""), "No tenemos IDE"

if __name__ == '__main__':
    unittest.main()