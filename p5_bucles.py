#Se hace diference, primero se crea una variable y luego se pone el iterador.

lista = ["uno", "dos", "tres", "cuatro", "cinco"]

for numeros in lista:
    print(numeros) #la variable numero coje cada elemento del array y lo va a mostrar por pantalla

for variable in range(0,10): #esto sustituye al x++
    print(f'Lista sin incrementos {variable}')

for variable in range(0,10,3): #aqui especificamos que habrá incrementos de 3 en 3.
    print(f'Lista con incrementos de 3 en 3 {variable}')