import Entrada.datosEntrada as entrada
from Solicitud.SolicitaAPI import SolicitaApi 

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

                ciudad_selec = int(input("Escoge un viaje:"))

                if ciudad_selec > 0 and ciudad_selec <= canti_ciudades:

                    verif = True   

                else:

                    print("ERROR : Solo se puede introducir valores entre 1 - " + str(canti_ciudades) + ".")
                    verif = False             

            except ValueError:
                print("ERROR : Solo se pueden introducir valores numéricos.")

        return ciudad_selec

print("w")

terminado  = 1
while terminado == 1:
    print("--- CLIMA ---")           
    coordenadas = entrada.listaCoordenadas
    indice_prop = manejo_errores(len(entrada.lista_ciudades))
    Clase = SolicitaApi(coordenadas ,indice_prop)
    diccionarioCoordenadas = Clase.identificarCoordenadasVuelos()
    Clase.solicitarAPI()
    Clase.preguntaApi(diccionarioCoordenadas, indice_prop)

    # El usuario decide si se finaliza el programa o no.
    terminado = finaliza()
    
   
    
    #print(diccionarioCoordenadas)
    diccionarioCiudades = entrada.obtenerCiudades()
    print(diccionarioCiudades)
    entrada.ciudades_archivo_csv.close()