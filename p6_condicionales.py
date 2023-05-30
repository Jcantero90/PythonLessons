#Son condicionales if else

numero = 1

if numero >= 2:
    print("numero es mayor o igual a 2")
else:
    print("balance es menor a 2")

#Con el not delante negamos la condición
if not numero == 1:
    print("no es igual a 1")
else:
    print("si es igual a 1")

#si es un booleano no necesitamos igualarlo
booleano = True

if booleano:
    print("es true")
else:
    print("es false")

#if anidados.

acceso_parcial = True
acceso_total = True

if acceso_parcial:
    print("tienes acceso parcial")
    if acceso_total:
        print("tienes acceso total")
else:
    print("no dispones de acceso")

#Else if
valorElseIf1 = 0
valorElseIf2 = 0

if valorElseIf1 == 0:
    print("primera validación correcta!")
elif valorElseIf2 == 0:
    print("Segunda validación correcta") #Recordar que si la primera validación es correcta, esta no se validará.
else:
    print("Ninguna validación es correcta")

#Condicionales And y Or

if valorElseIf1 == 0 and valorElseIf2 == 0:
    print("las dos validaciones son correctas")
else:
    print("las validaciones son incorrectas")

if not valorElseIf1 == 0 or valorElseIf2 == 0:
    print("una de las dos es correcta")
else:
    print("ninguna es correcta")

