distance=int(input())
age=int(input())
fare=distance*2
if(age>=60):
    fare=fare-(fare*30/100)
elif age<12:
    fare=fare-(fare*50/100)
print(int(fare))