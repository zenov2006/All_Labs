### Первое задание
a = int(input("Введите число>>"))
print(*[i for i in range(1, a + 1)])
a = int(input("Введите число>>"))
for i in range(1, a+1):
    print(i)
### Второе задание

a, b = int(input("Введите первое число>>")), int(input("Введите второе число>>"))
print(max(a,b), "<< Это самое большое число")
