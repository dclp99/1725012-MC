#Definicion de Algoritmos
#BUBBLE

def bubble(A):
	c=0
	for i in range(1,len(A)):
		for j in range(0,len(A)-1):
			c+=1
			if(A[j+1]<A[j]):
				aux=A[j]
				A[j]=A[j+1]
				A[j+1]=aux
	print(c)
	return c
        

        

#INSERTION


def insertion(arreglo): 
	con=0
	for indice in range(1,len(arreglo)):
		valor=arreglo[indice] 
		i=indice-1 
		while i>=0: 
			con+=1
			
			if valor<arreglo[i]:  
				arreglo[i+1]=arreglo[i]  
				arreglo[i]=valor
				i-=1
				
			else:
				break
	print(con)
	return con
	
        
#SELECTION

def selection(lis):
	co=0 
	for i in range(0,len(lis)-1):
		v=i
		
		for j in range(i+1,len(lis)):
			co+=1
			if lis[j]<lis[v]:
				v=j	
		if v !=-1:
			aux=lis[i]
			lis[i]=lis[v]
			lis[v]=aux
	print(co)
	return co
	

#QUICKSORT
cn=0
def quicksort(lis):
        global cn
        if lis==[] :
                return []
        a=lis[0]
        b=[]
        c=[]
        for i in lis[1:]:
                if i<a:
                        b.append(i)
                else:
                        c.append(i)
                        cn+=1
        
        
        return quicksort(b)+[a]+quicksort(c)

#1era prueba con 50 elementos
import random
W = random.sample(range(0,1000),50)
print(W)
print("Prueba valores de c")
import copy
#Creamos una copia del arreglo generado con ayuda de la fn copy para poder usarla individualmente con cada algoritmo
B,D,E,F =  copy.deepcopy(W), copy.deepcopy(W), copy.deepcopy(W), copy.deepcopy(W)
bubble(B)
insertion(D)
selection(E)
ss=quicksort(F)

print(cn)
print(B)
print(D)
print(E)
print(ss)



#Nota
#Probe 7-8 veces el programa cambiando el numero de elementos que queria que generara en el arreglo
#Los resultados obtenidos fueron recolectados en la tabla que aparece en el pdf
#Los resultados del contador dependen del arreglo generado aleatoriamente
#por lo que si se vuelve a probar para 50,100,150,.. valores pueden diferir en solo unas cifras
#No supe como ponerlo en un ciclo para que generara ciertos arreglos de cierta magnitud o de ciertos elementos
#por eso hice las pruebas individuales y genere la tabla con su grafica, la tabla fue hecha en excel
#El codigo imprime el arreglo generado, despues la variable contador y por ultimo el arreglo ordenado con cada algoritmo
