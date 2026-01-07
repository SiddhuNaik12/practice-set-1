# capacity=1000
# n=int(input())
# current_capacity=0
# minute=0
# for i in range(n):
#     minute+=1
#     inflow=int(input())
#     current_capacity+=inflow
#     if current_capacity>capacity:
#         print(minute)
#         exit()
       
capacity = 1000
N = int(input())
inflows = input().split()   # split string into pieces
current = 0
for minute in range(N):
    inflow = int(inflows[minute])   # convert each value manually
    current += inflow
    if current > capacity:
        print(minute + 1)
        break
