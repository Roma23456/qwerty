a = [3456, 567, 00, 2332, 45, 66]
b = []
for i in a:
    if str(i) == str(i)[::-1]:
        b.append(i)
print("Числа паліндроми: ", b)