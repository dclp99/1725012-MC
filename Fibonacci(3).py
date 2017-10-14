
#Fibonacci(3)

arr= {}
c=0
def fibonacci(n):
    global arr,c
    c+=1
    if n==0 or n==1:
        return(1)
    if n in arr:
        return arr[n]
    else:
        val=fibonacci(n-2)+ fibonacci(n-1)
        arr[n]=val
        return val

#intervalo del 2 al 35
for i in range(2,35):
    cnt=0
    print(i,fibonacci(i),c)


