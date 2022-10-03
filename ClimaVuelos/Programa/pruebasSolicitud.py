import unittest
import Solicitud.SolicitaAPI as solicitud
import Entrada.datosEntrada as entrada

class pruebasSolicitaApi(unittest.TestCase):

    def test_solicita(self):
        soli = solicitud.SolicitaApi(entrada.listaCoordenadas, 1)
        self.assertEqual(soli.enlace, "https://api.openweathermap.org/data/2.5/weather?lat=")

    def test_diccVuelos(self):
        soli = solicitud.SolicitaApi(entrada.listaCoordenadas, 1)
        vuelos = soli.identificarCoordenadasVuelos()
        assert len(vuelos.keys()) != 0, "Vuelos vacíos"

    def test_ID(self):
        ''' También nos lanza un error de que no se encontró el archivo de nuestra clave'''
        soli = solicitud.SolicitaApi(entrada.listaCoordenadas, 1)
        ID = soli.obtenerId()
        self.assertNotEqual(ID, ""), "No tenemos IDE"

if __name__ == '__main__':
    unittest.main()