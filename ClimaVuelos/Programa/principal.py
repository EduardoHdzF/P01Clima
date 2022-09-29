import InterfazGrafica.interfazGrafica as interfaz

import Entrada.datosEntrada as entrada
from Solicitud.Cache.CreaCache import Cache
from Solicitud.SolicitaAPI import SolicitaApi 
"""
    Documento en donde se ejecutará todo el programa, aquí es donde se 
    moverá el menú de opciones.
"""
"""
    Método que nos ayuda a que el usuario decida si desea salir del programa o no
    regresa un número que nos servirá más adelante para salir del programa.
"""
def finaliza():
    
    verif = False

    while not verif:

        try:

            termina = int(input("** Para regresar al menu de opciones presiona 1.\n** Para finalizar programa presiona 0.\n"))

            if termina == 0 or termina == 1:

                verif = True  
                

            else:

                print("ERROR : Solo se puede introducir valores 0 o 1")
                verif = False             

        except ValueError:
            print("ERROR : Solo se pueden introducir valores numéricos.")

    return termina

#Para manejar las excepciones.
'''
    La función manejor de errores nos ayuda a que cuando se elija un viaje, este exista dentro de la lista de
    disponibles, y si no, que nos desplegue un mensaje de que no eligió un valor aceptable.
    @param el número de ciudades que se tienen disponibles.
'''
def manejo_errores(canti_ciudades):
        
        verif = False

        while not verif:

            try:

                ciudad_selec = int(input("Escoge un viaje (revisa la lista):\n"))

                if ciudad_selec > 0 and ciudad_selec <= canti_ciudades:

                    verif = True   

                else:

                    print("ERROR : Solo se puede introducir valores entre 1 - " + str(canti_ciudades) + ".")
                    verif = False             

            except ValueError:
                print("ERROR : Solo se pueden introducir valores numéricos.")

        return ciudad_selec-1


"""
    Ciclo que nos ayudará a que el usuario pueda seguir consultando los diversos climas o no.
"""
terminado  = 1
while terminado == 1:
    print("--- CLIMA ---")

    ACache = Cache()
    #Cache.archivo.truncate(0)

    coordenadas = entrada.listaCoordenadas

    entrada.imprimeVuelos()

    indice_prop = manejo_errores(len(entrada.lista_ciudades))

    Clase = SolicitaApi(coordenadas ,indice_prop)

    diccionarioCoordenadas = Clase.identificarCoordenadasVuelos()

    #Clase.solicitarAPI()
    Clase.preguntaApi(diccionarioCoordenadas, indice_prop)
    
    interfaz_grafica = interfaz.interfazGrafica(entrada.lista_ciudades, diccionarioCoordenadas)

    interfaz_grafica.desplega_ventana()

    # El usuario decide si se finaliza el programa o no.
    terminado = finaliza()

    if terminado == 0:
        quit()

    #print(diccionarioCoordenadas)
    
    diccionarioCiudades = entrada.obtenerCiudades()

    #print(diccionarioCiudades)
    ACache.cerrarCache()
    entrada.ciudades_archivo_csv.close()