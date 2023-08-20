sdvig = int(input("Введите шаг сдвига: "))
N = int(input('Количество элементов: '))
list = []
for i in range(N):
    c = int(input('Введите числа: '))
    list.append(c)
new_list = list[-sdvig:] + list[:-sdvig]
print(new_list)
