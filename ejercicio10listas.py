# Ejercicio 10 #
'''
Crear un programa que cree un matriz de 5 x 5 con números aleatorios.
'''

import random

def crear_fila(n):
    fila=[]
    for i in range(0,n):
        fila.append(random.randint(0,10))
    return fila

def crear_matriz(n):
    matriz=[]
    while(len(matriz)<n):
        matriz.append(crear_fila(n))
    return matriz
                
'''
Crea dos matrices y realiza la SUMA
(Tienen que ser matrices equidimensionales)
    M_A= M_B + M_C
'''

def suma_matriz():
    matriz1=crear_matriz(5)
    matriz2=crear_matriz(5)
    resMatriz=[]
    
    for i in range(0,len(matriz1)):
        print("Iteración: ", i)
        print(matriz1[i])
        print(matriz2[i])
        lst_aux=[]
        for j in range(0,len(matriz1[i])):
            suma_aux= matriz1[i][j]+matriz2[i][j]
            lst_aux.append(suma_aux)
                           
    return resMatriz
