def sum(a, b):
    return a + b
def vidnimannia(a, b):
    return a - b
def mnojennia(a, b):
    return a * b
def dilenia(a, b):
    return a / b
def power(a, b):
    return a ** b
def square_root(a):
    return a ** 0,5
def reverse_number(a):
    return int(str(a)[::-1])
while True:
    print("Операції калькулятора: ")
    print("1: додати числа")
    print("2: відняти числа")
    print("3: помножити числа")
    print("4: поділити числа")
    print("5: піднести до степеня числа(де перше введене число це основа степеня, а друге введене число - показник степеня)")
    print("6: взяти в корінь число")
    print("7: обернути число")
    print("8: вийти з калькулятора")
    a = int(input("Введіть число з операцією, яку ви хочете зробити: "))
    if a == 1:
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))
        print(sum(num1, num2))
    elif a == 2:
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))
        print(vidnimannia(num1, num2))
    elif a == 3:
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))
        print(mnojennia(num1, num2))
    elif a == 4:
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))
        print(dilenia(num1, num2))
    elif a == 5:
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))
        print(power(num1, num2))
    elif a == 6:
        num = int(input("Введіть число: "))
        print(square_root(num))
    elif a == 7:
        num = int(input("Введіть число: "))
        print(reverse_number(num))
    elif a == 8:
        print("дякую за те що використали мій калькулятор, гуд бай і всього самого найкращого)")
        break