'''Para que pueda ejecutarse correctamente el programa, debemos ejecutarlo desde la
    carpeta P01Clima
'''

with open('ClimaVuelos\Programa\Entrada\dataset1.csv', 'r+') as ArchivoEntrada:

#ArchivoEntrada = open('ClimaVuelos\Programa\Entrada\dataset1.csv', 'r+')
    print(type(ArchivoEntrada))

    #print(ArchivoEntrada.readline())
    Lista = []

    for linea in range(len(ArchivoEntrada.readlines())):#ArchivoEntrada:
        ArchivoEntrada.seek(0)
        print(ArchivoEntrada.readline())
        print(ArchivoEntrada.readline())    
        Lista.append(ArchivoEntrada.readline())

    #print(ArchivoEntrada.readlines())
    print(Lista)