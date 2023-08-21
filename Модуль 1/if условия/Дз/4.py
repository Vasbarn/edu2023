chair_1 = int(input("Введите стоимость 1 стула: "))
chair_2 = int(input("Введите стоимость 2 стула: "))
chair_3 = int(input("Введите стоимость 3 стула: "))
price = chair_1 + chair_2 + chair_3
if price > 10000:
    print(f"Конечная цена по скидке: {price*0,9}")
else:
    print(f"Конечная цена: {price}")