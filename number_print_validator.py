#right to left
import sys
number=int(input())
current=sys.maxsize
while(number>0):
    rem=number%10
    if(rem<current):
        current=rem
    else:
        print("NO")
        sys.exit()
    number=number//10
print("YES")
#left to right
number=input()
is_true=True
for i in range(len(number)-1):
    if number[i]>number[i+1]:
        is_true=False
        break
if is_true:
    print("YES")
else:
    print("NO")


