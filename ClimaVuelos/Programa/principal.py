
import Entrada.datosEntrada as entrada

print(str(len(entrada.ArchivoEntrada.readlines()))+ "sss")

for iter in range(len(entrada.ArchivoEntrada.readlines())):
    
    print("a")
    print(entrada.ArchivoEntrada.readline())

for line in entrada.ArchivoEntrada:
    
    print("w")

