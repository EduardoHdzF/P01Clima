import Entrada.datosEntrada as entrada
from Solicitud.SolicitaAPI import SolicitaApi 

'''
print("w")

Hola = "perro"
print(Hola[0:2])
print("frencisco")
'''
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

print("w")

terminado  = 1
while terminado == 1:
    print("--- CLIMA ---")
    
     # Para manejar las excepciones.
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

    indice_prop = manejo_errores(len(entrada.lista_ciudades))

    # El usuario decide si se finaliza el programa o no.
    terminado = finaliza()
    coordenadas = entrada.listaCoordenadas
    Clase = SolicitaApi(coordenadas ,indice_prop)
    Clase.solicitarAPI()
    diccionarioCoordenadas = Clase.identificarCoordenadas()
    print(diccionarioCoordenadas)
    entrada.ciudades_archivo_csv.close()