a = input("Введіть список чисел, розділені пробілами: ").split()
b = {}
for num in a:
    if num in b:
        b[num] += 1
    else:
        b[num] = 1
print("Словник унікальних значень та їх кількостей:")
for key, values in b.items():
    print(f"{key}: {values}")