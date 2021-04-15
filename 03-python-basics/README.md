# Introducción a la programación con Python

## El arte de la programación

Python tiene una forma de escribirse muy elegante y simple. Además la programación está en todos lados.

## ¿Por qué Python?

En tecnología existen muchísimos lenguajes de programación. Además de Python podemos aprender... javascript, java, ruby, php, go, etc. En lugar de preguntarnos que lenguaje queremos aprender deberíamos preguntarnos que queremos lograr.

Frontend, IOT, Inteligencia Artificial, Backend, DevOps, Data Science, Videojuegos, Desarrollo móvil.

Python funciona bien en estos campos: IOT, Inteligencia Artificial, Backend, Data Science.

**Ventajas**

- Nos ayuda a fortalecer las buenas prácticas
- Es fácil de aprender, es muy paralelo al idioma ingles.
- Es elegante, necesita de una estructura definida para poder trabajar de forma correcta.

## El núcleo de un programa: los algoritmos

Un algoritmo es una serie de pasos para resolver un problema. No podemos tener pasos infinitos, así que debe ser finito. Debemos tener claro cuando termina el algoritmo (o que termina). Además un algoritmo no es ambiguo, no podemos tener algo que signifique algo en un contexto sigunifique una cosa y en otro contexto significa algo diferente.

## Instalación de nuestras herramientas

Herramientas necesarias...

1. Editor de código:
   - VS Code
   - Otras opciones: PyCharm.
2. La todopoderosa terminal
   - En windows cmder
3. Python... Obviamente.

## Instalación de nuestras herramientas en Mac

En Mac no se necesita instalar una consola. Ya está instalada. Pero si necesitamos ejecutar lo siguiente desde la terminal:

> sudo xcode-select --install
>
> sudo xcode-select --reset

Se instala VS Code desde el sitio de vs code https://code.visualstudio.com y en Mac también es necesario instalar Python 3: https://www.python.org/downloads/

## Instalación de nuestras herramientas en Ubuntu

1. En Linux ya hay terminal... siguiente.
2. Para instalar vscode pues se puede descargando el archivo .deb de la página de vscode.
3. Y python:

> sudo apt upgrade
>
> sudo apt install python3-pip
>
> python3 -v

## Tu mejor herramienta: la consola

1. Se puede utilizar Ctrl+l para limpiar la pantalla.
2. cd para cambiar de directorios. . es el directorio actual, .. es el directorio superior.
3. ls para listar el directorio.
4. mkdir para crear directorio
5. touch para crear archivos

# Conceptos básicos de Python

## Explorando Python: operadores aritméticos

- es para sumar, - es para restar, \* es para multiplicar, / para dividir...

// es para división entera (división euclidiana)
`**` es para potencia

```python
import math
math.sqrt(25)
```

## ¿Qué es una variable?

Una variable es un símbolo constituyente de un predicado, formula, algoritmo o proposición. Se utiliza para designar una cantidad susceptible de tomar distintos valores numéricos dentro de un conjunto de números especificados.

Una variable es una caja donde podemos guardar cosas. Esta caja tiene un nombre (identificador).

```python
numero = 3
numero1 = 5
numero2 = 6
print(numero)
print(numero1)
print(numero2)
print(numero1 + numero2)
numero1 = 12
print(numero1 + numero2)
numero1 = numero1 + numero2
```

El identificador de mi variable no puede comenzar con un número y debe estar en minúsculas. Las palabras dentrod del mismo se separan con guión bajo.

## Los primitivos: tipos de datos sencillos

Los 4 tipos de datos básicos son (Simples):

1. Número enteros
   - entero = 10
2. Número de punto flotante
   - numeroDecimal = 3.4
3. Texto (Cadenas de caracteres, Strings)
   - nombre = 'Fredy'
   - apellido = 'Castellón'
   - nombre + ' ' + apellido
   - nombre\*4
4. Booleanos (Verdadero y Falso)
   - verdadero = True
   - falso = False

## Convertir un dato a un tipo diferente

```python
numero1 = input("Escribe un número:")
numero2 = input("Escribe un número:")
numero1 = int(numero1)
numero2 = int(numero2)
numeroDecimal = 4.5
numeroEntero = int(numeroDecimal)
numeroTexto = str(numeroDecimal)
```

## Operadores lógicos y de comparación

```python
es_estudiante = True
trabaja = False
es_estudiante and trabaja
es_estudiante or trabaja
not es_estudiante
numero1 = 5
numero2 = 5
numero1 == numero2
numero3 = 7
numero1 == numero3
numero1 != numeros3
numero1 > numero3
numero1 < numero3
numero1 >= numero3
numero1 <= numero3
```

## Tu primer programa: conversor de monedas

Creamos conversor.py y conversor2.py

# Herramientas para programar

## Construyendo el camino de un programa con condicionales

Muchas veces vamos a tener situaciónes a partir de los cuales debemos tomar una decisión y tomar por una ruta o por otra. Y allí es donde entran los condicionales.

## Modularizando nuestro conversor de monedas

```python
def convertirMoneda(nombreMoneda, valorDolar):
    moneda = float(input("¿Cuántos " + nombreMoneda + " tienes?: "))
    dolares = round(moneda / valorDolar, 2)
    return dolares
```

## Trabajando con texto: cadenas de caracteres

```python
nombre = "fredy "
# "FREDY "
nombre.upper()
# "Fredy "
variable.capitalize()
# "fredy "
variable.lower()
# "fredy"
variable.strip()
# "frody "
variable.replace('e', 'o')
# 6
len(fredy)
```

## Trabajando con texto: slices

```python
nombre = "Fredy"
# Fre
nombre[0:3]
# Fre
nombre[:3]
# dy
nombre[3:]
# red
nombre[1:4]
# Fey
nombre[0:5:2]
# Fredy
nombre[::]
# Fey
nombre[1::2]
# yderF
nombre[::-1]
```

## Proyecto: palíndromo

```python
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    if word == word[::-1]:
        return True
    else:
        return False

def run():
    word = input("Escribe una palabra: ")
    if is_palindrome(word):
        print("Es palíndromo")
    else:
        print("No es palíndromo")

# Este el el entrypoint de un script de Python
if __name__ == "__main__":
    run()
```

# Bucles

## Aprendiendo bucles

Para repetir un conjunto de pasos del algoritmo varias veces.

## El ciclo while

```python
def run():
    LIMIT = 10000
    count = 0
    potencia = 0
    while (potencia <= LIMIT):
        potencia = 2**count
        print("2^"+str(count), "=", potencia)
        count += 1

if __name__ == "__main__":
    run()
```

## Explorando un blucle diferente: el ciclo for

## Recorriendo un string con for

## Interrumpiendo ciclos con break y continue

## Proyecto: prueba de primalidad

## Proyecto: videojuego

# Estructuras de datos

## Almacenar varios valores en una variable: listas

Estos son tipos de datos más complejos. Las listas pertenecen a un conjunto de datos llamados estructras de datos y nos permiten guardar grupos de diferentes tipos de datos en una variable.

```python
numeros = [1, 3, 6, 8, 9, 45, 90]
objetos = ["Hola", 3, 4.5, True]
```

Esto es muy parecido a los strings pues pueden accederse por su index.

```python
objetos[0]
objetos[3]

# Agrega un elemento al final de la lista
objetos.append(False)
# Sacar el elemento en una posición
objetos.pop(1)
for o in objetos:
    print(o)
print[::-1]
print[1:3]
```

```
**Suma **(+) Concatena dos o más listas:
a=[1,2]
b=[3,4]
a + b --> [1,2,3,4]
**Multiplicación **(*) Repite la misma lista:
a=[1,2]
a * 2 —> [1,2,1,2]
Añadir elemento al final de la lista:
a=[1]
a.append(2)=[1,2]
Eliminar elemento al final de la lista:
a=[1,2]
b=a.pop()
a=[1]
**Eliminar elemento **dado un indice:
a=[1,2]
b=a.pop(1)
a=[2]
Ordenar lista de menor a mayor, esto modifica la lista inicial
a=[3,8,1]
a.sort() —> [1,3,8]
Ordenar lista de menor a mayor, esto NO modifica la lista inicial
a=[3,8,1]
a.sorted() —> [1,3,8]
Eliminar elementos de lista Elimina el elemento de la lista dado su indice
a=[1,2,3]
del a[0] —> a[2,3]
Eliminar elementos de lista Elimina el elemento de la lista dado su valor
a=[0, 2, 4, 6, 8]
a.remove(6)
a=[0, 2, 4, 8]
**Range **creacion de listas en un rango determinado
a=(list(range(0,10,2))) -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a=[0,2,4,6,8]
Tamaño lista len Devuelve el valor del tamaño de la lista:
a=[0,2,4,6,8]
len(a)=5
```

## Entendiendo cómo funcionan las tuplas

Esto se puede hacer con listas:

```python
numeros = [1, 2, 3, 4, 5]
numeros2 = [6, 7 , 8 , 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
listaFinal = numeros + numeros2
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5,]
numeros * 5
```

Así es una tupla

```python
mi_tupla = (1, 2, 3, 4, 5)
for i in mi_tupla:
    print(i)
```

Las tuplas son inmutables, a diferencia de una lista no se puede hacer pop, append, etc. Entonces resulta que hacer un ciclo contra una tupla es más rápido que contra una lista. Además las tuplas requiren menos memoria pues no necesita el sistema almacenar memoria extra para hacer append de datos.

## ¿Qué son los diccionarios?

En python los {} sirven para definir diccionarios. Los diccionairios son estructuras de datos de claves y valores.

```python
def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave4": 3,
    }
    print(mi_diccionario)
    print(mi_diccionario["llave1"])
    print(mi_diccionario["llave2"])
    print(mi_diccionario["llave3"])

    ploblacion_pais = {
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
        print(problacion)

    for pais, poblacion in poblacion_paises.items():
        print(pais, "tiene", poblacion, "habitantes"s)

if __name__ == "__main__":
    run()

```

## Proyecto: generador de contraseñas

# Despedida

## Sigue aprendiendo
