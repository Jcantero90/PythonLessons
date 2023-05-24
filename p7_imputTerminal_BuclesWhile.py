datosTerminal = input('Escribe esta variable a través de la terminal: ')

print(f'estos datos han sido escritos a traves de la termianl: {datosTerminal}')

datoParaCerrarBucle = True

while datoParaCerrarBucle:

    pregunta = input('Escribe "cerrar" para terminar el bucle: ')

    if pregunta == "cerrar":
        datoParaCerrarBucle = False
        print("bucle cerrado")

