from random import randint
from math import sqrt
import numpy as np


def generarPuntos(cantidad):
    matriz = []
    if(cantidad > 0 and cantidad < 101):
        for i in range(0, cantidad):
            tmp = []
            x = randint(-25, 25)
            y = randint(-25, 25)
            tmp.append(x)
            tmp.append(y)
            matriz.append(tmp)
    else:
        print("El algoritmo seria muy lento para graficar")
        print("Use una cantidad positiva menor a 100")

    return matriz


def d(a, b):
    cuadrados = ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)
    return sqrt(cuadrados)


def elegirRep(vectores, cantidad):
        reps = []
        largo = len(vectores) - 1
        encontrados = 0

        while cantidad > encontrados:
            indice = randint(0, largo)

            if vectores[indice] not in reps:
                reps.append(vectores[indice])
                encontrados += 1

        return reps


def cardinalidad(lista):
    total = 0
    for i in range(len(lista)):
        total += lista[i]

    return total


def sumaVectores(a, b):
    a[0] += b[0]
    a[1] += b[1]
    return a


def actualizarVectores(vectores, reps, matriz):
    for i in range(len(matriz)):
        tmp = [0,0]
        c = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                tmp = sumaVectores(tmp, vectores[j])
                c += 1

        tmp[0] = tmp[0] / c
        tmp[1] = tmp[1] / c
        reps[i] = tmp

    return reps


def miminino(vectores, punto):
    mini = np.inf
    for i in range(len(vectores)):
        mini = min(mini, d(vectores[i], punto))

    return mini


def calcularMatriz(puntos, reps):
    matriz = []
    for s in range(len(reps)):
        tmp = []
        for r in range(len(puntos)):
            tmp.append(0)

        matriz.append(tmp)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if d(puntos[j], reps[i]) == miminino(reps, puntos[j]):
                matriz[i][j] = 1

            else:
                matriz[i][j] = 0

    return matriz


def calcularQ(matriz, puntos, reps):
    resq = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                resq += d(reps[i], puntos[j])

    return resq


def calcularS(matriz, puntos, reps, i):
    suma = 0
    for e in range(len(matriz[i])):
        if matriz[i][e] == 1:
            suma += d(puntos[e], reps[i])

    card = cardinalidad(matriz[i])
    return suma / card


def calcularDij(reps, i, j):
    return d(reps[i], reps[j]) ** 2


def calcularRij(matriz, puntos, reps, i, j):
    return (calcularS(matriz, puntos, reps, i) + calcularS(matriz, puntos, reps, j)) / calcularDij(reps, i, j)


def calcularRi(matriz, puntos, reps):
    maxR = -np.inf
    for i in range(len(reps)):
        for j in range(len(reps)):
            if i != j:
                tmpR = calcularRij(matriz, puntos, reps, i, j)
                if tmpR > maxR:
                    maxR = tmpR

    return maxR


def calcularRk(p):
    listaDeR = []
    for i in range(2, 5):
        cantidad = 50
        reps = elegirRep(p, i)
        terminado = False
        while not terminado:
            m = calcularMatriz(p, reps)
            q = calcularQ(m, p, reps)
            reps = actualizarVectores(p, reps, m)
            k = calcularQ(m, p, reps)
            diferencia = q - k
            if diferencia <  0.001 and diferencia > -0.001:
                terminado = True

        listaDeR.append(calcularRi(m, p, reps))

    mini = min(listaDeR)
    return listaDeR.index(mini) + 2


def combinarLista(a, b):
    return a + b