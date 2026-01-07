binary_number=int(input())
i=0
decimal_number=0
while(binary_number>0):
    rem=binary_number%10
    if rem==1:
        decimal_number+=2**i
    i+=1
    binary_number//=10
print(decimal_number)

