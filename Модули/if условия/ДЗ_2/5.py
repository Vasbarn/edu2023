first = int(input("Введите число: "))
sec = int(input("Введите число: "))
third = int(input("Введите число: "))
if first == sec == third:
    print(3)
elif first == sec or sec == third or first == third:
    print(2)
else:
    print("Не повезло")