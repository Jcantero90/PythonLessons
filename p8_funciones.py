# Creamos una clase con las funciones dentro
class FuncionEjemplo:

    def holaMundo(self, mensaje):  # Añadimos las funciones que deseemos, se ha de poner self obligatoriamente.
        print(mensaje)


funcion = FuncionEjemplo()  # Instanciamos el nombre de la clase
funcion.holaMundo("Hola mundo!")  # invocamos el método que se encuentra dentro de la clase.


# Ahora crearemos una clase con un constructor:
class FuncionConConstructor:

    def __init__(self): #el init se ejecuta si o si cuando ejecutamos un método de la clase.
        print("ejecución del init")

    def funcionConconstructor(self):
        print("estamos llamando al método")


funcionConConstructor = FuncionConConstructor()
funcionConConstructor.funcionConconstructor()

#Buenas prácticas. Normalmente se le asigna al constructor (__init__) todos los argumentos para su uso
class FuncionConConstructorYArgumentos:

    def __init__(self, argumento1, argumento2, argumento3):
        self.argumento1 = argumento1 #Declaramos aquí los ojbetos y sus argumentos.
        self.argumento2 = argumento2
        self.argumento3 = argumento3

    def exponiendoArgumentos(self): #Aquí esponemos los argumentos mostrándolos por pantalla.
        print(self.argumento1, self.argumento2, self.argumento3) #se exponen a través del self.argumento*

funcionConConstructorYArgumentos = FuncionConConstructorYArgumentos("este es el argumento 1", "este es el argumento 2", "este es el argumento 3")
funcionConConstructorYArgumentos.exponiendoArgumentos()
funcionConConstructorYArgumentos.argumento1 = "Nuevo Argumento 1" #se peuden cambiar los datos, esto NO ES encapsulamiento ni son buenas practicas.
funcionConConstructorYArgumentos.exponiendoArgumentos()

#Clases con argumentos PRIVADOS, no se pueden modificar a no ser de que esté la modificación en el propio método.
class FuncionArgumentosPrivados:
    def __init__(self, argumentoPublico, argumentoPrivado):
        self._argumentoPublico = argumentoPublico #un guión bajo significa que es un argumento público
        self.__argumentoPrivado = argumentoPrivado #dos guiones bajos significa que es un argumento privado.

    def mensaje(self):
        print(self._argumentoPublico, self.__argumentoPrivado)

funcionArgumentosPrivados = FuncionArgumentosPrivados("Argumento publico", "Argumento privado")
funcionArgumentosPrivados.mensaje()
funcionArgumentosPrivados._argumentoPublico = "estoy modificando el argumento público" #Este argumento SI se puede modificar
funcionArgumentosPrivados.__argumentoPrivado = "estoy intentando modificar el argumento privado" #No se puede modificar, ya que es privado.
funcionArgumentosPrivados.mensaje()
