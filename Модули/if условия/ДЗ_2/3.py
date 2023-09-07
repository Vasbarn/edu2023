top = int(input("Введите позицию в списке: "))
count = int(input("Введите количество баллов: "))
if top <= 10:
    print("Вы поступили")
    if count > 290:
        print("Вам стипендия")
    else:
        print("Стипендии нет")
else:
    print("Вы не поступили")