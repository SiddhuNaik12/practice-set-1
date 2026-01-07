seats=40
N=int(input())
allocated_seats=0
for _ in range(N):
    request=int(input())
    allocated_seats+=request
    if allocated_seats<=40:
        print("CONFIRMED")
    else:
        print("WAITLISTED")
