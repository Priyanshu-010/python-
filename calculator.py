a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=input("+,-,*,/,%")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)    
elif c=="/":
    print(a/b)
elif c=="*":
    print(a*b)    
elif c=="**":
    print(**b)
else:
    print(a%b)    