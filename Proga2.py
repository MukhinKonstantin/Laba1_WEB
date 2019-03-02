stroka=str(input("Введите строку: "))
m=stroka.split(' ')
for i in range(0,len(m)):
    if i%2==0:
        print(m[i])
