'''Para que pueda ejecutarse correctamente el programa, debemos ejecutarlo desde la
    carpeta P01Clima
'''

with open('ClimaVuelos\Programa\Entrada\dataset1.csv', 'r+') as ArchivoEntrada:

#ArchivoEntrada = open('ClimaVuelos\Programa\Entrada\dataset1.csv', 'r+')
    print(type(ArchivoEntrada))

    print(ArchivoEntrada.readline())

    for linea in ArchivoEntrada:
        print(linea)

    print(ArchivoEntrada.readlines())
