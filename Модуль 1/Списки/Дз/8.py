N = int(input("Введите количество элементов списка: "))
list = []
for i in range(N):
    count = int(input("Введите число: "))
    list.append(count)
print(sorted(list))