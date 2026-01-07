password=input()
digit=False
upper=False
for ch in password:
    if '0'<=ch<='9':
        digit=True
    if 'A'<=ch<='Z':
        upper=True
length=len(password)>=8
if digit and upper and length:
    print("STRONG")
else:
    print("WEAK")