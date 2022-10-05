'''
    Para que pueda ejecutarse correctamente el programa, debemos ejecutarlo desde la
    carpeta P01Clima
    En este archivo de lee la lista de datos, de igual manera tiene la función de enlistar cada ciudad existente en los
    vuelos, también nos hace una lista de las coordenadas de origen y destino de los vuelos distinguibles que 
    existen en la lista dada.
'''
class datosEntrada:
    """ Representa los datos dados como entrada. """

    def __init__(self):
        """ Incializa el objeto de tipo datosEntrada."""

        self.ciudades_archivo_csv = open('ClimaVuelos/Programa/Entrada/dataset1.csv', 'r+')
        self.listaVuelos = self.obtenerListaVuelos()
        self.listaAeropuertos = self.listaCiudades()

    def obtenerListaVuelos(self):

        """ Nos regresa una lista con los distintos vuelos(sin repeticiones) que existen en todo el archivo de entrada.
            Regresa: una lista.
        """

        listaCoordenadas = []

        for iter in range(len(self.ciudades_archivo_csv.readlines())):
            
            if iter == 0:
                self.ciudades_archivo_csv.seek(0)
                self.ciudades_archivo_csv.readline()
                listaCoordenadas.append(self.ciudades_archivo_csv.readline())
                
            elif iter > 1:                    
                self.ciudades_archivo_csv.seek(0)

                if listaCoordenadas.count(self.ciudades_archivo_csv.readlines()[iter]) == 0:                                                
                    self.ciudades_archivo_csv.seek(0)
                    listaCoordenadas.append(self.ciudades_archivo_csv.readlines()[iter])                                
                    self.ciudades_archivo_csv.seek(0)   

        listaCoordenadas.sort()
        return listaCoordenadas


    def listaCiudades(self):
        """ Nos regresa una lista con las claves iata del origen y destino de cada vuelo.
            Regresa: una lista.
        """
                
        lista_ciudades = []
        lista_coordenadas = self.listaVuelos
        for iter in range(len(lista_coordenadas)):
            
            ciudades_org_des = [lista_coordenadas[iter][0:3] , lista_coordenadas[iter][4:7]]
            lista_ciudades.append(ciudades_org_des)

        return lista_ciudades

    
    def obtenerCiudades(self):
        """
            Nos crea un diccionario con las distintas ciudades que están en los vuelos con sus coordenadas.            
            Regresa: un diccionario.
        """
        print("Hola")
        listaCiudades = {}       
        listaCoordenadas = self.listaVuelos

        for vuelo in range(len(listaCoordenadas)):
            
            iata1 = listaCoordenadas[vuelo][0:3]
            iata2 = listaCoordenadas[vuelo][4:7]

            coord_lat_origen = listaCoordenadas[int(vuelo)][6:]
            coord_long_origen = listaCoordenadas[int(vuelo)][14:]
            coord_lat_destino = listaCoordenadas[int(vuelo)][22:]    
            coord_long_destino =listaCoordenadas[int(vuelo)][30:]

            listaCiudades[iata1] = {

                "Latitud" : listaCoordenadas[vuelo][listaCoordenadas[int(vuelo)].index(coord_lat_origen) + coord_lat_origen.index(',') + 1 : listaCoordenadas[int(vuelo)].index(coord_long_origen)],
                "Longitud" : listaCoordenadas[int(vuelo)][listaCoordenadas[int(vuelo)].index(coord_long_origen) + coord_long_origen.index(',') + 1:listaCoordenadas[int(vuelo)].index(coord_lat_destino) + 1],            
            }
            listaCiudades[iata2] = {


                "Latitud" : listaCoordenadas[int(vuelo)][listaCoordenadas[int(vuelo)].index(coord_lat_destino) + coord_lat_destino.index(',') + 1:-11],
                "Longitud" : listaCoordenadas[int(vuelo)][listaCoordenadas[int(vuelo)].index(coord_long_destino) + coord_long_destino.index(',') + 1:-1]    
            }

        return listaCiudades

    def cerrarListaDatos(self):
        """ Cierra el archivo dado como entrada. """
        self.ciudades_archivo_csv.close()


