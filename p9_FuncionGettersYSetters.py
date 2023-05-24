# Clase con getters y setters
class Funcion:
    def __init__(self, argumento1):
        self.__argumento1 = argumento1 #El argumento es privado.

    def get_rgumento1(self):
        return self.__argumento1 #Con esta funcion conseguimos el argumento

    def set_argumento1(self, data): #Con esta le seteamos valores.
        self.__argumento1 = data

function = Funcion("valor predeterminado")
print(function.get_rgumento1())
function.set_argumento1("Modificando el valor predeterminado")
print(function.get_rgumento1())

#Vamos a heredar los datos de la clase anterior en la nueva clase:
class ClaseHeredada(Funcion): #Agregamos el nombre de la función de la cual queremos heredar.
    def __init__(self,argumento1):
        super().__init__(argumento1) #con la sentencia super le indicamos que estamos heredando del init de la clase anterior.

claseHeredada = ClaseHeredada("Valor por defecto")
claseHeredada.set_argumento1("Estoy modificando un valor")
print(claseHeredada.get_rgumento1())

#Polimorfismo (heredar una clase y asignar nuevos atributos y funcionalidades a tu clase antigua a través de la clase nueva).
class Polimorfismo(Funcion):
    def __init__(self, argumento1, argumentoPolimorfico):
        super().__init__(argumento1)
        self.argumentoPolimorfico = argumentoPolimorfico

    def mostrarTodoPolimorfismo(self):
        print(f'{self.argumentoPolimorfico} y así fue como salvé la navidad {self.get_rgumento1()}')

polimorfismo = Polimorfismo("este mensaje es el argumento1", "y este es el mensaje polimorfico")
polimorfismo.mostrarTodoPolimorfismo()