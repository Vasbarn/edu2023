word = input('Введите зашифрованое слово: ')
sum1 = ' '
sum2 = ' '
count = 0

for text in word:
    count += 1
    if (count % 2 == 1):
        sum1 += text
    else:
        sum2 = text + sum2

print('Расшифрованое слово', sum1 + sum2)