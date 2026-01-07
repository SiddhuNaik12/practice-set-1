sentence=input()
vowel='aeiouAEIOU'
count=0
for ch in sentence:
    if ch in vowel:
        count+=1
print(count)
