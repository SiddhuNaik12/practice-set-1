A=int(input())
B=int(input())
def prime_check(num):
    if num<2:
        return False
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1
    return True
count=0
for i in range(A,B+1):
    if prime_check(i):
        count+=1
print(count)

