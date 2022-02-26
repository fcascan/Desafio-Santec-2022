#!/bin/python3

# import math
import os
# import random
# import re
import sys



#%%
# Complete the 'maximumPoints' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY costs
#
#%%
# Fernando Castro Canosa - 26/02/2022
# Desafio Academia Santec 2022
# Implementacion en Python 3
#
#%%
# Tests for debugging:
#
# k=10
# costs = [5, 2, 3, 1, 4]
# print("Puntos ejemplo1: ", maximumPoints(k, costs)) #Clean: 3 ; Skip: 4
#
# k=4
# costs = [4,0,0,0]
# print("Puntos ejemplo2: ", maximumPoints(k, costs)) #Clean: 4 ; Skip el 4: 3 (resuelto)    
#    
# k=2
# costs = [4,1,1,5]
# print("Puntos ejemplo3: ", maximumPoints(k, costs)) #Clean: 0 ; Skip al 4: 2 ; Skip al 5: 0 (resuelto)
# 
#%% Funciones:
def maximumPoints(k, costs):
    '''
    Descripcion: Funcion que permite simular la cantidad maxima de puntos obtenibles en un juego por niveles (1 nivel completado = 1 punto). Se recibe el monto inicial disponible (k), y una lista con los precios para ingresar cada nivel (costs). Se tiene en cuenta que es posible saltear un solo nivel de esa lista.
    Parametros: int k, int costs[n]
    Condiciones: 1 <= k <= 10e9 ; 1 <= n <= 10e5 ; 1 < costs[i] < 10e9
    Retorno: int points
    '''
    points_clean = 0
    k_clean = k
    points_skip = 0
    k_skip = k    
    
    #Primero veo de no saltear ningun nivel para garantizar 1 punto extra:
    for i in range(0, len(costs)):
        if k_clean >= costs[i]:
            k_clean = k_clean - costs[i]
            points_clean = points_clean + 1
        else:
            break            
    
    #Ahora evaluo si me conviene jugar salteando alguno de los niveles a ver si llego mas lejos:
    for level_to_skip in range(0, len(costs)):
        points_temp = 0
        for i in range(0, len(costs)):            
            if i == level_to_skip:
                continue
            if k_skip >= costs[i]:
                k_skip = k_skip - costs[i]
                points_temp = points_temp + 1
                if points_skip < points_temp:
                    points_skip = points_temp
            else:
                break                
    
    #Devuelvo la cantidad maxima de puntos alcanzables:
    if points_skip > points_clean:
        return points_skip
    else:
        return points_clean
    

#%% Programa principal:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    costs_count = int(input().strip())

    costs = []

    for _ in range(costs_count):
        costs_item = int(input().strip())
        costs.append(costs_item)

    result = maximumPoints(k, costs)

    fptr.write(str(result) + '\n')

    fptr.close()
