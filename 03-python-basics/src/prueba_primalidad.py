def esPrimo(numero):
    if numero == 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def run():
    # numero = int(input("Escribe un numero: "))
    for i in range(1001):
        if esPrimo(i):
            print(i)

if __name__ == "__main__":
    run()