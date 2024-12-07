### 1)
def greet(name):
    return "Здравствуйте " + name + "!"
a = input()
print(greet(a))

def sqaure(number):
    return number ** 2
b = input()
print(sqaure(b))

def max_of_two(x, y):
    return max(x, y)
print(max_of_two(int(input()), int(input())))
### 2)
def describe_person(name, age = 30):
    return name, age
print(*describe_person(input()))
### 3)
def is_prime(num):
    cont = 0
    for i in range(1, num+1):
        if num % i == 0:
            cont += 1
    if cont > 2:
        return False
    else:
        return True
print(is_prime(int(input())))
