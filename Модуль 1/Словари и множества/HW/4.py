slovar = dict()
stroka = input("Введите текст: ").lower()
for i in stroka:
    if i in slovar:
        slovar[i] += 1
    else:
        slovar[i] = 1
    print(i, ":", slovar[i])