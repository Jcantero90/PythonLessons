class Agenda:

    def menu(self,opcion):

        if opcion == '1':
            self.addName(name= input("escribe el nombre"), age=input("escribe la edad"), address=input("escribe la direccion"))
        elif opcion == '2':
            print('opcion2')
        elif opcion == '3':
            print('opcion3')
        elif opcion == '4':
            print('opcion4')
        elif opcion == '5':
            print('opcion5')
        else:
            print("Error!")

    def opciones(self):
        print("Agregar usuario")
        print("Editar usuario")
        print("Ver usuarios agregados")
        print("Buscar usuarios")
        print("Eliminar usuario")

    def addName(self, name, age, address):
        contactos.write(name)
        contactos.write(age)
        contactos.write(address)





contactos = open("contactos.txt","w")
agenda = Agenda()
agenda.opciones()
opcion = input("Ingresa tu opción")
agenda.menu(opcion)