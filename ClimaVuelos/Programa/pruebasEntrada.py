import unittest
import Entrada.datosEntrada as entrada#Entrada.datosEntrada as entrada
class pruebasEntrada(unittest.TestCase):
    
    def test_archivoEntrada(self):
        assert len(entrada.ciudades_archivo_csv.readlines()) == 0, 'El archivo es vacío'
    
    def test_listaCoordenadas(self):
        assert len(entrada.listaCoordenadas) != 0, 'La lista donde tenemos los aeropuertos con las coordenadas es vacío'

    def test_diccionarioAeropuertos(self):
        diccionario = entrada.obtenerCiudades()
        self.assertNotEqual(diccionario.keys(), 0)

    def test_coordenadasDiccionario(self):
        ''' Nos verifica que las coordenadas que se guardaron en cada aeropuerto del diccionario sean puros números'''
        diccionario = entrada.obtenerCiudades()
        #listaAerop = entrada.listaCoordenadas
        self.assertNotEqual(diccionario.keys(), 0)
        #num = int("as12")

        
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()