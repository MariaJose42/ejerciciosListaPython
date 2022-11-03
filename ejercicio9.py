# Ejercicio 9 #

'''
Implementar la siguientes funciones 
        - sumaVector(<Lista>) devuelve <Entero>.
        - sumaVectorDeVector(<Lista>) devuelve <Entero>.
        
      
              
'''
import random

def crearlst_random():
    lst=[]
    for i in range(0,random.randint(0,10)):
        lst.append(random.randint(0,50))
    return lst
    

# Dado una lista con números enteros devolver la suma
#de todos ellos por ejemplo:
              # sumaVector([1,2,3]) -->  6
              # sumaVector([3,4]) --> 7
              
def sumaVector(lst):
    #print(lst)
    sumaTotal = 0
    for i in range (0,len(lst)):
        sumaTotal= sumaTotal + lst[i]
        
    return sumaTotal        

# Dado una lista con listas de números enteros
#devolver la suma de todos ellos por ejemplo:
              # sumaVectorDeVector([[1,2],[3,4],[5,6,7]]) --> 28

def sumaVectorDeVector(lst1,lst2):
    resultado=0
    print(lst1)
    print(lst2)
    resultado= sumaVector(lst1) + sumaVector(lst2)
    return resultado
