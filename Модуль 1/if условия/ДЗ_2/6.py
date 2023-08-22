price = int(input("Введите стоимость: "))
square = int(input("Введите площадь: "))
if (square >= 100 and price <= 10000000) or (square >= 80 and price <= 7000000):
    print("Квартира подходит")
else:
    print("Квартира не подходит")

