# Primeros pasos

## ¿Qué es la terminal?

Para desarrollo web, ciencia de datos, ciberseguridad la terminal es una herramienta indispensable. La mera mera terminal.

**¿Por qué debo aprender esto?**

- Flexibilidad
- Velocidad
- Mover grandes volúmenes de información de manera rápida, hacer copias, backups, programar procesos que se ejecuten autmáticamente cada cierto tiempo.
- No siempre cuentas con una interfaz gráfica

**La terminal**

Es una interfaz gráfica que simula una línea de comandos.

Cuando hablamos de una línea de comandos nos referimos a un shell.

**Vamos por partes**

- **Terminal**: Nos referimos a la ventana que nos muestra el prompt. Este arroja a la shell.
- **Línea de comandos (shell)**: Un programa que toma comandos y los pasa al sistema operativo para hacer algo.

**Algunso tipos de shells**

- Bourne Shell
- Bash Shell
- Z Shell
- C Shell
- Korn Shell
- Fish Shell
- PowerShell (La de windows)

**Un comando de manera sencilla es**

Un programa que se puede ejecutar desde la terminal. Este puede recibir parámetros y opciones.

## Aprendiendo a caminar en la terminal

Primeros pasos en la terminal.

- /

  - etc
  - dev
  - home
    - fredy
      - work
      - photos
  - usr
    - lib
  - var

https://www.geeksforgeeks.org/linux-file-hierarchy-structure/

- **ls**: Para listar. ls -l, ls -lh, ls -la (ocultos), ls -lS (ordeando por tamaño), ls -lr (En orden reverso)
- **cd**: Para cambiar de directorio. cd ~, cd, cd ., cd ..
- **clear**: Para limpiar la terminal. Ctrl+l hace lo mismo.
- **pwd**: Nos da la ruta en la que estamo ubicados en ese momento. (Print work directory)
- **file**: Nos describe un tipo de archivo. file ./Pictures/screenshot.png
- **tree**: Es para ver los archivos como un árbol. tree, tree -L 2 (que solo muestre 2 niveles)

## Manipulando archivos y directorios

- **mkdir**: Para crear directorios. mkdir midirectorio, mkdir dir1 dir2 dir3.
- **touch**: Para crear archivos. touch file1 file2 file3.
- **cp**: Copiar archivos. cp file1 file1_bk
- **mv**: Mover archivos. O renombrar archivos y directorios. mv file1_bk ./dir1/, mv file2 file4, mv dir1 dir2
- **rm**: Para borrar archivos. rm file4, rm -i file4, rm -ri dir1

## Explorando el contenido de nuestros archivos

- **head**: Para ver las primeras líneas del archivo de texto. head archivo.md (las primeras 10 lineas), head -n 15 archivo.md
- **tail**: Para ver las últimas líneas de archivo. tail archivo.md (las últimas 10 líneas por default), tail -n 15 archivo.md.
- **less**: Para explorar el archivo y hacer scroll. less archivo.md.
- **xdg-open**: Debería venir con linux para abrir archivos.
- **nautilus**: Abre el explorador de archivos.

## ¿Qué es un comando?

**Un comando puede ser 4 cosas**

1. Un programa ejecutable.
2. Un comando de utilidad de la shell.
3. Una función de shell.
4. Una alias.

- **type cd**: cd si a shell builtin.
- **type mkdir**: mkdir is /usr/bin/mkdir
- **type ls**: ls is aliased to 'ls --color=auto'
- **alias** para crear un alias. alias l="ls -lh". Los alias no duran para toda la vida... son temporales. Se deben guardar en el .bashrc
- **help**: Es para pedir ayuda, help cd, ls --help
- **man**: Es para ver el manual de usuario. man ls
- **info**: Tambien para ver info del comando. info ls
- **whatis**: whatis ls.

## Wildcards

Para realizar busquedas mucho más avanzadas con el comando ls. Usamos wildcards para encontrar un cierto patrón.

- ls \*.txt
- ls datos\*
- ls datos? (archivos que tengas datos al inicio y solo un caracter al final)
- ls datos??? (archivo que tenga datos al inicio y 3 caracteres al final)
- ls [[:upper:]] (Un character con mayúscula) (Las wildcards buscan en dos niveles)
- ls -d [[:upper:]] (Solo directorios)
- ls -d [[:lower:]] (Directorios que inicien con minúscula)
- ls [ad]\*: Archivos que empiecen con a o d

# Empezando a correr

## Redirecciones: cómo funciona la shell

Normalmente nosotros ingresamos un comando y en terminal produce un output. Y podemos manejar estas entradas y salidas a través de ciertos operadores.

**Outputs e inputs**

- **stdin**: Este es el Standard Input y tiene el file descriptor de 0
- **stdout**: Este es el Standard Output y tiene el file descriptor de 1
- **stderr**: Este es el Standard Error y tiene el file descriptor de 2

> ls Pictures/ > list-files.txt
>
> ls Downloads/ >> list-files.txt
>
> ls kdjfaksdfja 2> error.txt
>
> ls askdjfaksd > output.txt 2>&1
>
> ls Documents > output.txt 2>&1

## Redirecciones: pipe operator

El pipe operator nos permite ejecutar un comando y que su standard output pasen como input para un siguiente comando y así encadenar comandos.

Echo es para generar una salida al standard input con cualquier mensaje

> echo "Hola Mundo"

Cat de hecho sirve para contacternar archivos:

> cat errot.txt output.txt

Ahora si al pipe operator

> ls -lh | less
>
> ls -lh | tee output.txt | less
>
> ls -lh Pictures | sort | tee list-pictures.txt | less
>
> sudo apt install cowsay lolcat
>
> cowsay "Hola"
>
> echo "Hola Mundo" | lolcat
>
> conwsay "Hola amigos" | lolcat

## Encadenando comandos: operadores de control

Los operadores de control son simbolos reservados por la terminal que nos permiten ejecutar más de un comando. Síncrona, asíncrona, incluso con condicionales.

Comandos de manera síncrona sería así:

> ls; mkdir hola; cal

Los comandos separados por ; se ejecutan uno seguido del otro en el orden en que fueron puestos. Uno no se ejecuta hasta que el otro haya terminado.

Ahora ejecutarlos de manera asíncrona sería de la siguiente manera. Por cada comando va a abrir un hilo separado de la terminal.

> ls & date & cal

Los comandos separados por & se ejecutan todos al mismo tiempo.

Ahora para correr comandos de manera condicional, es decir si se ejecuta uno satisfactoriamnete entonces que ejecute el siguiente, sería así:

> mkdir test && cd test && pwd

También podrías utilizar un operador "or" que es ||

> cd not-existent-directory || touch archivo.txt

## Cómo se manejan los permisos

**Tipos de archivos**

1. Atributo (-): Un archivo normal
2. Atributo (d): Un directorio
3. Atributo (l): Un link simbólico
4. Atributo (b): Un archivo de bloque especial. Son archivos que manejan la información de los bloques de datos como una USB.

**Tipos de modo**

1. Dueño: rwx (111)
2. Grupo: r-x (101)
3. World (Others): r-x (101)

Cada una de las categorías puede tener permisos de read, write y execute. Los permisos se pueden manejar de modo octal, rwx = 7, r-x = 5, r-- = 4, -w- = 2, --x = 1.

**Modo simbólico**

- u: Solo para el usuario.
- g: Solo para el grupo.
- o: solo para otros (es el world).
- a: Aplica para todos.

## Modificando permisos en la terminal

> mkdir sandbo
>
> cd sandbox

Esto crea un archivo:

> > mitexto.txt
>
> cat > mitexto.txt
>
> Hola amigos
>
> ls -l

```
-rw-r--r-- 1 user group date mitexto.txt
```

> chmod 755 mitexto.txt

```
-rwxr-xr-x 1 user group date mitexto.txt
```

> chmod u-r mitexto.txt
>
> chmod u-x, go=w mitexto.txt

Estos comandos son para saber con que usuario estamos:

> whoami
>
> id

Para cambiar de usuario:

> su root
>
> touch rootfile

El home de root es /root

> sudo rm rootfile

Para cambiar mi contraseña

> passwd

Los links simbolicos son un tipo de archivo que hace referencia a algún lugar.

> ln -s Documents/Dev Desarrollo

Los links simbólicos son como un acceso directo.

## Variables de entorno

La terminal tiene una configuración, esta configuración y otras variables del sistema se les puede acceder a traves de las variables de entorno.

Para ver todas las variables de entorno ejecutamos:

> printenv

Podemos imprimir una variable de entorno con el comando echo:

> echo $HOME
>
> echo $PATH

Las variablesd e entorno puedo modificarlas para mi usuario, modificando el archivo .bashrc o si estoy usando zsh es el .zshrc

> code .bashrc

En el .bashrc podemos crear alias, por ejemplo:

```bash
alias l='ls lh'
```

Crear variables de entorno

```bash
MESSAGE='Buenos días'
```

Puedo volver a ejecutar bash para que se vean los cambios:

> bash
>
> echo $MESSAGE

Para anexar a nuestra variable path

```bash
PATH=$PATH:/home/myuser/bin
```

**Recomendaciones**

1. Nunca creemos alias de comandos que ya existen
2. Podemos crear alias de git, ejemplo alias gpom="git push origin main"

## Comandos de búsqueda

Estos nos ayudan a encontrar archivos y directorios.

El comando which nos ayuda a encontrar la ruta de nuestros binarios, which busca en todas las rutas del PATH para buscar un comando.

> which code
>
> which obs

El comando find nos permite encontrar un archivo, el formato es find ruta-desde-donde-empieza-a-buscar -name nombre-del-archivo

> find ./ -name \*.txt | less

En find podemos buscar por tipos:

> find ./ -type d -name Documents
>
> find ./ -type f -name \*.log

Se puede buscar por tamaño, aquí todos los mayores o iguales a 20M

> find ./ -size 20M

Con find podemos ponerle la opción exec para ejecutar un comando luego del find

> find . -name "file-to-find" -exec rm -rf {} \;

## Su majestad: grep

Uno de los comandos más útiles que hay en la terminal. Grep nos permite encontrar coincidencias de una búsqueda dentro de un texto.

> grep Towers movies.csv
>
> grep the movies.csv

Podemos colocarle la opción -i en grep para hacer una búsqueda ignorando el si son mayúculas o minúsculas.

> grep -i the movies.csv | less

Con la opción -c nos cuenta cuantas coinciden

> grep -c the movies.csv
>
> grep -ci the movies.csv

Para encontrar todas aquellas que no cohincidan es la opción -v

> grep -vi towers movies.csv

Esta el comando word count (wc)

> wc movies.csv
>
> wc -l movies.csv
>
> wc -w movies.csv
>
> wc -c movies.csv

# Utilidades de la terminal

## Utilidades de red

Para ver información de nuestra red podemos utilizar

> ifconfig

La otra herramienta muy útil es ping

> ping www.google.com

También esta curl para traer un archivo a través de la red como texto, básicamente nos devolvería el html de la petición.

> curl wwww.google.com

También para traernos cosas de internet, por ejemplo para descargar las cosas directamente en la computadora.

> wget www.google.com

Para ver por todos los puntos por los que vamos pasando cuando tratamos de llegar a un servidor, por ejemplo:

> traceroute www.google.com

También con netstat podemos ver los dispositivos de red:

> netstat -i

## Comprimiendo archivos

> mkdir ToCompress
>
> cd ToCompress
>
> touch file1 file2 file3
>
> cd ..
>
> tree ToCompress

Tar para empaquetar...

> tar -cvf ToCompress.tar ToCompress

Tar para comprimir...

> tar -cvzf ToCompress.tar.gz ToCompress

Tar para descomprimir...

> tar -xzvf ToCompress.tar.gz

Para comprimir con zip...

> zip -r ToCompressInZip.zip ToCompress

Para descomprimir usamos unzip

> unzip ToCompressInZip.zip

## Manejo de procesos

Para ver que procesos están corriendo:

> ps

Para matar un proceso, lo hacemos con kill con su PID

> kill 20523

Para ver como el task manager podemos utilizar top

> top
>
> h
>
> q

## Procesos en foreground y background

Ejecutemos:

> cat > mi_nota.txt

Podemos escribir algo y terminar el input de texto con Ctrl + D. Pero no hagamos eso, suspendamos el proceso con Ctrl + Z.

Nuestro proceso se suspende y se queda en el background. Podemos ver los procesos en background con jobs:

> jobs

El trabajo podemos traerlo al foreground con el id que nos muestra el comando jobs

> fg 1

o en zsh

> fg %1

**Otras formas de enviar trabajos al background**

cat > mi_nota.txt &

Ahora para dejar un proceso ejecutandose en background, digamos que abrimos el chrome desde la terminal:

> google-chrome-stable

Y luego en la terminal presionamos Ctrl+Z entonces efectivamente el proceso se va al background pero queda detenido y no podemos interactuar con la ventana del chrome...

> jobs

Al ejecutar jobs podemos ver que nos muestra el id del job en el background, entonces podemos dejarlo ejecutando en background con bg:

> bg 1

## Editores de texto en la terminal

Hay diferente opciones de editores de texto de terminal como: emacs, nano, vi y vim... (vi es el más viejo y vim es el más nuevo)

> vim index.html

- i: Para insertar texto.
- Esc: Regresar al modo normal

## Personalizar la terminal de comandos

Instalamos el emulador de terminal llamado tilix

https://gnunn1.github.io/tilix-web/

> sudo pacman -S tilix

Instalar zsh

> sudo pacmang -S zsh
>
> zsh --version

Ahora cambiamos la shell por defecto:

> chsh -s $(which zsh)

Luego le instalamos oh-my-zsh

https://ohmyz.sh/

Luego instalarmos el tema powerlevel10k

https://github.com/romkatv/powerlevel10k

> git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
>
> vim .zshrc

```bash
ZSH_THEME="powerlevel10k/powerlevel10k"
```

Descargamos e instalamos las fuentes del tema powelevel10k

# Despedida

## Nunca pares de hackear

Libros recomendados:

https://nostarch.com/linuxbasicsforhackers

https://nostarch.com/tlcl2

https://www.oreilly.com/library/view/grep-pocket-reference/9780596157005/

https://www.oreilly.com/library/view/learning-the-vi/9780596529833/

https://www.oreilly.com/library/view/linux-pocket-guide/9781491927557/

https://www.oreilly.com/library/view/regular-expression-pocket/9780596514273/
