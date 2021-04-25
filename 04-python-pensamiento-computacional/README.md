# Introducción al pensamiento computacional

## Introducción al pensamiento computacional

Podemos utilizar Python todos los días, para automatizar nuestras computadoras, para escribir backend y servidores web con apis, y para desarrollar modelos de machine learning. Pero debemos aprender a pensar como ingenieros de software y como computer scientist.

- Resolver problemas de manera computacional.
- Entender los puntos en común entre todos los lenguajes de programación.
- Desarrollar las bases para una carrera en Computer Science.

Todos los lenguajes de programación comparten cosas en común. Y bases para estructurar la carrera como ingeniero de software.

## Introducción al cómputo

1. **Primera Computadora**: Inventada por los griegos para calcular las posiciones del Sol, Luna y algunas constelaciones del Zodiaco. Para conocer las estaciones y sembrar.
2. 1801, El telar de Jacquard, un telar que utilizaba puch cards para controlar la máquinaria. Nos dimos cuenta que podemos separar el producto final de las instrucciones para realizar el proceso.
3. Siglo XIX, El motor análitico de Babbage, tratando de lograr una máquina general para realizar cálculos. Utilizando engranes para llegar a resultados moviendose de cierta manera. Nos dimos cuenta que podemos separar las instrucciones del cálculo y podemos separa las instrucciones del cálculo y tener una máquina para realizar diferentes cálculos.
4. Para finales del siglo XIX, EUA el gobierno empezo a utilizar máquinas que usan los puch cards para realizar los cálculos de sus censos. Para principios del 1900 ya existían empresas que necesitaban cálculos muy precisos y personas cuya profesión era ser computadores (realizar cálculos a mano). Para 1930 llegan Alan Turing y Alonso Chuch y ven que todos los algoritmos que se habían desarrollado podían reducirse a una simple máquina imaginaria que tuviera una cinta infinita con simbolo y que esto se pudieran manipular (Church utilizó funciones con la misma idea.) Con este Insight se dio la carrera por construir la primera computadora electronica que pudiera realizar lo que Turing y Church predijeron. ENIAC se crea en 1945, utilizaba sistema decimal (El binario da ventajas con respecto a la electrónica.)
5. En 1945, La arquitectura de Von Neuman, que es una pieza adicional. Von Neuman se da cuenta que se puede utilizar el mismo hardware para hacer los cálculos y almacenar el algoritmo. Se desarrolla el EDVAC que podía recibir un algoritmo y ejecutarlo.
6. 1950, El Chip, ejemplo Apple 1. Luego fue desarrollandose esto hasta el Microchip. Ahora tenemos computadoras y data centers. Aún a esta escala existen problemas que no podemos resolver de manera computacional.
7. Richard Feynman nos dío las bases del cómputo cuántico. Nos dio las bases mátemáticas que puedan hacer esto. Hoy estamo empezando a lograr estas computadoras.

**Cómputo y computadoras**

- Las computadoras hacen dos cosas: hacen cálculos y recuerdan el resultado de dichos cálculos.
- Por la mayoría de la historia humana, estábamos limitados por la velocidad del cerebro y la mano.
- Aún con las computadoras modernas existen problemas que no podemos resolver.

## Introducción a los lenguajes de programación

Existe conocimiento declarativo y conocimiento imperativo. El declarativo nos indica que relaciones existen entre variables. Y el conocimiento imperativo nos indica como llegar a un resultado.

Dentro del conocimiento imperativo están los algoritmos. Un algoritmo es una lista finita de instrucciones que describen un cómputo, que cuando se ejecuta con ciertas entradas (inputs) ejecuta pasos intermedios para llegar a un resultado(output) - John V. Guttag

Esta idea de algoritmos nos dio los primeros lenguajes de programación.

Adda Lovelace era una contemporanea de Charles Babbage. Con las bases teoricas del motor análitico se podía hacer un programa para calcular la seríe de bernoulli.

Grace Hopper se da cuenta que puede escribir una serie de instrucciones que leen otro programa y traducirlos a un lenguaje de máquina.

Los lenguajes de programación son para los humanos y podemos traducirlos a unos y ceros entendibles para la computadora. Hubo un salto enorme para que nosotros podamos escribir en un lenguaje que entendamos y compilarlo a un lenguaje que entienda la máquina.

C es casí el latín de los lenguajes de programación. De C tenemos toda una familia de lenguajes inspirados ene esta sintaxis.

Guiddo Van Rossum, se dio cuenta en los 90 que una cosa muy importante de los lenguajes de programación es que sean fácil de leer (como el idioma). Por eso Python elimina casí todos los simbolos que no utilizaríamos en el lenguaje.

Los lenguajes de programación modernos son Turing Complete, pues implementan todos los primitivos que necesitamos para realizar cualquier tipo de algoritmo. Podemos implementar cualquier algoritmo que tengamos en la historia.

Los lenguajes de programación moderno dan primitivos que son más convenientoes que los primitivos de Truing.

**Lenguajes**

- **Sintaxis**: Define la secuencia de símbolos que está bien formada.
- **Semántica estática**: Define que enunciados con sintaxis correcta tienen significado.
- **Semántica**: Define el significado. En los lenguajes de programación sólo hay un significado. No tienen doble sentido.

# Introducción a Python

## Preparación de tu computadora

Instalar:

1. Python 3.7+
2. VS Code
3. Instalar la extensión de Python en VSCode

## Elementos básicos de Python

**Lenguajes de programación**

No estamos aprendiendo Python, sino que estamos aprendiendo elementos de los lenguajes de programación que son comúnes a cualquier lenguaje de programación.

- Bajo nivel vs. Alto Nivel: Alto nivel es diseñado para los humanos. Bajo nivel está optimizado para lás máquinas.
- General vs. Dominio específico: Generales tienen todos los primitivos determinados por Turing para poder interpretar cualquier tipo de algoritmo. Especializado es que su target y optimización es para aplicaciones muy específicas.
- Interprestado vs. Compilado: Que el interprete está transformando las instrucciones para entregarselas a la máquina en tiempo de ejcución. Compilado primero lo transoformamos a lenguaje máquina y luego lo ejecutamos.

```python
# <literales> = 1, 'abc', 2.0, True (Formas de inicializar objetos directamente en memoria anotandolos directamente en código) estos literales podemos interpolarlos con ciertos operadores.
# <operadore> = +, -, *, /, %, **, =, ==... (Podemos sumar, restar, multiplicar, dividir, modulo, potencias, asignar, determinar igualdad.)
# La forma en que podemos interpolar estos simbolos es <literal> <operador> <literal>

1 + 2
1 3.0 # error sintáctico
5 / 'un string' # error semántico estático
5 * 'string'
print('Hello world!")
```

**Objetos**

Son la abstracción más alta dentro de cualquier lenguaje de programación. Son la forma en que modelamos el mundo en nuestros lenguajes de programación. Son valores en memoria que podemos referenciar con alguna variable.

Tienen diferentes tipos, enteros, flotantes, booleanos, string, vectores, arreglos (O de alguna clase que creemos).

Los tipos pueden ser escalares y no escalares. Escalares los podemos dividir en piezas más pequeñas. Los no escalares ya no los podemos subdividir. Un vector lo podemos subdividir y un entero ya no lo podemos subdividir.

```python
# A lo que llamamos <objeto> <operador> <objeto> en conjunto lo llamamos una expresión y eso es un valor.
'Un ' + 'Texto'
'Un Texto'
2 + 2
4

my_int = 1
my_float = 1.0
my_bool = False
my_none = None

# Type nos regresa el tipo de objeto
type(my_int)
type(my_float)
type(my_bool)
type(my_none)

1 + 2
2 - 5
2.0 * 3
6 // 2
6 // 4
6 / 4
7 % 2
2**3
```

## Asignación de variables

Las variables son nombres que se vinculan con un valor en memoria a través del operador de asignación.

```python
a = 2
x = 4
z = (a * x) / 2
```

Si llamamos a las variables z, x, z, etc. Nadie tiene idea de que hace tu programa. Debemos dar nombres exactos de lo que significan las variables (y funciones).

```python
base = 2
altura = 4
area = (a * x) / 2
```

Las variables tienen que tener nombres que signifiquen algo para los humanos. Nosotros podemos reasignar una variables y cuando lo hacemos solo reasignamos a dónde apunta en memoria.

```python
my_var = 'Hello World'
print(my_var)
my_var = 3
print(my_var)
```

Existe un garbage collector que se encarga de liberar espacios en memoria cuando reasignamos variables.

**Variables**

- Pueden contener maýusculas, minúsculas, números (sin comenzar con uno) y el símbolo \_
- No pueden llamarse como las palabras reservadas del lenguaje. (False, await, else, import, pass, None, break, except, in, raise, True, class, finally, is, return, and continue, for, lambda, try, as, def, from, nonlocal, while, assert, del, global, not, with, async, elif, if, or, yield)

**Resumen**

- Las variables hacen los programas más comprensibles.
- Son simplemente nombres que apuntan a un valor en memoria.
- El operador de asignación (=) asocia una variable con un valor.

## Cadenas y entradas

Nuestro primer tipo no escalar. Son secuencias de caracteres. Cuando trabajamos con diferentes tipos los operadores tienen diferentes significado.

```python
'123'
'123' * 3
'123' + '456'
('Hip ' * 3) + ' ' + 'hurra'
f'{"Hip " * 3} hurra'
```

Nosotros podemos trabajar con diferentes funciones en las cadenas pero también podemos aplicarles diferentes funciones:

- len(longitud)
- Indexing(indexación)
- slicing(rebanadas) (comienzo-inclusivo:final-exclusivo:pasos)

```python
my_str = 'Python'
len(my_str)
my_str[0]
my_str[1]
# Cadena desde el caracter en la posición 2 hasta el final
my_str[2:]
# Cadena desde el caracter en la posición 0 hasta el 3 caracter exclusivo.
my_str[:3]
# Toda la cadena pero de 2 en 2 caracteres.
my_str[::2]
my_str + ' is cool'
f'{ my_str } is cool'
f'{ my_str } is cool, ' * 100
```

**Cadenas (strings)**

- Los objetos de tipo str pueden representarse con "" o ''.
- El operador + tiene diferentes significados según el tipo de datos (overloaded). Con cadenas significa concatenación.
- El operador \* es el operador de repetición con cadenas.
- Las cadenas son inmutables.

**Entradas (inputs)**

- Python tiene la función input para recibir datos del usuario del programa.
- Input siempre regresa cadenas, por lo que si queremos utilizar otro tipo, tenemos que hacer type casting.

```python
nombre = input("¿Cuál es tu nombre? ")
print(nombre)
print("Tú nombre es", nombre)
print(f"Tú nombre es { nombre }")
numero = input("Escribe un número: ")
print(numero)
print(type(numero))
numero = int(input("Escribe un número: "))
print(numero)
print(type(numero))
```

## Programas ramificados

Para generar programas interesantes nuestras instrucciones deben poder realizar decisiones, tests o pruebas para decidir si se ejecta una parte de un programa u otra.

Los tests los haríamos con operadores de comparación. Para comparar dos valores y determinar el resultado de esta comparación.

```python
2 == 3
2 != 3
2 > 3
2 < 3
2 <= 3
2 >= 3
```

Además de los operadores de comparación también tenemos operadores lógicos y estos son 3:

```python
True and True
False or True
not True
```

La forma en que generamos condiciones es con if, if-else, if-elif-else

```python
if 3 > 2:
    print("3 es mayor que 2")

if 5 >= 10:
    print("Esto no va a pasar")
else:
    print("5 no es mayor o igual a 10")

if 4 > 5:
    print("Esto no va a pasar")
elif 4 < 5:
    print("4 es menor que 5")
else:
    print("Esto tampoco va a pasar")
```

## Iteraciones (loops)

Otro concepto importante dentro de los lenguajes de programación son las iteraciones o los loops. Nos permiten realizar la misma tareas varias veces.

- La mayoría de las tareas computacionales no se pueden lograr con ramificaciones.
- Cuando queremos que un programa haga lo mismo varias veces, utilizamos iteraciones.
- Se pueden escribir iteraciones dentro de iteraciones.
- Podemos utilizar break para sarlir anticipadamente de una iteración
- Tener cuidado de iteraciones infinitas.

```python
contador = 0
while contador < 10:
    print(contador)
    contador += 1

contador_externo = 0
contador_interno = 0
while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1
        if contador_interno >= 3:
            break

    contador_externo += 1
    contador_interno = 0

```

## Bucles for

Los bucles, en diversos lenguajes de programación pueden ser definidos o indefinidos. Los bucles definidos prestablecen las condiciones de la iteración por adelantado. Por su parte, los bucles indefinidos establecen la condición en la que una iteración terminará. En este último tipo de bucles existe el riesgo de que el bucle se vuelva infinito (cuando la condición de suspensión nunca se cumple).

Los bucles definidos se implementan en Python a través del keyword for. Por su parte, los bucles indefinidos se implementan con el keyword while.

Sin embargo, esta no es la única forma de implementar bucles definidos. Por ejemplo, Javascript puede implementar un bucle definido mediante el constructo:

```
for (i = 0; i <= 10; i++){
    expresión
}
```

El bucle se puede leer de la siguiente manera:

- Inicializa el bucle en 0
- Continua el bucle mientras i sea menor o igual que 10
- Incrementa i en uno al final de cada iteración

Es importante señalar que la expresión i++ es equivalente a lo que en Python escribiríamos como i += 1.

Una segunda forma de crear un bucle definido es iterando en una colección de objetos. esta es la forma que Python utiliza:

```
for variable in iterable:
    expresión
```

**El bucle for en Python**

En la definición anterior debemos entender iterable como una colección de objetos; y la variable como el elemento específico que se está exponiendo mediante el bucle en cada iteración.

```python
frutas = ["manzana", "pera", "mango"]
for fruta in frutas:
    print(fruta)
```

**Iterables**

En Python, un iterable es un objeto que se puede utilizar en un bucle definido. si un objeto es iterable significa que se puede pasar como argumento en la función iter. El iterable que se pasa como parámetro a la función iter regresa un iterator.

```python
iter("cadena") # cadena
iter(["a", "b", "c"]) # lista
iter(("a", "b", "c")) # tupla
iter({"a", "b", "c"}) # conjunto
iter({"a": 1, "b": 2, "c": 3}) # diccionario
```

Todas las llamadas anteriores regresan un objeto de tipo iterador.

¿Qué pasa si le pasamos a la función iter un objeto que no es iterable? Obtendremos un TypeError que señala que el objeto no es un iterable. Esto es un ejemplo de programación defensiva en el que Python verifica el tipo del objeto antes de proceder al cómputo.

Es importante señalar que estos no son lo únicos tipos de objetos que pueden ser iterables. Existe gran cantidad de ejemplos en la librería estándar y, de hecho, casi caulquier objeto se peude convertir en un iterable.

**Iterators**

Ahora que ya sabemos cómo obtener un iterator, ¿Qué podemos hacer con él? Un iterator es un objeto que regresa sucesivamente los valores asociados con el iterable.

```python
frutas = ["manzana", "pera", "mango"]
iterador = iter(frutas)
next(iterador) #manzana
next(iterador) #pera
next(iterador) #mango
```

El iterator guarda el estado interno de la iteración, de tal manera que cada llamada sucesiva a next regresa el siguiente elemento. ¿Qué pasa una vez que ya no existan más elementos en el iterable? La llamada a next arrojará un error de tipo StopIteration.

**¿Cómo implementa Python los bucles definidos?**

Ahora ya conocemos todos los elementos necesarios para entender que es lo qeu sucede en Python cuando ejecutamos un bucle for. Considera nuevamente el siguiente código:

```python
frutas = ["manzana", "pera", "mango"]
for fruta in frutas:
    print(fruta)
```

Este bucle se puede describir con los conceptos que explicamos previamente:

1. Python llama internamente la función iter para obtener un iterador.
2. Una vez que tiene un iterator llama repetidamente la función next para tener acceso al siguiente elemento en el bucle.
3. Detiene el bucle una vez que se arroja el error StopIteration.

**Bucles for con diccionarios**

Para iterar a lo largo de un diccionario tenemos varias opciones:

- Ejecutar el bucle for directamente en el diccionario, lo cual nos permite iterar a lo largo de las llaves del diccionario.
- Ejecutar el bucle for en la llamada keys del diccionario, lo cual nos permite iterar a lo largo de las llaves del diccionario.
- Ejecutar el bucle for en la llamada items del diccionario, lo cual nos permite iterar en una tupla de las llaves y los valores del diccionario.

```python
estudiantes = {
    "mexico": 10,
    "colombia": 15,
    "puerto_rico": 4,
}

for pais in estudiantes:
    print(pais)

for pais in estudiantes.keys():
    print(pais)

for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)

for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)
```

**Modificación del comportamiento de un bucle for**

Podemos modificar el comportamineto de un bucle for mendiante los keywords break y continue.

break termina el bucle y permite continuarl con el resto del flujo de nuestro programa.

continue termina la iteración en curso y continua con el siguiente ciclo de iteración.

# Programas numéricos

## Representación de flotantes

La mayoría del tiempo los números flotantes (tipo float) son una muy buena aproximación de los números que queremos calcular con nuestras computadoras. sin embargo, "la mayoría del tiempo" no significa todo el tiempo, y cuando no se comportan de esta manera puede tener consecuencias inesperadas.

Por ejemplo:

```python
x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f"x = {x}")
else:
    print(f"x != {x}")
```

El resultado es 0.999999999999 . ¿Qué es lo que pasó? Para entender qué es lo que pasó tenemos que entender que es lo que pasa en la computadora cuando realizamos cómputos con números flotantes. Y para eso necesitamos entender números binarios.

Cuando aprendiste a contar, lo que enrealidad paprendiste es una técnica combinatoria para manipular los siguientes símbolos que llamamos números: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

La forma en la que funciona esta técnica es asignando el núermo 10 a la 0 al núermo de la extrema derecha, 10 a la 1 al siguiente, 10 a la 2 al siguiente y así sucesivamentes. De tal manera que el núermo 525 es simplemnte la representación de (5 _ 100) + (2 _ 10) + (5 \* 1).

Esto nos dice que el número que podemos represntar depende de cuanto espacio tengamos. Si tenemos un espacio de 3, podemos represntar 1000 números (10 elevado a la 3) o la secuencia de 0 al 9999. Si tenemos 4, podemos representar 10000 (10 elevado a la 4) o la secuencia de 0 al 9999. De manera general podemos decir que con una secuencia de tamaño n, podemos representar 10 elevado a la n números.

Los números binarios funcionan de la misma manera (de hecho cualquier número en cualquier base, por ejemplo, octales o hexadecimales). La única diferencia es cuántos símbolos tenemos para represntar. En binario nada más tenemos 0, 1; en hexadecimal tenemos 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f.

De esta manera podemos decir que el núermo de la extrema derecha es cantidad_de_simbolos^0, cantidad_de_simbolos^1, cantidad_de_simbolos^2, etc. Por lo que en binario, que nada más tenemos 2 símbolos, decimos 2^0, 2^1, 2^2, etc. Por ejemplo el número binario 101 es la represntación de (1x4)+(0x2)+(1x1), es decir 5.

Esta representación nos permite trabajar con todos los números positivos enteros dentro del computador, pero ¿Qué hacemos con los negativos y los racionales?

El caso de los números negativos es sencillo: simplemente agregamos un bit adicionales que representa el signo y la añadimos en la extrema izquierda. Por lo que el núermo 0101 sería +5 y el núermo 1101 sería -5.

El caso de los racionales es más complejo. En la mayoría de los lenguajes de programación moderno los racionales utilizan una implementación llamada punto flotante. ¿Cómo funciona esta representación?.

Antes de pasar a binario, vamos a pretender que estamos trabajando con una computadora basada en decimales. Un número flotante lo representaríamos con un par de enteros: los dígitos significativos y el exponete. Por ejemplo, el número 2.345 se representaría como (2345 \* 10 \*\* -3) o (2345, -3).

El número de dígitos significativos determinan la precisión con la que podemos representar números. Por ejemplo si nada más tuviéramos dos dígitos significativos el número 2.345 no se podría representar de manera exacta y tendríamos que convertirlo a una aproximación, en este caso 2.3.

Ahora pasemos a la verdadera representación interna de la computadora, que es en binario. ¿Cómo representarías el número 5/8 o 0.635? Lo primero que tenemos que saber es que 5/8 es en realidad el número 5 \* 2 \*\* -3. Por lo que podríamos decir (101, -11) (recuerda que el núermo 5 es 1010 en bianrio y el 3 es 11).

Regresamos a nuestro problema inicial: ¿Cómo representaremos 1/10 (que escribimos en Python cómo 0.1)? Lo mejor que podemos hacer con cuatro dígitos significativos es (0011, -101), que es equivalente a 3/32 (0.09375). ¿Qué tal si tuviéramos cinco dígitos significativos? La mejor representación sería (11001, -1000) que es quivalente a 25/256 (0.09765625). ¿cuántos dígitos significativos necesitamos entonces? Un número infinito....
s
En la mayoría de las implementaciones de Python tenemos 53 bits de precisión para números flotantes. Así que los dígitos significativos para representarl el número 0.1 es igual a: 11001100110011001100110011001100110011001100110011001 que es equivalente al número decimal: 0.1000000000000000055511151231257827021181583404541015625.

Muy cercano a 1/10 pero no exactamente 1/10. Ahora ya sabemos la razón de esa respuesta tan extraña. Hay muy pocas situaciones en la que 1.0 es aceptable, pero 0.9999999999999999 no. Pero ¿Cuál es la moraleja de esta historia?

Hasta ahora hemos verificado igualdad con el operador ==. Sin embargo, cuando estamos trabajando con flotantes es mejor asegurarnos que los núermos sean aproximados en vez de idénticos. Por ejemplo x < 1.0 and x > 0.99999.

## Enumeración exhaustiva

El primer algoritmo que vamos a ver es la **Enumeración exhaustiva**

- También lo podríamos llamar "adivina y verifica".
- Las computadoras actuales son muy muy rápidas.
- Uno de los primeros algoritmos que debes tratar.

Ejemplo:

```python
objetivo = int(input("Escoge un entero: "))
respuesta = 0
while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f"La raíz cuadrada de {objetivo} es {respuesta}")
else:
    print(f"El {objetivo} no tiene una raíz cuadrada exácta")
```

## Aproximación de soluciones

- Similar a la enumeración exhaustiva, pero no necesita una respuesta exacta.
- Podemos aproximar solucines con un margen de error que llamaremos epsilon.

Nosotros no podemos ser precisos y rápidos a la vez. Mientras más nos acercamos a la solución (epsilon es más pequeño) más ciclos debemos hacer y por lo tanto demorar más en dar una respuesta.

```python
objetivo = int(input("Escoge un entero: "))
epsilon = 0.01
paso = epilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"No se encontró la raíz cuadrada de {objetivo}")
else:
    print(f"La raíz cuadrada de {objetivo} es {respuesta}")
```

## Búsqueda Binaria

La busqueda binaria es uno de los algoritmos más importantes y eficientes en computer science.

- Cuando la respuesta se encuentra en un conjunto ordenado, podemos utilizar búsqueda binaria.
- Es altamente eficiente, pues corta el espacio de búsqueda en dos por cada iteración.

```python
objetivo = int(input("Escoge un número: "))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetio) >= epsilon:
    if respuesta ** 2 < objetivo:
        bajo = respuesta
    else
        alto = respuesta
    respuesta = (alto + bajo) / 2

print(f"La raíz cuadrada de {objetivo} es {respuesta})
```

La busqueda binaria será una herramienta muy importante en nuestro cinturon de Computer Scientist.

# Funciones, alcance y abstracción

## Funciones y abstracción

Con lo que ya conocemos hasta este momento podríamos construir cualquier programa posible. Porque esto se conoce como Turing Complete. Pero escribir programas de esta manera sería un completo desorden, modificarlo sería un problema, nadie prodría entenderlo.

Los lenguajes de programación modernos nos dan otra serie de abstracciones para modularizar el código generando clases, funciones, módulos, paquetes.

**Abstracción**

Significa que no necesito entender la forma en que algo opera internamente para poderlo utilizar. Para saber utilizar una calculadora no necesito saber de electrónica. Esto es muy común en la vida diaria. Yo puedo utilizar un automovil sin saber como funciona el motor de combustión interna y la caja de cambios.

Una habilidad muy importante de los ingenieros de software es generar estas abstracciones. Muchas veces utilizaremos librerías escritas por otros que nos permiten utilizar funcionalidades sin conocer a fondo como están hechas pero sí como utilizarlas y lograr el objetivo.

**Decomposición**

- Permite dividir el código en componentes que colaboran con un fin en común.
- Se puede pensar como mini programas dentro de un programa mayor.

Nosotros podemos Abstraer (Encapsular la implementación de nuestro código y definimos una interfaz pública) y podemos decomponer (Generar muchos pedazos pequeños de nuestro código) y aquí nos ayudan las funciones.

**Definición de funciones**

Las funciones en python se definen así:

```
def <nombre>(<parametros>):
    <cuerpo>
    return <expresión>
```

Ejemplo:

```python
def suma(a, b):
    total = a + b
    return total

suma(2, 3)
```

**Argumentos de keyword y valores por defecto**

Las funciones en Python pueden tener argumentos de tipo Keyword y valores por defecto.

```python
def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return f"{apellido} {nombre}"
    else:
        return f"{nombre} {apellido}"

nombre_completo("Fredy", "Castellón")
nombre_completo("Fredy", "Castellón", inverso=True)
nombre_completo(apellido="Castellón", nombre="Fredy")
```

## Scope o Alcance

Un punto muy importante que tenemos que entender es el alcance de las funciones. Cuando ejecutamos una función Python entra en un nuevo contexto de ejecución y a este contexto se le asignan las variables a las que se tiene acceso en el código.

```python
def func1(un_arg, una_func):
    def func2(otro_arg):
        return otro_arg * 2

    valor = func2(un_arg)
    return una_func(valor)

un_arg = 1

def cualquier_func(cualquier_arg):
    return cualquier_arg + 5

func1(un_arg, cualquier_func)
```

Todo esto funciona por Frames.

http://www.pythontutor.com/visualize.html

## Especificaciones del código

Ahora necesitamos decirle al usuario de este código como utilizar esta función. Esto lo hacemos atraves de las especificaciones del código. En Python docstrings

```python
def suma(a, b):
    """Suma dos valores a y b

    param int a cualquier entero
    param int b cualquier entero
    returns la sumatoria de a y b
    """
    total = a + b
    return total
```

Con """ podemos generar un string de varias lineas. Y debemos tener 3 aspectos importantes dentro de la documentación:

1. Que hace la función
2. Que significan los parametros (nombre, tipo y que esperamos con los parametros)
3. Que es lo que regresa esta función.

Con esto podemos comunicar que es lo que hace nuestro código.

Estas docstrings se muestran cuando ejecutamos:

```python
help(suma)
```

## Recursividad

Uno de los temas más importantes dentro de las ciencias de la computación.

**Definición**

- **Algorítmica**: Una forma de crear soluciones utilizando el principio de "divide y vencerás". Un problema podemos resolverlo utilizando versiones más pequeñas del mismo problema. Hasta que encontremos una solución base muy facil de resolver.
- **Programática**: Una técnica programática mediante la cual una función se llama a sí misma.

**Factoriales**

```python
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n - 1)
```

La recursión es una forma de iterar. Y toda solución recursiva se puede representar como un loop.

## Fibonnacci y la Recursividad

La secuencia de Fibonacci es una función matemática que se define recursivamente. En el año 1202, el matemático italiano Leonardo de Pisa, también conocido como Fibnacci, econtró una fórmula para cuantificar el crecimiento que ciertas problaciones experimentan.

Tenemos dos casos base (0 y 1) y tenemos dos llamadas recursivas fibonacci(n-1) + fibonacci(n-2)

```python
def fibonacci(n):
    """Calcula el fibonacci de un número n
    param int n cualquier número entero positivo
    returns fibonacci de n
    """
    if n == 0 or n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
```

Aunque la definición es muy sencilla, es también bastante ineficiente.

# Tipos estructurados, mutabilidad y funciones de alto nivel

## Funciones como objetos

Una de las características más poderosas de Python es que todo es un objeto, incluyendo las funciones. Las funciones en Python son "ciudadanos de primera clase".

Esto, en sentido amplio, significa que en Python las funciones:

- Tienen un tipo
- Se pueden pasar como argumentos de otras funciones
- Se pueden utilizar en expresiones
- Se pueden incluir en varias estructuras de datos (como listas, tuplas, diccionarios, etc.)

**Argumentos de otras funciones**

Hasta ahora hemos visto que las funciones pueden recibir parámetros para realizar los cómputos que definen. Algunos de los tipos que ehmos pasado son tipos simples como cadenas, números, listas, etc. Sin embargo, también pueden recibir funciones para crear abstracciones más poderosas.

```python
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)

numeros = [1, 2, 3]
aplicar_operacion(multiplicar_por_dos, numeros)
aplicar_operacion(sumar_dos, numeros)
```

**Funciones en expresiones**

Una forma de definir una función en una expresión es utilizando el keyword lambda. lambda tiene la siguiente sintaxis: `lambda <vars>: <expresion>`.

Otro ejemplo interesnate es que las funciones se pueden utilizar en una expresión directamente. Esto es posible ya que en Python las variables son simplemente nombres que apuntan a un objeto (en este caso a una función). Pro ejemplo:

```python
sumar = lambda x, y: x + y
sumar(2, 3)
```

**Funciones en estructuras de datos**

Las funciones también se pueden incluir en diversas estructuras que las permiten almacenar. Por ejemplo, una lista puede guardar diversas funciones a aplicar o un diccionario las puede almacenar como valores.

```python
def aplciar_operaciones(num):
    operaciones = [abs, float]
    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

aplicar_operaciones(-2) # [2, -2.0]
```

Como pudimos ver, las funciones son objetos muy versátiles que nos permiten tratarlas de diversas maneras y que nos permiten añadir capas adicionales de abstracción a nuestro programa.

## Tuplas

- Son secuencias inmutables de objetos.
- A diferencia de las cadenas pueden contener cualquier tipo de objeto.
- Puede utilizarse para devolver varios valores en una función.

```python
my_tuple = ()
type(my_tuple)
my_tuple = (1, 'dos', True)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[3])
my_tuple[0] = 2 # No se puede
my_tuple = (1)
type(my_tuple) # Entero
my_tuple = (1,)
type(my_tuple) # Es un <class 'tuple'>
my_other_tuple = (2, 3, 4)
my_tuple += (2, 3, 4) # El objeto no muta, se reasigna
print(my_tuple) # (1, 2, 3, 4)
x, y, z = my_other_tuple
print(x, y, z) # 2 3 4
def coordenadas():
    return (5, 4)

coordenada = coordeandas()
print(coordenada) # (5, 4)
x, y = coordenada
print(x, y) # 5 4
```

## Rangos

- Representan una secuencia de enteros.
- range(comienzo, fin, pasos)
- Al igual que las cadenas y las tuplas, los rangos son inmutables
- Muy eficientes en uso de memoria y normalmente utilizados en los for loops

```python
my_range = range(1, 5)
print(type(my_range)) # <class 'range'>
for i in my_range:
    print(i)
my_range = range(0, 7, 2)
my_other_range = range(0, 8, 2)
my_range == my_other_range # True
for i in my_range:
    print(i)
for i in my_other_range:
    print(i)

id(my_range) # id es la dirección de memoria donde python guardó
id(my_other_range) # la dirección del otro rango

my_range is my_other_range # False porque no son el mismo objeto, porque no están en la misma variable

# Generando la secuencia de 0 a 100 de números pares:
for i in range(0, 101, 2):
    print(i)
```

## Listas y mutabilidad

Esta es nuestra primera estructura de objetos que de hecho si es mutable.

- Son secuencias de objetos, pero a diferencia de las tuplas, sí son mutables. Nosotros podemos ir creciendo la memoria porque Python no sabe de entrada el tamaño de nuestra lista.
- Cada vez que mutamos una estructura de datos podemos introducir bugs a nuestro código. Cuando modificamos una lista, pueden existir efectos secundarios.
- Es posible iterar con ellas.
- Para modificar una lista podemos:
  - Asignar vía índice (my_lista[0] = 5)
  - Utilizar los métodos de la lista (append, pop, remove, insert, etc.)

```python
my_list = [1, 2, 3]
my_list[0] # 1
my_list[1:] # 2, 3
my_list.append(4) # 1, 2, 3, 4
my_list[0] = 'a' # 'a', 2, 3, 4
my_list.pop() # 4
my_list # 'a', 2, 3
for element in my_list:
    print(element)

a = [1, 2, 3]
b = a
id(a)
id(b) # Apuntan al mismo lugar
a is b # True
c = [a, b] # [[1, 2, 3], [1, 2, 3]]
a.append(5)
c # [[1, 2, 3, 5], [1, 2, 3, 5]]
```

En lugar de estar asignando así porque eso puede se uno de sus side effects. Es mejor clonar la lista. Casí siempre es mejor clonar una lista que modificarla. Para clonar una lista podemos utiizar rebanadas (slices) o la función list.

```python
a = [1, 2, 3]
id(a)
b = a
id(b) # Mismo id de a, son la misma lista
c = list(a)
id(c) # Diferente id, diferente lista
d = a[::]
id(d) # d tiene un id diferente, es una lista diferente
```

**List comprehensions**

- Es una forma concisa de aplicar operaciones a los valores de una secuencia.
- También se pueden aplicar condiciones para filtrar.

```python
my_list = list(range(100)) # Una lista de 0 a 99
double = [i * 2 for i in my_list] # Una lista de multiplicar por dos la lista anterior
pares = [i for i in my_list if i % 2 == 0] # Una lista de los pares
```

## Diccionarios

- Son como listas, pero en lugar de usar índices utilizan llaves.
- No tienen un orden interno. También son conocidos como HashMaps. Los índices se pasan por una función de Hash y esto hace que sean super eficientes de buscar en ellos.
- Los diccionarios son mutables
- Pueden iterarse a traves de sus llaves, valores y claves y valores.

```python
my_dict = {
    "David": 35,
    "Erika": 32,
    "Jaime": 50,
}

my_dict["David"] # David
my_dict["Erik"] # Error porque la llave no existe.
my_dict.get("Juan", 30) # Regresa 30 porque Juan no existe
my_dict["Jaime"] = 20
print(my_dict) # {"David": 35, "Erika": 32, "Jaime": 20}
my_dict["Pedro"] = 70
print(my_dict) # {"David": 35, "Erika": 32, "Jaime": 20, "Pedro": 70}

# Si queremos borrar podemos usar del

del my_dict["Jaime"]
print(my_dict) # {"David": 35, "Erika": 32, "Pedro": 70}

for llave in my_dict.keys():
    print(llave)

for value in my_dict.values():
    print(value)

for llave, valor in my_dict.items():
    print(llave, valor)

# Cuando queremos saber si existe una llave en un diccionario

"David" in my_dict # True
"Tom" in my_dict # False
```

**Dictionary Comprehenstion**

```python
my_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
double_dict = {key:value * 2 for (key, value) in my_dict.items()} # Diccionario de doubles
pares_dict = {key:value for (key, value) in my_dict.items() if value % 2 == 0} # Diccionario de pares
my_dict_doble_key = {key*2:value for (key, value) in my_dict.items()}
```

# Pruebas y debugging

## Pruebas de caja negra

- Se basan en la especificación de la función o del programa.
- Prueba inputs y valida outputs.
- Unit testing o integration testing.

No conocemos la implementación, solo le mandamos inputs y esperamos outputs.

Unit Test es para probar que los modulos funcionen individualmente.

Integration Test es probar que los módulos funcionen entre sí.

caja-negra.py

```python
import unittest

def suma(num_1, num_2):
    return abs(num_1) + num_2

class CajaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -17)

if __name__ == '__main__':
    unittest.main()
```

## pruebas de caja de cristal

- Se basan en el flujo del programa. Asume que conocemos todos los caminos de la implementación.
- Prueba todos los caminos posibles de una función. Ramificaciones, bucles for y while, recursión.
- Son muy útiles cuando hacemos Regression testing o mocks.

Si tenemos un if, necesitamos una prueba de entrar al if y una de no entrar al if.

Si tenemos un ciclo, necesitamos una prueba de no entrar al for, de entrar una vez y de entrar más de una vez.

Y debemos probar todas las excepciones

caja_crital.py

```python
import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class CajaDeCristalTest(unittest.TestCase):
    def test_es_mayor_de_edad_verdadero(self):
        edad = 20
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, True)

    def test_es_mayor_de_edad_verdadero(self):
        edad = 15
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, False)
```

Es como una safety net, en donde nos protegemos de nuestro yo futuro y de nuestros compañeros que no tenían el contexto completo cuando escribimos nosotros la función.

## Debugging

Aún a los mejores ingenieros del mundo, sus programas tienen una tendencia de generar bugs. La mejor forma de generar bugs es con los tests. Si tenemos un test suite nuestros programas tendrán menos bugs pero de todos modos los tendrán.

Grace Hopper fue la primera persona que encontró un bug en una computadora... y fue literalmente un bug.

**Reglas generales**

- No te molestes con el debugger. Aprende a utilizar el print statement.
- Estudia los datos disponibles.
- Utiliza los datos para crear hipótesis y experimentos. Métodos científico.
- Ten una mente abierta. Si entendieras el programa, probablemente no habría bugs. No te preguntes porque el programa está fallando, pregunta ¿Por qué esta funcionando de esta manera? Los programas solo hacen lo que les decimos que hagan.
- Lleva un registro de lo que has tratado, preferentemente en la forma de tests.

**Diseño de experimentos**

- Debugear es un proces de búsqueda. Cada prueba debe acotar el espacio de búsqueda.
- Búsqueda binaria con print statements.

**Errores comunes**

Usual Suspects.
Encuentra a los sospechosos comunes: - Pasaste los argumentos en un orden incorrecto - Escribiste el nombre de forma erronea - No inicializaste una variable que debería estar inicializada. - Trataste de comparar dos flotantes de forma exacta en lugar de con una aproximación. - Trataste de comparar con value equality en lugar de object equality. - Usaste una función que tiene efectos secundarios... append. - Creamos una alias sin darnos cuenta - O errores comunes de nosotros

**Más recomendaciones**

- En lugar de preguntarte por qué el programa no funciona, pregúntate por qué está funcionando de esta manera.
- Es posible que el bug no se encuentre donde crees que está.
- Explicale el problema a otra persona. De preferencia que no tenga contexto.
- Lleva un registro de lo que has tratado, preferentemente en la forma de tests.
- Vete a dormir.

# Excepciones y afirmaciones

## Manejo de excepciones

Las excepciones son cuando ocurre un error en mi código.

- Las excepciones son muy comunes en la programación. No tienen nada de excepcional. Las encontramos en todas partes. Tenemos que utilizarlas para manejar los errores que sabemos que van a suceder. Se trata de utilizar defensive programing para defendernos de los posibles errores.
- Las excepciones de Python normalmente se relacionan con errores de semántica. Excepciones de tipo, de división.
- Se pueden crear excepciones propias.
- Cuando una excepción no se maneja (unhandled exception), el programa termina en error. Si existe una excepción y no la manejo mi programa termina, kaput, explota.
- Las se manejan con lo keywords: try, except, finally.
- Se pueden utilizar también para ramificar programas.
- No deben manejarse de manera silenciosa (por ejemplo, con print statements)
- Para aventar tu propia excepción utiliza el keyword raise

Los errores hay que manejarlos de forma explicita (ZeroDivisionError).

```python
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = 0
print(divide_elementos_de_lista(lista, divisor))
```

## Excepciones y control de flujo

Hsta ahora hemos visto como las excepciones nos permite controlar los posibles errores que pueden ocurrir en nuestro código. Sin embargo, dentor de la comunidad de Python tiene otro uso: control de flujo.

En este momento ya debes estar familiazado con las estructuras de control de flujo que ofrece Python (if.. elif...else); entonces, ¿por qué es necesaria otra modalidad para controlar el flujo? Una razón muy específica: el principo EAFP (Easier to ask for forgiveness than permission).

El principio EAFP es un estilo de programación común en Python en el cual se asumen llaves, índices o atributos válidos y se capturan las excepciónes si la suposición resulta ser falsa. Es importante resaltar que otros lenguajes de programación favorecen el principo LBYL (Look before you leap) en el cual el código se verifica de manera explícita las precondiciones antes de realizar llamadas.

Veamos ambos estilos:

```python
def busca_pais(paises, pais):
    """
    Países es un diccionario. País es la llave. Código con el principio EAFP.
    """
    try:
        return paises[pais]
    except KeyError:
        return None
```

```javascript
/*
 * Países es un objeto. País es la llave.
 * Código con el principo LBYL.
 */
function buscaPais(paises, pais) {
  if (!Object.keys(paises).includes(pais)) {
    return null;
  }
  return paises[pais];
}
```

Como puedes ver, el código de Python accede directamente a la llave y únicamente si dicho acceso falla, entonces se captura la excepción y se provee el código necesario. En el caso de JavaScript, se verifica primero que la llave exista en el objeto y únicamente con posterioridad se accede.

Es importante resaltar que ambos estilos pueden utilizarse en Python, pero el estilo EAFP es mucho más "pythonico".

## Afirmaciones

Las afirmaciones son un mecanismo para determinar si una condición se cumple o no se cumple. Y poder seguir adelante con la ejecución de nuestro programa y continuar...

- Las afirmaciones son un método de programación defensiva.
- Las podemos utilizar para verificar que los tipos sean correctos en una función.
- También sirven para hacer debug.

```python
# assert <expresión booleana>, <mensaje de error>
def primera_letra(lista_de_palabras):
    primera_letra = []
    for palabra in lista_de_palabras:
        assert type(palabra) == str, f"{ palabra } no es un str"
        assert len(palabra) > 0, "No se permiten str vacíos"
        primeras_letras.append(palabra[0])
    return primeras_letras
```
