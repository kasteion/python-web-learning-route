def convertirMoneda(nombreMoneda, valorDolar):
    moneda = float(input("¿Cuántos " + nombreMoneda + " tienes?: "))
    dolares = round(moneda / valorDolar, 2)
    return dolares


menu = """
💰 Bienvenido al conversor de monedas 💰

1. Quetzales 
2. Pesos Mexicanos
3. Pesos colombianos

Elige una opción: """

opcion = input(menu)

if opcion == "1":
    print("Tienes $", convertirMoneda("quetzales", 7.72), "dolares")
elif opcion == "2":
    print("Tienes $", convertirMoneda("pesos mexicanos", 20.06), "dolares")
elif opcion == "3":
    print("Tienes $", convertirMoneda("pesos colombianos", 3656.80), "dolares")
else:
    print("Elige una opcicón correcta, por favor... 😒")