a = int(input("Введите число: "))
b = int(input("Введите число: "))
sum = 0
k = 0
for i  in range(a,b+1):
    if i % 3 == 0:
        sum += i
        k += 1
print(sum)
print(k)
print(f"Среднее арифметическое: {sum // k}")

