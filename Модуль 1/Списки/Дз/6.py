sdvig = int(input("Введите шаг сдвига: "))
list = [i for i in input("Введите список: ")]
new_list = list[-sdvig:] + list[:-sdvig]
print(new_list)
