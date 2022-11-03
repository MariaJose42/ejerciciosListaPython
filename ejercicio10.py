# Ejercicio 10 #
'''
Crear un programa que cree un matriz de 5 x 5 con números aleatorios
'''

import random

def crear_fila():
    fila=[]
    for i in range(0,5):
        fila.append(random.randint(0,10))
    return fila

def crear_matriz():
    matriz=[]
    while(len(matriz)<5):
        matriz.append(crear_fila())
    for i in matriz:
        print (i)
