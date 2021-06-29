'''
CURSO:2019/2020
ASIGNATURA: PARADIGMAS DE PROGRAMACION
GRUPO 3
PRACTICA 1:El tercer clon (I)
@author: MIGUEL CHAVEINTE GARCIA
@author: ABDURRAHIM ALI ALI
'''

#!/usr/bin/python3
import random
import copy

diccionario_2048 = {"A": "2", "B": "4", "C": "8", "D": "16", "E": "32", "F": "64", "G": "128", "H": "256", "I": "512",
                    "J": "1024",
                    "K": "2048", ".": " ", "*": "****"}
diccionario_1024 = {"A": "1", "B": "2", "C": "4", "D": "8", "E": "16", "F": "32", "G": "64", "H": "128", "I": "256",
                    "J": "512", "K": "1024",
                    ".": " ", "*": "****"}
diccionario_abc = {"A": 'A', "B": 'B', "C": 'C', "D": 'D', "E": 'E', "F": 'F', "G": 'G', "H": 'H', "I": 'I', "J": 'J',
                   "K": 'K', ".": " ", "*": "*"}
diccionario_nivel = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8", "I": "9",
                     "J": "10", "K": "11", ".": " ", "*": "**"}

puntos = 0
movimientos = 0


class PP:

    def cambiar_diccionario(matriz, size, diccionario_antiguo, diccionario_nuevo):
        """ Docstring
        :param matriz: Recibimos la matriz a recorrer
        :param size: Tomamos el tamano de la matriz como parametro para poder recorrerla
        :param diccionario_antiguo: Llamamos diccionario antiguo al que usuaba el usuario previamente antes de elegir uno nuevo
        :param diccionario_nuevo: Eleccion nueva de modo de juego

        :arg: Se trata de recorrer la matriz, leyendo cada valor de la misma e ir cambiandolo segun su Key en el nuevo diccionario, ya que
        las Keys son comunes para todos los diccionarios, leemos valor y devolvemos la Key, despues asginamos a ese espacio el valor
        correspondiente segun la Key devuelta anteriormente pero en el nuevo diccionario

        :return: matriz: Ya modificada en su nuevo modo y cambiando su aspecto
        """
        for r in range(size):
            for c in range(size):
                if matriz[r][c] != " ":
                    clave = [key for key, value in diccionario_antiguo.items() if
                             value == matriz[r][c]]  # RETURN DE KEY A PARTIR DE VALOR
                    asignar = clave[0]
                    matriz[r][c] = diccionario_nuevo[asignar]
        return matriz

    def goOn(matriz, mat_size, diccionario_actual):
        """ Docstring
        :param matriz: Recibimos matriz para recorrerla.
        :param mat_size: Tamano de matriz para poder recorrer la misma.
        :param diccionario_actual: Necesitamos el diccionario con el que juega el usuario para adaptarnos al numero de *.
        :return: Boolean: Continua nos indica si el juego puede continuar si encontramos un espacio en blanco disponible
        en la matriz
        """
        continua = False
        for r in range(mat_size):
            for c in range(mat_size):
                if matriz[r][c] == diccionario_actual["."] and matriz[r][c] != diccionario_actual["*"]:
                    continua = True
        return continua

    def endGame(matriz, mat_size, diccionario_actual):
        """ Docstring
        :param matriz: Recibimos matriz para recorrerla.
        :param mat_size: Tamano de matriz para poder recorrer la misma.
        :param diccionario_actual: Necesitamos el diccionario con el que juega el usuario para adaptarnos al numero de *.
        Y tambien el valor maximo segun el el modo de juego empleado por el usuario.

        :arg: En este metodo lo que realizamos son una serie de comprobaciones esenciales para poder saber si el programa
        debe detener su ejecucion, nos basamos en recibir la matriz con el nuevo bloque ya insertado y comprobamos que
        no existe un espacio en blanco disponible y que no hay fusion posible, cuando se cumplen estos requisitos, devolvemos
        un True y con esto  acaba la ejecucion del codigo. Tambien si al recorrer la matriz conseguimos encontrar un bloque
        de nivel maximo, con esto el juego tambien concluye.

        :return: endGame, es un booleano que nos permite saber si el juego ha terminado o no.
        """
        continua = PP.goOn(matriz, mat_size, diccionario_actual)
        endGame = False
        fusion = False
        for r in range(mat_size):
            for c in range(mat_size):
                valor = matriz[r][c]
                if valor == diccionario_actual["K"]:
                    endGame = True
                    return endGame
        for r in range(mat_size):
            for c in range(mat_size - 1):
                if matriz[r][c] == matriz[r][c + 1] and matriz[r][c] != diccionario_actual["*"]:
                    fusion = True
        for c in range(mat_size):
            for r in range(mat_size - 1):
                if matriz[r][c] == matriz[r + 1][c] and matriz[r][c] != diccionario_actual["*"]:
                    fusion = True
        if continua == True:
            endGame = False
            return endGame
        if continua == False and fusion == False:
            endGame = True
        if continua == False and fusion == True:
            endGame = False
        return endGame

    def new_values(matriz, diccionario_actual, mat_size):
        """ Docstring
        :param matriz: Recibimos una matriz de la cual debemos verificar la existencia de un espacio disponible e insertar
        un nuevo bloque.
        :param diccionario_actual: Necesitamos el diccionario actual para poder insertar los bloques correspondientes
        al modo de juego que esta jugando el usuario.
        :param mat_size: Tamano de matriz para poder recorrerla.

        :arg Recibimos una matriz y nos ayudamos de un booleano en este caso val_in, lo utilizamos como condicion en un bucle
        while para asegurar que hemos podido calcular una posicion aleatoria y vacia y hemos insertado el nuevo bloque, con las
        probabilidades correspondientes.


        :return: matriz: Devolvemos una matriz con un nuevo bloque insertado.
        """
        val_in = False
        select_val = random.random()
        if select_val <= 0.75:
            new_val = diccionario_actual["A"]
        else:
            new_val = diccionario_actual["B"]
        while val_in != True:
            rrand = random.randint(0, mat_size - 1)
            crand = random.randint(0, mat_size - 1)
            if matriz[rrand][crand] == " ":
                matriz[rrand][crand] = new_val
                val_in = True
        return matriz

    def pnt_matrix(matriz, size, espacio, movimientos, puntos):
        """ Docstring
        :param matriz: Matriz a imprimir en pantalla
        :param size: Tamano para poder imprimirla
        :param espacio: Es un numero con el que hacemos referencia al espacio disponible en un bloque segun el modo de juego
        que el usuario haya elegido, asi podemos averiguar lo necesario y hacer los calculos para que salga la interfaz correspondiente
        :param movimientos: Numero de movimientos realizados por el usuario
        :param puntos: Numero de puntos sumados por el usuario

        :arg Nuestro metodo para conseguir la impresion en pantalla, construyendo la interfaz correspondiente segun modo de juego.
        """
        null = " "
        a = 0
        while a < size:
            print("+-" + ("-" * int(espacio)), end="")
            a += 1
        print("+", end="")
        print()
        for r in range(size):
            for c in range(size):
                print("|", end="")
                if espacio == 0:
                    print(matriz[r][c], end="")
                else:
                    if matriz[r][c] != "*" or matriz[r][c] != "**" or matriz[r][c] != "****":
                        print(matriz[r][c], end="")
                    else:
                        print((matriz[r][c]) * (espacio + 1), end="")
                    if len(str(matriz[r][c])) == 1:
                        print((null * (espacio)), end="")
                    elif len(str(matriz[r][c])) == 2:
                        print((null * (espacio - 1)), end="")
                    elif len(str(matriz[r][c])) == 3:
                        print((null * (espacio - 2)), end="")
            print("|", end='')
            print()
            a = 0
            while a < size:
                print("+-" + ("-" * int(espacio)), end="")
                a += 1
            print("+", end="")
            print()
        print("MOVIMIENTOS = ", movimientos, "|", "PUNTUACIÓN = ", puntos)

    def encontrar(entrada, busqueda):
        l1 = []
        length = len(entrada)
        index = 0
        while index < length:
            i = entrada.find(busqueda, index)
            if i == -1:
                return l1
            l1.append(i)
            index = i + 1
        return l1

    """
     Este metodo nos permitira guardar en una lista las posiciones donde tenemos un "*"
     Parametros de entrada:cadena donde buscar,parametro a buscar
     Parametros de salida: lista que indica el/los lugares(fila o columna) del "*"
    """
    def eleccion(matriz, size, inp, diccionario, nivel):
        global movimientos
        movimientos = movimientos + 1
        matriz_auxiliar = PP.cambiar_diccionario(matriz, size, diccionario, diccionario_abc)
        if inp == "I" or inp == "D":
            for r in range(size):
                lista = []
                for c in range(size):
                    list1 = str(matriz_auxiliar[r][c])
                    lista.append(list1)
                str1 = ''.join(lista)
                lugar = PP.encontrar(str1, "*")
                PP.movimiento(matriz, size, inp, diccionario, str1, lugar, r, c, nivel)

        else:
            for r in range(size):
                lista = []
                for c in range(size):
                    list1 = str(matriz_auxiliar[c][r])
                    lista.append(list1)
                str1 = ''.join(lista)
                lugar = PP.encontrar(str1, "*")
                PP.movimiento(matriz, size, inp, diccionario, str1, lugar, r, c, nivel)

    """
     Este metodo nos permitira recorrer la matriz según el movimiento e ir guardando en un string cada fila o columna
     correspondiente.Ademas sumamos un movimiento y llamamos a cambiar diccionario para segun el modo en el que estemos
     pasemos de forma indirecta al modo alfabeto con el que trabajaremos para los movimientos. Posteriormente llamamos
     una vez que tenemos la cadena a la funcion movimiento.
     Parametros de entrada:matriz, tamano matriz, orden de movimiento,diccionario actual,diccionario de nivel
     Salida: descarga en la funcion movimiento el control
    """
    def movimiento(matriz, size, inp, diccionario, str1, lugar, r, c, nivel):
        if inp == "S" or inp == "I":
            if len(lugar) == 0:
                cadena = str1.replace(" ", "")
                nuevacad = PP.arriba_y_izquierda(cadena, nivel)
                fincad = nuevacad.replace(" ", "")
                PP.nueva_matriz(matriz, size, lugar, fincad, inp, diccionario, r, c, 0)
            else:
                a = str1.split("*")
                i = 0
                cont = 0
                while i < len(a):
                    if a[i] != "":
                        cadena = a[i].replace(" ", "")
                        nuevacad = PP.arriba_y_izquierda(cadena, nivel)
                        fincad = nuevacad.replace(" ", "")
                        PP.nueva_matriz(matriz, size, lugar, fincad, inp, diccionario, r, i, cont)
                        cont = cont + 1
                    i = i + 1

        elif inp == "B" or inp == "D":
            if len(lugar) == 0:
                cadena = str1.replace(" ", "")
                nuevacad = PP.abajo_y_derecha(cadena, nivel)
                fincad = nuevacad.replace(" ", "")
                PP.nueva_matriz(matriz, size, lugar, fincad, inp, diccionario, r, c, 0)
            else:
                a = str1.split("*")
                i = 0
                cont = 0
                while i < len(a):
                    if a[i] != "":
                        cadena = a[i].replace(" ", "")
                        nuevacad = PP.abajo_y_derecha(cadena, nivel)
                        fincad = nuevacad.replace(" ", "")
                        PP.nueva_matriz(matriz, size, lugar, fincad, inp, diccionario, r, i, cont)
                        cont = cont + 1
                    i = i + 1

    """
     Este metodo nos permitira trabajar con el string y moldearle como nosotros queremos. Primero analizamos según el tipo
     de movimiento y posteriormente si hemos detectado algun * que se encontraran en lugar.Si no detectamos ninguno, quitamos
     los espacios en blanco, llamamos a la funcion que realiza el movimiento y la fusion y posteriormente volvemos a quitar
     los espacios en blanco y llamamos a nueva matriz que nos genera la matriz resultante. Si hay algun * debemos hacer un paso
     previo de comprobacion si en a hay algun "" que nos indicaria que ha habido dos asteriscos juntos y creamos en este caso
     otro contador que nos indicarian las cadenas que en realidad contienen datos
     Parametros de entrada:matriz, tamano matriz, orden de movimiento,diccionario actual,cadena recibida, lista del lugar
     de los "*" ,contadores de filas y columnas de recorrer la matriz y el diccionario nivel que lo utilizaremos para los puntos.
     Salida: descarga en la funcion nueva_matriz el control que nos proporciona la matriz resultante.
    """

    def abajo_y_derecha(cadrecibida, nivel):
        cadlista = list(cadrecibida)
        puntero = len(cadlista) - 1
        if len(cadlista) != 1:
            while puntero > 0:
                if cadlista[puntero] == cadlista[puntero - 1]:
                    cadlista[puntero - 1] = " "
                    a = nivel[cadlista[puntero]]
                    global puntos
                    nuevo = int(a) + 1
                    puntos = puntos + nuevo
                    clave = [key for key, value in nivel.items() if
                             value == str(nuevo)]  # RETURN DE KEY A PARTIR DE VALOR
                    asignar = clave[0]
                    cadlista[puntero] = str(asignar)

                puntero = puntero - 1

        cadena = ''.join(cadlista)
        return cadena

    """
     En este metodo pasamos a una lista la cadena recibida para poder recorrerla y mutarla. Esta al ser la estructura de abajo y derecha
     lo que hacemos es recorrerla de atras hacia delante y miramos si los valores del puntero y el anterior son iguales para
     proceder a su fusion. Si esto sucede mediante el diccionario de nivel accedemos al valor de lo que vale la letra(ya que hemos convertido
     el diccionario actual al diccionario abc para poder trabajar el movimiento) y con esto sumamos los puntos y conseguidos que la fusion
     se lleve acabo.Por ultimo juntamos en un string toda la lista.
     Parametros de entrada:el string sin espacios y el diccionario de nivel.
     Salida: retorna el string ya fusionado.
    """

    def arriba_y_izquierda(cadrecibida, nivel):
        cadlista = list(cadrecibida)
        puntero = len(cadlista) - 1
        i = 0
        while i < puntero:
            if cadlista[i] == cadlista[i + 1]:
                cadlista[i + 1] = " "
                a = nivel[cadlista[i]]
                global puntos
                nuevo = int(a) + 1
                puntos = puntos + nuevo
                clave = [key for key, value in nivel.items() if
                         value == str(nuevo)]  # RETURN DE KEY A PARTIR DE VALOR
                asignar = clave[0]
                cadlista[i] = str(asignar)
            i = i + 1

        cadena = ''.join(cadlista)
        return cadena

    # Mismo procedimiento ya comentado en la funcion abajo y derecha. Solo que en este caso empezamos a analizar la
    # cadena de alante hacia atras hasta la longitud maxima de la cadena.

    def nueva_matriz(matriz, size, lugar, fincad, inp, diccionario, pos, cont, bucle):
        if inp == "S":
            if bucle == 0:
                for r in range(size):
                    matriz[r][pos] = " "
            for r in range(len(lugar)):
                matriz[lugar[r]][pos] = diccionario["*"]
            if len(lugar) == 0:
                for i in range(len(fincad)):
                    matriz[i][pos] = diccionario[fincad[i]]
            else:
                if bucle == 0:
                    contador = 0
                    while matriz[0 + contador][pos] == diccionario["*"]:
                        contador = contador + 1
                    for i in range(len(fincad)):
                        matriz[contador + i][pos] = diccionario[fincad[i]]
                else:
                    contador = 0
                    while matriz[lugar[cont - 1] + contador][pos] == diccionario["*"]:
                        contador = contador + 1
                    for i in range(len(fincad)):
                        matriz[lugar[cont - 1] + contador + i][pos] = diccionario[fincad[i]]

        elif inp == "B":
            if bucle == 0:
                for r in range(size):
                    matriz[r][pos] = " "
            for r in range(len(lugar)):
                matriz[lugar[r]][pos] = diccionario["*"]
            if len(lugar) == 0:
                for i in range(len(fincad)):
                    matriz[size - 1 - i][pos] = diccionario[fincad[len(fincad) - 1 - i]]
            else:
                if bucle == 0:
                    if lugar[0] == 0:
                        contador = 0
                        while matriz[0 + contador][pos] == diccionario["*"]:
                            contador = contador + 1
                        j = 0
                        while (contador + j) <= (size - 1) and matriz[contador + j][pos] != diccionario["*"]:
                            j = j + 1
                        for i in range(len(fincad)):
                            matriz[contador + j - 1 - i][pos] = diccionario[fincad[len(fincad) - 1 - i]]
                    else:
                        contador = 0
                        while contador <= (size - 1) and matriz[0 + contador][pos] != diccionario["*"]:
                            contador = contador + 1
                        for i in range(len(fincad)):
                            matriz[contador - 1 - i][pos] = diccionario[fincad[len(fincad) - 1 - i]]
                else:
                    contador = 0
                    while matriz[lugar[cont - 1] + contador][pos] == diccionario["*"]:
                        contador = contador + 1
                    j = 0
                    while (lugar[cont - 1] + contador + j) <= (size - 1) and matriz[lugar[cont - 1] + contador + j][
                        pos] != diccionario["*"]:
                        j = j + 1
                    for i in range(len(fincad)):
                        matriz[lugar[cont - 1] + contador + j - 1 - i][pos] = diccionario[fincad[len(fincad) - 1 - i]]


        elif inp == "I":
            if bucle == 0:
                for r in range(size):
                    matriz[pos][r] = " "
            for r in range(len(lugar)):
                matriz[pos][lugar[r]] = diccionario["*"]
            if len(lugar) == 0:
                for i in range(len(fincad)):
                    matriz[pos][i] = diccionario[fincad[i]]
            else:
                if bucle == 0:
                    contador = 0
                    while matriz[pos][0 + contador] == diccionario["*"]:
                        contador = contador + 1
                    for i in range(len(fincad)):
                        matriz[pos][contador + i] = diccionario[fincad[i]]
                else:
                    contador = 0
                    while (lugar[cont - 1] + contador) <= (size - 1) and matriz[pos][lugar[cont - 1] + contador] == \
                            diccionario["*"]:
                        contador = contador + 1
                    for i in range(len(fincad)):
                        matriz[pos][lugar[cont - 1] + contador + i] = diccionario[fincad[i]]

        elif inp == "D":
            if bucle == 0:
                for r in range(size):
                    matriz[pos][r] = " "
            for r in range(len(lugar)):
                matriz[pos][lugar[r]] = diccionario["*"]
            if len(lugar) == 0:
                for i in range(len(fincad)):
                    matriz[pos][size - 1 - i] = diccionario[fincad[len(fincad) - 1 - i]]
            else:
                if bucle == 0:
                    if lugar[0] == 0:
                        contador = 0
                        while matriz[pos][0 + contador] == diccionario["*"]:
                            contador = contador + 1
                        j = 0
                        while (contador + j) <= (size - 1) and matriz[pos][contador + j] != diccionario["*"]:
                            j = j + 1
                        for i in range(len(fincad)):
                            matriz[pos][contador + j - 1 - i] = diccionario[fincad[len(fincad) - 1 - i]]
                    else:
                        contador = 0
                        while contador <= (size - 1) and matriz[pos][0 + contador] != diccionario["*"]:
                            contador = contador + 1
                        for i in range(len(fincad)):
                            matriz[pos][contador - 1 - i] = diccionario[fincad[len(fincad) - 1 - i]]
                else:
                    contador = 0
                    while matriz[pos][lugar[cont - 1] + contador] == diccionario["*"]:
                        contador = contador + 1
                    j = 0
                    while (lugar[cont - 1] + contador + j) <= (size - 1) and matriz[pos][
                        lugar[cont - 1] + contador + j] != diccionario["*"]:
                        j = j + 1
                    for i in range(len(fincad)):
                        matriz[pos][lugar[cont - 1] + contador + j - 1 - i] = diccionario[fincad[len(fincad) - 1 - i]]

    """
     En este proceso lo que realizamos es según el movimiento indicado, introducir los valores que formaran la nueva matriz.
     Lo primero que haremos será limpiar la matriz y llenar los huecos que tenian asteriscos haciendo caso del lugar donde estaban.
     Lo siguiente sera introducir las cadenas. Para ello distinguimos si es sin asteriscos o con ellos, ya que en el primer caso
     no debemos tener "cuidado" de las posiciones iniciales de las cadenas. En cuanto al segundo caso mediante desarollamos un algoritmo
     mediante el cual comprueba si se trata de la primera cadena u otra. Si es la primera empezamos a introducir los valores de esta justo
     tras los asteriscos pertinentes( para lo cual desarrollamos un contador para saber la poscion exacta donde empezar).Sino se trata de
     la primera cadena con otro contador de nuevo contamos desde la ultima posicion del asterisco correspondiente al indice que traemos
     por entrada. Y posteriormente esa cadeana la introducimos a partir de ese indica mas el contador.
     Parametros de entrada:la matriz,su tamano,lista con el lugar de los *,diccionario actual, la columna o fila donde se deben introducir,
     el contador de la cadena una vez separada tras los * y el otro contador que almacena el anterior pero sin contar donde la posicion del
     vector sea "".
     Salida: modifica los valores de la matriz a imprimir
    """
    def comparar(matriz, matriz_comparar, size):
        iguales = True
        for r in range(size):
            for c in range(size):
                if (matriz[r][c] != matriz_comparar[r][c]):
                    iguales = False

        return iguales

    """
     Esta funcion lo que hace es comparar si las dos matrices de entrada: la que teniamos comparada con la actualizada tras el movimiento
     Si son iguales en todos los elementos devuelve True, sino False.
     Precondicion: Las dos matrices tienen el mismo tamano
     Parametros de entrada:la matriz antigua y la actual y su tamaño
     Salida: boolean que nos indicara si todos sus elementos son iguales
    """

# MAIN EMPIEZA AQUI


matriz = []
main_acabado = False
endGame = False
while endGame != True:  #Bucle que ejecuta nuestro programa
    while not main_acabado:
        """ Aqui esta el codigo correspondiente para generar una nueva matriz al empezar el programa o cargar un fichero ya existente"""
        print(
            "‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐  CLON‐3  ‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐---  \n ‐ Práctica de Paradigmas de Programación 2019‐20 ‐ \n ‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐")
        matriz = []
        print(" 1. CREAR NUEVO TABLERO \n 2. LEER TABLERO DE FICHERO \n 3. SALIR ")

        inp_opcion = int(input("Indique opcion: "))

        if inp_opcion == 1:
            # crear tablero
            """Creacion de un nuevo tablero, con la insercion paso a paso de los distintos bloques."""
            mat_size = int(input("Indique tamano del tablero: "))
            obs_num = int(input("Numero de obstaculos: "))
            espacio = 3
            matriz = []
            s = 0
            z = 0
            for i in range(mat_size):
                matriz.append([" "] * mat_size)
            while z < obs_num:
                rand_r = random.randint(0, mat_size - 1)
                rand_c = random.randint(0, mat_size - 1)
                if matriz[rand_r][rand_c] == " ":
                    matriz[rand_r][rand_c] = "*" * (espacio + 1)
                    z = z + 1
                    espacio = 3
                    PP.pnt_matrix(matriz, mat_size, espacio, movimientos, puntos)
                    x = input("Pulsa [Enter] para mostrar el siguiente bloque")

            while 2 > s:
                pos_inic_r = random.randint(0, mat_size - 1)
                pos_inic_c = random.randint(0, mat_size - 1)
                dicci = random.choice("AB")
                if matriz[pos_inic_r][pos_inic_c] != "*" and matriz[pos_inic_r][pos_inic_c] == " ":
                    matriz[pos_inic_r][pos_inic_c] = diccionario_2048[dicci]
                    PP.pnt_matrix(matriz, mat_size, espacio, movimientos, puntos)
                    s = s + 1
                    if s <= 1:
                        x = input("Pulsa [Enter] para mostrar el siguiente bloque")
            diccionario_actual = diccionario_2048
            main_acabado = True

        elif inp_opcion == 2:
            '''Para generar un tablero segun un fichero guardado por el usuario anteriormente, primero le pedimos que nos indique el nombre del mismo, manejamos la excepcion que 
            se puede producir, que no encuentre ese archivo, y con la ayuda de un booleano podemos pedirle un nombre correcto y hasta que no sea asi, no hara otra cosa el programa'''
            # Abrir fichero y crear tablero

            r = -1

            matriz = []

            archivo = False

            while archivo != True:

                try:

                    cargar = input("Introduzca el nombre del fichero que desea cargar con la extension .txt: ")

                    partida = open(cargar, "r+")

                    archivo = True

                except FileNotFoundError:

                    print("Introduzca un archivo que exista")

            """Empezamos leyendo el tamano de la matriz que en nuestro caso nos resulta mas sencillo asi, tanto para guardar y cargar una partida, 
            contar simepre con el tamano de la matriz y no tener que calcularlo. Primera linea es por tanto el tamano de la matriz, segunda linea 
            es la cantidad de movimientos, la siguiente la puntuacion y asi vamos leyendo linea a linea hasta que tenemos la matriz rellena, 
            luego simplemente la imprimimos por consola."""

            mat_size = int(partida.readline())
            movimientos = int(partida.readline())
            puntos = int(partida.readline())

            for i in range(mat_size):
                matriz.append([" "] * mat_size)

            espacio = 3

            for position, line in enumerate(partida):

                r += 1

                for c in range(mat_size):
                    char = line[c]

                    matriz[r][c] = diccionario_2048[char]

            diccionario_actual = diccionario_2048

            PP.pnt_matrix(matriz, mat_size, espacio, movimientos, puntos)

            partida.close()

            main_acabado = True


        elif inp_opcion == 3:
            print("Esperamos volver a verle pronto :D")
            exit()

    inp = input("[S]ubir, [B]ajar, [I]zda, [D]cha | [M]odo, [G]uardar, [F]in: ")

    if inp == "S" or inp == "B" or inp == "I" or inp == "D":
        matriz_comparar = copy.deepcopy(matriz)  # copiamos la matriz antes de realizar el movimiento
        PP.eleccion(matriz, mat_size, inp, diccionario_actual,
                    diccionario_nivel)  # llamamos a la funcion que nos realizara todo aquello referente al movimiento
        igual = PP.comparar(matriz, matriz_comparar,
                            mat_size)  # llamamos a la funcion comparar que nos dira si la matriz anterior y la actual son iguales
        if igual:  # si son iguales restamos un movimientos ya que previamente se le habia sumado uno cuando la matriz es igual
            movimientos = movimientos - 1  # cuando la matriz resultante es igual y por tanto no introducimos un nuevo valor tampoco
        else:
            PP.pnt_matrix(matriz, mat_size, espacio, movimientos, puntos)
            x = input("Presione [Enter] para insercion de nuevo bloque")
            matriz = PP.new_values(matriz, diccionario_actual,
                                   mat_size)  # si  no es igual introducimos tras el movimiento un nuevo valor aleatorio entre 2 y 4 en una posicion vacia aleatoria


    elif inp == "M":
        print("ESCOJA MODO VISUALIZACION: \n 1. ALFABETO \n 2. NIVEL \n 3. 1024 \n 4. 2048 ")
        diccionario_num = int(input("ESCOJA OPCION: "))
        if diccionario_num == 1:
            diccionario_aux = diccionario_abc
            espacio = 0
        elif diccionario_num == 2:
            diccionario_aux = diccionario_nivel
            espacio = 1
        elif diccionario_num == 3:
            diccionario_aux = diccionario_1024
            espacio = 3
        elif diccionario_num == 4:
            diccionario_aux = diccionario_2048
            espacio = 3

        diccionario_antiguo = diccionario_actual

        matriz = PP.cambiar_diccionario(matriz, mat_size, diccionario_antiguo, diccionario_aux)

        diccionario_actual = diccionario_aux



    elif inp == "G":
        """ Para guardar, le pedimos al usuario el nombre con el que le gustaria guardar la partida, luego utilizamos
        las 3 primeras lineas para, el tamano de la matriz, movimientos y la puntuacion. Tras eso, recorremos la matriz
        y leemos el valor que existe en cada casilla y conseguimos almacenar en clave, la Key correspondiente a ese valor, 
        simplemente lo vamos escribiendo en el fichero, anadiendo un salto de linea cuando se llega al tamano de la matriz"""
        nombre_fich = input("Introduzca nombre del fichero, con la extension .txt: ")


        game_file = open(nombre_fich, "w+")
        game_file.write(str(mat_size))
        game_file.write("\n")
        game_file.write(str(movimientos))
        game_file.write("\n")
        game_file.write(str(puntos))
        game_file.write("\n")

        for r in range(mat_size):
            for c in range(mat_size):

                clave = [key for key, value in diccionario_actual.items() if
                         value == matriz[r][c]]  # RETURN DE KEY A PARTIR DE VALOR
                game_file.write(clave[0])

                if c == mat_size - 1:
                    game_file.write("\n")

        game_file.close()

        print("Guardado con exito :D")
    elif inp == "F":
        main_acabado = False        #Volvemos a empezar el menu principal

    if inp != "F":

        PP.pnt_matrix(matriz, mat_size, espacio, movimientos, puntos)
        endGame = PP.endGame(matriz, mat_size, diccionario_actual)
        if endGame:
            v = int(input("La partida ha terminado. \nDesea volver a jugar? \n[1] Volver a jugar\n[2] Salir del juego\nIntroduzca lo que desea hacer: "))  #Aqui si acaba el juego, ya sea porque no se pueden fusionar mas bloques o porque se ha alcanzado el bloque de nivel maximo, se le pregunta al usuario si desea volver a jugar.
            if v == 1:
                movimientos = 0
                puntos = 0
                endGame = False         #Reiniciamos ambos bucles para volver a empezar la ejecucion
                main_acabado = False
            if v == 2:
                print("Esperamos volver a verle pronto :D")
