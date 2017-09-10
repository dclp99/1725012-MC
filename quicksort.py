#Algoritmo de ordenamiento quicksort

c=0 #declaracion de variable contador
#def de quicksort
def quicksort(x):
    global c
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        c+=1 
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part
    
#Programa Principal    
alist = [54,26,100,17,77,31,44,55,20]
print(alist)#arreglo inicial
quicksort(alist)#implementando quicksort
print(alist)#arreglo ordenado
print(c) #numero de iteraciones 