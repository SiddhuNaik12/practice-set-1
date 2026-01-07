units=int(input())
bill=0
#first 100 units
if units>100:
    bill=bill+100*3
else:
    bill=bill+units*3
    print(bill)
    exit()
#next 100 units(101-200)
if units>200:
    bill=bill+100*5
else:
    bill=bill+(units-100)*5
    print(bill)
    exit()
# remaining units(201+)
bill=bill+(units-200)*8
#surcharge if units>300
if units>300:
    bill=bill+(bill*10/100)

#final bill
print(int(bill))

