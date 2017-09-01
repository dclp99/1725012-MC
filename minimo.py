c=0 #variable contador
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
w=random.sample(range(0,200),50)
print(w)
wsort=orden(w)
print(c)
print(wsort)
