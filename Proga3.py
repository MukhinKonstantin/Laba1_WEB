import random
sum=0
spisok=random.sample(range(20),10)
print("Данный список: ", spisok)
for i in range(0,10):
    if spisok[i]<=10 and spisok[i]>=1:
        sum=sum+spisok[i]
print(sum)
