N = int(input("Введите количество моделей:"))
list = []
for i in range(N):
    model = int(input('Введите модель: '))
    list.append(model)
print(list)
print(list.remove(max(list)))