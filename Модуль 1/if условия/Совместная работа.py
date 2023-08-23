x = 1
y = 2
z = 3
k = 6
if y < z and y > x or k == 5:
    print("Тест")

if x < y < z or k == 5:
    print("Тест")

if x == 1:
    my_list = [2, 4, "слово", {}]
elif x == 2:
    my_list = 1223
else:
    my_list = None



if my_list:
    if isinstance(my_list, int):
        print("Это целочисленное число")
    elif len(my_list) == 4:
        print("Список содержит 4 элемента")
    else:
        print("Не подходит под условие")
