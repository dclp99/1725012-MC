#Algoritmo para saber si un numero es primo

def primo(n):
    global cnt
   
    for i in range (2,round(n**(1/2)+1)):
            cnt=cnt+1
            if ((n%i)==0):
                return ("No es primo")

    return ("Es primo")
    
#Ciclo para saber si el numero dado es primo o no, con un rango de 2 al 35
for i in range(2,36):
    cnt=0
    primo(i)
    print(i,cnt)
    
   
