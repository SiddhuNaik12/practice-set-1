m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
if m1 <35 or m2<35 or m3<35 or m4<35 or m5 < 35 :
    print("FAIL")
elif (m1+m2+m3+m4+m5)/5 >=75:
    print("DISTINCTION")
else:
    print("FAIL")
