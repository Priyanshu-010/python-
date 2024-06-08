def hcf(a,b):
    if(a<b):
        smaller=a
    else:
        smaller=b
        for i in range(1,smaller+1):
            if(a%i==0 and b%i==0):
                hcf=i
                return hcf
                a=int(input("enter the number"))    
                b=int(input("enter the number"))
                x=hcf(a,b)
                print(x)