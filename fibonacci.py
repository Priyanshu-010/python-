def fibo(n):
    if(n<0):
        print("Incorrect input")
    elif(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))
n=int(input("enter the number of sequence to be genrated:"))
for i in range(n):
    print(fibo(i))
