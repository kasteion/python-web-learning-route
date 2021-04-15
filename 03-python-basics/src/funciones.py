def imprimirMensaje():
    print("Mensaje Especial: ")
    print("¡Estoy aprendiendo a usar funciones!")

def conversacion(opcion):
    print("Hola")
    print("¿Cómo estás?, elegiste la opción ", opcion)
    print("Adiós")

for x in range(3):
    imprimirMensaje()

opcion = input("Elige una opcione (1,2,3): ")


if opcion == "1" or opcion == "2" or opcion=="3":
    conversacion(opcion)
else:
    print("Elige la opción correcta... 😒")

def suma(a, b):
    print("Se suman dos números")
    return a + b

resultado = suma(1, 4)
print("El resultado de ", 1, "+", 4, "es:", resultado)