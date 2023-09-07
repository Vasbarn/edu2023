def reverse(num:int) -> int:
    new_num = 0
    summ = 0
    while num > 0:
        new_num = num % 10
        summ *= 10
        summ = summ + new_num
        num = num // 10
    return summ

number = 1
while number != 0:
    number = int(input("Введите число: "))
    print("Перевернутое число", reverse(number))
