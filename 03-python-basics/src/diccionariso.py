def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    print(mi_diccionario)
    print(mi_diccionario["llave1"])
    print(mi_diccionario["llave2"])
    print(mi_diccionario["llave3"])

    poblacion_pais = {
        "Argentina": 44937612,
        "Brasil": 210147125,
        "Colombia": 50372424
    }
    print(poblacion_pais["Argentina"])
    print(poblacion_pais["Brasil"])
    print(poblacion_pais["Colombia"])

    for pais in poblacion_pais.keys():
        print(pais)

    for poblacion in poblacion_pais.values():
        print(poblacion)
    
    for pais, poblacion in poblacion_pais.items():
        print(pais, "tiene", poblacion, "habitantes")

if __name__ == "__main__":
    run()