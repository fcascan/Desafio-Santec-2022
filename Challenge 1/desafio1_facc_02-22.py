#!/bin/python3

# import math
import os
# import random
# import re
import sys



#%%
# Complete the 'getMaximumGrossValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
#%%
# Fernando Castro Canosa - 26/02/2022
# Desafio Academia Santec 2022
# Implementacion en Python 3
#
#%%
# Tests for debugging:
# array = [-5,3,9,4]
# a = getSum(array, 0, 0)
# b = getSum(array, 0, 1)
# c = getSum(array, 1, 4)
# d = getSum(array, 4, 4)
# suma = getGrossValue(array,0,1,4)
# print ("Valor MAX bruto:", getMaximumGrossValue(array)) #tiene que dar 21
# 
# array2 = [-1,1,-2,-2]
# e = getSum(array2, 0, 0)
# f = getSum(array2, 0, 1)
# g = getSum(array2, 1, 2)
# h = getSum(array2, 2, len(array2))
# suma2 = getGrossValue(array2,0,1,2)
# print ("Valor MAX bruto:", getMaximumGrossValue(array2)) #tiene que dar 6
# 
# array3 = [4,-8,2,-10,3,-20]
# i = getSum(array3, 0, 1)
# j = getSum(array3, 1, 4)
# k = getSum(array3, 4, 5)
# l = getSum(array3, 5, len(array3))
# suma3 = getGrossValue(array3,1,4,5)
# print ("Valor MAX bruto:", getMaximumGrossValue(array3)) #tiene que dar 43
#%% Funciones
def getMaximumGrossValue(arr):
    '''
    Descripcion: Funcion que recibe un array de n enteros positivos, y retorna el maximo valor bruto (Maximum gross value) de cualquier tripleto valido de armar con en el mismo
    Parametros: int arr[n]
    Condiciones: 1 <= n <= 3000 ; -10e9 <= arr[i] <= 10e9 ; 1 <= i[i] <= i[i+1] <= ... <= i[n-1] <= n
    Retorno: int valor_max
    '''
    #variables para compensar el inicio y fin de las listas respecto a python:
    inicio = 0 #-1
    fin = len(arr)+1 #len(arr)
        
    #Verificacion de condiciones:
    if len(arr) <= 0 or len(arr) > 3000:
        raise RuntimeError("El array no cumple con las condiciones especificadas: su contenido excede 3000 elementos o esta vacio")
    
    #generacion de tripletos:
    valor_max = 0
    for x in range(inicio, fin):
        for y in range(x, fin):
            for z in range(y, fin):
                valor_actual = getGrossValue(arr, x, y, z)
                if valor_actual > valor_max:
                    valor_max = valor_actual     
    
    #retorno el valor bruto maximo alcanzando para el array
    return valor_max                    
    
        
def getGrossValue(arr, x, y ,z):
    '''
    Descripcion: Funcion que recibe un arr de 3 items, y retorna el valor bruto para ese tripleto (Maximum Gross Value)
    Parametros: int arr[n] ; int x, y, z
    Condiciones: arr[x] <= arr[y] <= arr[z] ; 1 <= x <= y <= z <= n
    Retorno: int ret
    '''
    valor = 0
    
    #Compruebo que se cumplan las condiciones:
    if x < 0 or z > len(arr) or x > y > z:
        raise RuntimeError("Se intento hallar el valor bruto de un array usando unos indices no acordes a las condiciones.")
    
    #condiciones de contorno corregidas para evitar desborde en python:    
    inicio = 0
    fin = len(arr)
        
    #realizar las sumas del tripleto solicitado
    valor = getSum(arr, inicio, x) - getSum(arr, x, y) + getSum(arr, y, z) - getSum(arr, z, fin)
    
    #Retorno el valor bruto correspondiente:
    return valor

    
def getSum(arr, l, r):
    '''
    Descripcion: Funcion que suma todos los elementos del array recibido como parametro, en el rango que va de l a r-1 inclusive. En caso que l==r se obtiene 0.
    Parametros: int arr[l,r]
    Condiciones: 0 <= l <= r <= n
    Retorno: int suma
    '''
    suma = 0    
    for i in range(l, r):    #range va de l hasta r-1
        if arr[i] < -10e9 or arr[i]> 10e9:
            raise RuntimeError("El array contiene un elemento con un valor que no cumple con las condiciones especificadas")
        if i >= 0 or i <= len(arr)-1:  #Not out of range      
            suma = suma + arr[i]
    return suma     
    
#%%
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMaximumGrossValue(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
