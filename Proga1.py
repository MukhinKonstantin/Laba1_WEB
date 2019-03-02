a=float(input("Введите значение a: "))
b=float(input("Введите значение b: "))
c=float(input("Введите значение c: "))
d=float(input("Введите значение d: "))
k=float(input("Введите значение k: "))
if (b==0) or (a==0): 
    print("Происходит деление на 0")
else:
    x=abs( ((a**2)-(b**3)-(c**3)*a**2)*(b-c+c*(k-d/b**3))-(((k/b-k/a)*c)**2)-20000 )
    print("Ответ: ",x)
