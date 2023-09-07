string = input('Введите строку из 10 символов a и b: ')
milk = 0
total_liters = 0

for i in string:
    milk += 2
    if i == "b":
        total_liters += milk
    elif i == "a":
        total_liters += 0
    else:
        print("Неверный ввод данных")
        total_liters = 0

        break

print('Всего молока', total_liters, 'литров')

