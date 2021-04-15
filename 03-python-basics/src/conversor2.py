dolares = input("¿Cuántos dolares tienes?: ")
dolares = float(dolares)
valorDelDolar = 7.73
quetzales = str(round(dolares * valorDelDolar, 2))
print("Tienes Q", quetzales, "Quetzales")