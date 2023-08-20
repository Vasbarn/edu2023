N = int(input('Количество контейнеров: '))
list = []
for i in range(N):
    cont = int(input('Введите вес контейнера: '))
if cont <= 200:
   list.append(cont)

new_cont = int(input('Введите вес нового контейнера: '))
index = 0
while index < len(list) and list[index] >= new_cont:
    index += 1

print('Номер, который получит новый контейнер:', index + 1)



