n=int(input("enter the value:"))
x=n
a=[]
while(n>0):
    digit=n%2
    a.append(digit)
    n=n//2
    a.reverse()
    print("the decimal equivalance of(0) in".format(n))
    for i in a:
        print(i,end="")