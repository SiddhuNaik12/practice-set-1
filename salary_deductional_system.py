salary=int(input())
late_days=int(input())
absent_days=int(input())
deduction=0
if late_days>10:
    deduction+=10/100
elif late_days>5:
    deduction+=5/100
if absent_days>2:
    deduction+=5/100
salary=salary-(salary*deduction)
print(int(salary))