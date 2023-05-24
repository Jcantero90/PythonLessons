# Una función es un trozo de código que ofrece una funcionalidad.

def holaMundo():
    print("hola Mundo desde una función!")  # muy importante respetar la tabulación


holaMundo()
holaMundo()
holaMundo()
holaMundo()


# Función con variables

def funcionVariables(variable):
    print(f'El siguiente exto es una variable: {variable}') #Muy importnate ponter la f para concatenar

funcionVariables("esto es un argumento!")

def funcionConUnParametroPorDefecto (parametro1, parametro2 = 'Esto es un parametro por defecto' ): #Si parametro2 está vacio, se colocará por defecto la cadena de String,
    print(parametro1, parametro2)                                                                   #pero si parametro 2 lleva info, se pondrá la info de algumento de llamada.

funcionConUnParametroPorDefecto("Esto es información") #Solo le estamos pasando un argumento, por ende, se verá por consola el valor por defecto que hemos asignado.

def funcionConReturn (num1, num2):
    num3 = num1 + num2
    return num3 #devuelve la suma de ambos números

print(funcionConReturn(1,2)) #devolverá un 3