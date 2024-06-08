def lcm(a,b):
    if(a>b):
        greater=0
    else:
        greater=b
        while True:
            if(greater %a==0 and greater %b==0):
                lcm=greater
                break
            else:    
                greater+=1
                return greater
                a=int(input("enter  the number"))
                b=int(input("enter the number"))
                X=lcm(a,b)
                print("the lcm of a and b is",X)