#Algoritmo de ordenamiento selection
c=0 #declaracion de variable contador

#definir el algoritmo
def selection(lis):
	global c 
	for i in range(0,len(lis)-1):
		v=i
		for j in range(i+1,len(lis)):
			c= c+1
			if lis[j]<lis[v]:
				v=j	
		if v !=-1:
			aux=lis[i]
			lis[i]=lis[v]
			lis[v]=aux
	return c

#declaracion de una funcion para que nos de un arreglo de valores aleatorios del 0 la 100

import random 
#definicion de la funcion
def ran_n(n,lim_i=0,lim_s=100):
	lis=[]
	for i in range(n):
		lis.append(random.randint(lim_i,lim_s))
	return lis


#programa principal
A=ran_n(12) #generamos un arreglo	
print(A) #mostramos el arreglo generado
selection(A) #aplicamos el algoritmo al arreglo
print(A) #mostramos el arreglo ordenado
print(c) #mostramos el numero de iteraciones durante el cilo (cuantas veces se compraro)
