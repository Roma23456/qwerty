a = input("Введіть рядок: ")
b = {}
unnecessary_words = ["і", "та", "або", "не", "на", "у", "з", "за", "під", "від", "до", "по"]
for i in a:
    words = i.split()
    for c in words:
        c = c.strip('.,!?-:;\'"()[]{}')
        c = c.lower()
        if c not in unnecessary_words:
            if c not in b:
                b[c] = 1
            else:
                b[c] += 1
words = []
for i in range(10):
    max_word = None
    max_count = 0
    for key, values in b.items():
        if values > max_count:
            max_word = key
            max_count = values
    if max_word is not None:
        words.append((max_word, max_count))
        del b[max_word]
for key, value in words:
    print(f"{key}: {value} разів")