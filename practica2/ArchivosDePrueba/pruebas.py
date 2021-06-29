
import random

diccionario_abc = {"A": 'A', "B": 'B', "C": 'C', "D": 'D', "E": 'E', "F": 'F', "G": 'G', "H": 'H', "I": 'I', "J": 'J',
               "K": 'K', ".": " ", "*": "*"}
x = 3
matriz = []
z = 0
l = 0
for i in range(3):
    matriz.append([" "] * 3)
while z < 2:
    rand_r = random.randint(0, 3 - 1)
    rand_c = random.randint(0, 3 - 1)
    if matriz[rand_r][rand_c] == " ":
        matriz[rand_r][rand_c] = diccionario_abc["*"]
        z = z +1
while l < 2:
    rand_r = random.randint(0, 3 - 1)
    rand_c = random.randint(0, 3 - 1)
    if matriz[rand_r][rand_c] != diccionario_abc["*"]:
        matriz[rand_r][rand_c] = diccionario_abc["A"]
        l = l +1

espacio = 0
null = " "
a = 0
while a < x:
    print("+-" + ("-" * int(espacio)), end="")
    a += 1
print("+", end="")
print()
for r in range(x):
    for c in range(x):
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
    while a < x:
        print("+-" + ("-" * int(espacio)), end="")
        a += 1
    print("+", end="")
    print()


hayhueco = True
f = 1
c = x-2
q = f + c
while hayhueco == True and q < x:
    if matriz [r] [q] == " ":
        hayhueco= True
        f = f + 1
        q = f + c
    else:
        c = c - 1
        hayhueco = False



espacio = 0
null = " "
a = 0
while a < x:
    print("+-" + ("-" * int(espacio)), end="")
    a += 1
print("+", end="")
print()
for r in range(x):
    for c in range(x):
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
    while a < x:
        print("+-" + ("-" * int(espacio)), end="")
        a += 1
    print("+", end="")
    print()