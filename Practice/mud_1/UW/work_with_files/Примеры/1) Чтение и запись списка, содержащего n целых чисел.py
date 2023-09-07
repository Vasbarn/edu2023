"""
1. Чтение/запись списка, содержащего n целых чисел
"""
# Запись/чтение списка случайных чисел
# 1. Подключить модуль random
import random

# 2. Создать список из 10 случайных чисел
i = 0
lst = []
while i < 10:
    number = random.randint(0, 101)  # число от 0 до 100
    lst = lst + [number]
    i = i+1

print("lst = ", lst)

# 3. Сохранить список в текстовом файле
# 3.1. Открыть файл для записи
f = open('file.txt', 'w')

# 3.2. Записать количество элементов в списке
s = str(len(lst))  # Конвертировать целое число в строку
f.write(s + '\n')  # Записать строку

# 3.3. Записать каждый элемент
for i in lst:
    s = str(i)  # конвертировать элемент списка в строку
    f.write(s + ' ')  # записать число в строку

# 4. Закрыть файл
f.close()

# -------------------------------------------
# 5. Чтение из файла 'file.txt'
f = open('file.txt', 'r')

# 6. Прочитать из файла числа и сформировать список
# 6.1. Прочитать количество элементов в списке,
# сначала читается строка, затем эта строка
# конвертируется в целое число методом int()
s = f.readline()
n = int(s)

# 6.2. Создать пустой список
lst2 = []

# 6.3. Реализовать обход файла по строкам и считать числа.
# Для чтения строк используется итератор файла.
for line in f:
    # метод split - разбивает на слова на основании символа пробел
    strs = line.split(' ') # получить массив строк strs

    # Вывести strs с целью контроля
    print("strs = ", strs)

    # прочитать все слова и записать их в список как целые числа
    for s in strs:
        if s != '':
            lst2 = lst2 + [int(s)]  # добавить число к списку

# 6.4. Вывести результат для контроля
print("n = ", len(lst2))
print("lst2 = ", lst2)

# 6.5. Закрыть файл - необязательно
f.close()
