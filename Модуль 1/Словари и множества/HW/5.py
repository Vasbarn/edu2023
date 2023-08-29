N = int(input("Количество пар: "))
slovar = dict()
for _ in range(N):
    slovo = input("Введите  слово в виде _ - _:  ").split('-')
    if len(slovo) != 2:
        print("Неверный ввод")
        continue
    if slovo[0].isalpha() and slovo[1].isalpha():
        slovar[slovo[0]] = slovo[1]
while True:
    syn = input("Введите слово: ")
    if slovar.get(syn.lower()):
        print("Синоним к заданному слову: ", slovar[syn])
    else:
        for key, value in slovar.items():
            if syn.lower() == value.lower():
                print("Синоним к заданному слову: ", key)
                break
        else:
            print("Такого слова не найдено")



