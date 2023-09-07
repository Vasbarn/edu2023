num_1 = int(input("Введите число:"))
num_2 = int(input("Введите число:"))
num_3 = int(input("Введите число:"))
max = 0
if num_3 < num_1 > num_2:
    max = num_1
elif num_3 < num_2 > num_1:
    max = num_2
elif num_2 < num_3 > num_1:
    max = num_3
print("Максимальное число: ", max)

