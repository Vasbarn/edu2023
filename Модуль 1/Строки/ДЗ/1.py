# menu = input("Введите названия блюд: ").split(";")
# print("Доступные блюда: ", ", ".join(menu))
menu = input("Введите названия блюд: ")
print(f"Введите названия блюд: {menu.replace(';',', ')}")