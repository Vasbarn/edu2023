num = int(input("Введите число: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Число цифр:", count)
