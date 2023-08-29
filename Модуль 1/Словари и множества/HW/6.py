N = int(input("Введите количество заказов: "))
pizzeria = dict()
for _ in range(N):
    name, pizza_name, counts = input("Покупатель - название пиццы - количество заказанных пицц: ").split('-')
    if pizzeria.get(name):
        if pizzeria[name].get(pizza_name):
            pizzeria[name][pizza_name] += int(counts)
        else:
            pizzeria[name][pizza_name] = int(counts)


    else:
        pizzeria[name] = {
            pizza_name:int(counts)
        }


print(pizzeria)