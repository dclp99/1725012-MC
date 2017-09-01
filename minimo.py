c=0
def minimo(arreglo):
    x=arreglo[0]
    global c
    for y in arreglo:
        c+=1
        if(y<x):
            x=y
    return x

def ordenar(arreglo):
    aux=arreglo[:]
    arreglosort=[]
    for x in range(len(aux)):
        y=minimo(aux)
        aux.remove(y)
        arreglosort.append(y)
    return arreglosort

import random
p=random.sample(range(0,150),50)
print(p)
psort=ordenar(p)
print(c)
print(psort)
