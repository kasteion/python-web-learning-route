def run():
    for contador in range(20):
        if contador % 2 != 0:
            continue
        print(contador)

    for i in range(10000):
        if i == 5678:
            break
        print(i)
    
    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)

if __name__ == "__main__":
    run()