def run():
    LIMIT = 10000
    count = 0
    potencia = 0
    while (potencia <= LIMIT):
        potencia = 2**count
        if potencia <= LIMIT:
            print("2^"+str(count), "=", potencia)
        count += 1

    a = range(1000)
    print(a)
    a = list(range(1, 1001))
    print(a)

    for i in range(1, 11):
        print(i)

if __name__ == "__main__":
    run()