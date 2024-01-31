a = input("Введіть рядок")
b = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        substr = a[i:j]
        str = a[j:]
        if substr in str:
            b.append(substr)
c = set(b)
print("Частини що повторюються: ", c)