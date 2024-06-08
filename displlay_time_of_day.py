time=int(input("enter the time in 0000hrs format:"))
if(time>=600 and time<1200): 
    print("morning hours")
elif(time>=1200 and time<1700):
    print("afternoon hours")
elif(time>=1700 and time<2000):
    print("evening hours")
elif(time>=2000 and time<2400)or(time>=0000 and time<600):
    print("night hours")
else:
    print("invalid time")