balance=int(input())
n=int(input())
for _ in range(n):
    amount=int(input())
    if amount%100==0 and amount<=balance:
        print("SUCCESS")
        balance-=amount
    else:
        print("FAILED")
print(balance)