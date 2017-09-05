#Algoritmo de ordenacion Bubble

#declaracion de funciones
contador=0
def burbuja(A):
	global contador
	for i in range(1,len(A)):
		for j in range(0,len(A)-1):
			contador+=1
			if(A[j+1]<A[j]):
				aux=A[j]
				A[j]=A[j+1]
				A[j+1]=aux
	print(A)

#programa principal
A=[6,5,3,1,8,7,2,4]
print(A)
burbuja(A)
print(contador)
