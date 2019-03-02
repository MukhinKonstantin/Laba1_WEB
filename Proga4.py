import random
minim=99999
spisok=random.sample(range(100),10)
print("Данный список: ", spisok)
for i in range(0,10):
    if spisok[i]<minim:
        minim=spisok[i]
print("Минимальное число списка", minim)
