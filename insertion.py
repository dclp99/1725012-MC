#insertion 

#definirInsertion
contador=0
def insercion(arreglo): 
	global contador
	for indice in range(1,len(arreglo)):
		valor=arreglo[indice] #valor es el elemento que vamos a comparar
		i=indice-1 #i es el valor anterior al elemento que estamos comparando
		while i>=0: 
			contador+=1
			if valor<arreglo[i]: #compraramos valor con el elemento anterior 
				arreglo[i+1]=arreglo[i] #intercambiamos los valores 
				arreglo[i]=valor
				i-=1 #decremento en 1 el valor de i
			else:
				break
	return arreglo


A=[20,34,53,12,11,3,45,76,89,100,24,201]
print(A)
insercion(A)
print(A)
print(contador)


