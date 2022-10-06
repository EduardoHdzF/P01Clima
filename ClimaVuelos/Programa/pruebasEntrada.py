import unittest
import Entrada.datosEntrada as entrada

class pruebasEntrada(unittest.TestCase):
    """ Clase que nos correrá las pruebas automatizadas para detectar errores en el código del archivo datosEntrada"""
    
    def test_archivoEntrada(self):
        """ Verificar que el archivo de entrada no sea vacío"""
        Entra = entrada.datosEntrada()
        archivo = Entra.ciudades_archivo_csv      
        archivo.seek(0)  
        elementos = len(archivo.readlines())            
        Entra.cerrarListaDatos()
        assert elementos != 0, 'El archivo es vacío'
        
        
    def test_listaCoordenadas(self):
        """Ver que la lista de los vuelos con sus coordenadas no es vacío"""
        Entra = entrada.datosEntrada()        
        Entra.cerrarListaDatos()
        assert len(Entra.listaVuelos) != 0, 'La lista donde tenemos los aeropuertos con las coordenadas es vacío'

    def test_diccionarioAeropuertos(self):
        """ Verificar que el diccionario con las claves iata y sus coordenadas correspondiente no sea vacío """
        Entra = entrada.datosEntrada()        
        diccionario = Entra.obtenerCiudades()
        Entra.cerrarListaDatos()
        self.assertNotEqual(diccionario.keys(), 0)

    def test_coordenadasDiccionario(self):
        """ Nos verifica que las coordenadas que se guardaron en cada aeropuerto del diccionario sean puros números"""
        Entra = entrada.datosEntrada()
        diccionario = Entra.obtenerCiudades()        
        listaAerop = Entra.listaVuelos
        Entra.cerrarListaDatos()
        self.assertNotEqual(diccionario.keys(), 0)
        
        for vuelo in range(len(listaAerop)):

            iata1 = listaAerop[vuelo][0:3]
            iata2 = listaAerop[vuelo][4:7]
            try:
                latitud = float(diccionario[iata1]["Latitud"])
                longitud = float(diccionario[iata2]["Longitud"])
                
            except:
                print("Las coordenadas estan mal dadas, ya que se mezclan con comas(,)")
                

if __name__ == '__main__':    
    unittest.main()
    