import random

def generatePassword():
    mayusculas = [ "A", "B", "C", "D", "E", "F", "G"]
    minusculas = [ "a", "b", "c", "d", "e", "f", "g"]
    simbolos = [ "!", "#", "$", "&", "/", "(", ")"]
    numeros = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range(15):
        randomChar = random.choice(caracteres)
        password.append(randomChar)

    password = "".join(password)
    return password

def run():
    password = generatePassword()
    print("Tu nueva contraseña es: ", password)

if __name__ == "__main__":
    run()