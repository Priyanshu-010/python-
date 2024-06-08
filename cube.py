n=int(input("enter the number"))
t=n
s=0
while(n>0):
    d=n%10
    c=n**3
    s+=c
    n=n//10
    if t==s:
        print("the given number satisfies the given condition")
    else:
        print("the given number does not satisfy the given condition")