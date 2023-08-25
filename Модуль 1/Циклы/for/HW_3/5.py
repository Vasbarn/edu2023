text = input('Введите текст: ').split()
max_len = 0
for word in text:
    word_len = 0
    for letter in word:
        word_len += 1
    if word_len > max_len:
        max_len = word_len
print(f'Длина самого длинного слова: {max_len}')
