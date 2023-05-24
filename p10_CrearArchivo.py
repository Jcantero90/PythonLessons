def crearYEscribirArchivo():

    archivo = open("Archivo.txt", "w") #Esta función creará un archivo en el directorio raiz.
    archivo.write("Estoy escribiendo datos en un archivo") #son los datos que vamos a escribir en el archivo. 
    archivo.close() #cierra el archivo.

crearYEscribirArchivo()