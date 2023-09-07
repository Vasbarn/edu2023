a=int(input("Введите число: "))
b=int(input("Введите число: "))
c=int(input("Введите число: "))
count = 0
total = 0
for i in range(a, b + 1):
    if i % c == 0:
        count += 1
        total += i
print("Среднее арифметическое: ", total/count)