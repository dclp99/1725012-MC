c=0
def minimo(vec): #definicion de la funcion minimo
    x=vec[0]
    global c
    for y in vec:
        c+=1
        if(x<y):
            y=x
    return x

def orden(vec): #definicion de la funcion ordenar
    aux=vec[:]
    vecsort=[]
    for x in range(len(vec)):
        y=minimo(aux)
        aux.remove(y)
        vecsort.append(y)
    return vecsort

import random
p=random.sample(range(0,100),40)
print(p)
psort=orden(p)
print(c)
print(psort)
