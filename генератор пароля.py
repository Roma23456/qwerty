import random
simbols = "fjiefuwdegwforgpotgijiejdwuhwgyqgftwfqt438549hy3uj2bngmbgbzxpoqq"
a = ""
b = int(input("Введіть довжину пароля, яку ви хочете: "))
for i in range(b):
    a += random.choice(simbols)
print("Ваш пароль: ", a)