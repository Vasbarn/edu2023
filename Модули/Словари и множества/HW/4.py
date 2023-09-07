slovar = dict()
stroka = input("Введите текст: ").lower()
for i in stroka:
    if i in slovar:
        slovar[i] += 1
    else:
        slovar[i] = 1
print(slovar)
inv_slovar = dict()
for key, value in slovar.items():
    if inv_slovar.get(value) is None:
        inv_slovar[value] = [key]
    else:
        inv_slovar[value].append(key)
print()
print(inv_slovar)