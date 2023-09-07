def nod (num1: int, num2: int):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
           num1 = num1 % num2
        else:
            num2 = num2 % num1
    delitel = num1 + num2
    print("Нод заданных чисел равен: ", delitel)






number_1 = int(input("Введите 1 число: "))
number_2 = int(input("Введите 2 число: "))
nod(number_1, number_2)