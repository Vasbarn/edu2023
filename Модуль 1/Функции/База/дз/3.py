def summa(num: int) -> int:

    stek = list()
    while True:
        if num // 10 != 0:
            stek.append(num % 10)
            num = num // 10
        else:
            stek.append(num % 10)
            break

    print("Сумма равна:", sum(stek))



def minimum(num: int) -> int:
    stek = list()
    while True:
        if num // 10 != 0:
            stek.append(num % 10)
            num = num // 10
        else:
            stek.append(num % 10)
            break
    mini = min(stek)
    print("Минимальная цифра в числе: ", mini)


def maximum(num: int) -> int:
    stek = list()
    while True:
        if num // 10 != 0:
            stek.append(num % 10)
            num = num // 10
        else:
            stek.append(num % 10)
            break
    maxi = max(stek)
    print("Максимальная цифра в числе: ", maxi)


while True:
    number = input("Введите число: ")
    vvod = input("Выберите действие ( 1 - максимум, 2 - минимум, 3 - сумма: ")
    number = int(number)
    vvod = int(vvod)
    if vvod == 1:
        maximum(number)
    elif vvod == 2:
        minimum(number)
    elif vvod == 3:

        summa(number)

