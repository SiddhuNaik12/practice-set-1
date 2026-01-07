time1=int(input())
time2=time1%90
if time2==0:
    time2=90
if(1<=time2<=30):
    print("RED")
elif(31<=time2<=45):
    print("YELLOW")
elif(46<=time2<=90):
    print("GREEN")