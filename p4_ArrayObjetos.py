#En python no existen los Arrays, pero si existe algo llamado "list"

meses = ["enero", "febrero", "marzo", "abril"]

print(meses[0]) #Se accede al igual que en los demás lenguajes.

meses.sort() #Ordena alfabeticamente la lista.
print(meses)

#setear Arrays
meses[0] = "Diciembre"
meses.append("Mayo") #Estamos seteando un valor al array
print(meses)

#Borrar de una lista un elemento
del meses[0]

meses.pop() #Borra el último
meses.pop(1) #Borra la posición especifica
meses.remove('marzo') #Borra el valor que yo le indique.

print(meses)

# Los objetos en python se llaman diccionarios. Se declaran con clave y valor

objetoDiccionario = {
    "objetoUno":"valor ObjetoUno",
    "objetoDos": "valor ObjetoDos",
    "objetoTres": "valor ObjetoTres",
}

print(objetoDiccionario.get("objetoUno")) #Acceder a un elemento
print(objetoDiccionario['objetoDos']) #otra forma de acceder a sus valores.
print(objetoDiccionario) #Acceder a todos los objetos.

#Agregar nuevos valores

objetoDiccionario["objetoCuatro"] = "valor ObjetoCuatro" #Hemos añadido un nuevo valor.
print(objetoDiccionario)

#Borrar nuevos valores

del objetoDiccionario["objetoCuatro"]
print(objetoDiccionario)
