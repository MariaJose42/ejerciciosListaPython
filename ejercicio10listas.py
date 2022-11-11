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
    sumMatriz=[]
    matriz1=crear_matriz(5)
    matriz2=crear_matriz(5)
    print("A:")
    print(matriz1)
    print("B:")
    print(matriz2)
    
    for i in range(0,len(matriz1)):
        #print("Iteración: ", i)
        #print(matriz1[i])
        #print(matriz2[i])
        lst_aux=[]
        
        for j in range(0,len(matriz1[i])):
            suma_aux = matriz1[i][j]+matriz2[i][j]
            lst_aux.append(suma_aux)
        sumMatriz.append(lst_aux)
        
    return sumMatriz

'''
Crea dos matrices y realiza la RESTA.
(Tienen que ser matrices equidimensionales)
    M_A = M_B - M_C
'''

def resta_matriz():
    resMatriz=[]
    matriz1=crear_matriz(5)
    matriz2=crear_matriz(5)
    print("A:")
    print(matriz1)
    print("B:")
    print(matriz2)
    
    for i in range(0,len(matriz1)):
        lst_aux=[]
        for j in range(0,len(matriz1[i])):
            resta_aux = matriz1[i][j] - matriz2[i][j]
            lst_aux.append(resta_aux)
        resMatriz.append(lst_aux)
        
    return resMatriz
        
'''
Producto de un número por una MATRIZ.
'''

def numXmatriz(n):
    mulMatriz=[]
    matriz1= crear_matriz(4)
    print(n, "x", matriz1)
    for i in range (0,len(matriz1)):
        #print(matriz1[i])
        lst_aux=[]
        for j in matriz1[i]:
            #print(j)
            multiplicación=j*n
            lst_aux.append(multiplicación)
        mulMatriz.append(lst_aux)
    
    return mulMatriz

matriz1=[[2,0,1],[3,0,0],[5,1,1]]
matriz2=[[1,0,1],[1,2,1],[1,1,0]]

'''
def matrizT(matriz2):
    matriz_b=[]
    for i in range(0,len(matriz2)):
        fila_aux=[]
        for j in range(0,len(matriz2[i])):
            fila_aux.append(matriz2[j][i])
        matriz_b.append(fila_aux)    
    return matriz_b
'''

def obtenerColumnaMatriz(pos,matriz2):
    vector=[]
    for i in range (0,len(matriz2)):
        vector.append(matriz2[i][pos])    
    return vector
    
  
def auxSumaMultvectores(vector1,vector2):
    res=0
    for i in range(0,len(vector1)):
        res += vector1[i]*vector2[i]
    return res
    
    
def multMatrices(matriz1,matriz2):
    matriz=[]
    for i in matriz1:
        vector=[]
        for j in range (0,len(matriz2)):
            vector_aux= obtenerColumnaMatriz(j,matriz2)
            vector.append(auxVectoresSumaMult(i,vect_aux))
        matriz.append(vector)
    
    return matriz
    
    