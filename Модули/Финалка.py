Sep = "----------------------------------------"
def menu() -> int:
    print(Sep)
    print("ГЛАВНОЕ МЕНЮ")
    print("1 - Ввести или обновить информацию", "2 - Вывести информацию", "0 - Завершить работу", sep="\n")
    vvod = int(input("Введите номер пункта меню: "))
    return vvod


def input_update():
    print(Sep)
    print("ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ")
    print("1 - Личная информация", "2 - Информация о предпринимателе", "0 - Назад", sep="\n")
    vvod = int(input("Введите номер пункта меню: "))
    return vvod


def private():
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    telephone = input("Введите номер телефона (+7XXXXXXXXXX): ")
    mail = input("Введите адрес электронной почты: ")
    index = input("Введите почтовый индекс: ")
    while not index.isnumeric():
        index = (input("Введите почтовый индекс: "))
    post = input("Введите почтовый адрес (без индекса): ")
    extra_inf = input("Дополнительная информация: ")
    s = f"Имя: {name}\n Возраст: {age}\n Телефон: {telephone}\n E-mail: {mail}\n Индекс: {index}\n Адрес: {post}"
    return s


def man_info():
    ogrn = int(input("Введите ОГРНИП: "))
    while len(str(ogrn)) != 15:
        print("ОГРНИП должен содержать 15 цифр")
        ogrn = int(input("Введите ОГРНИП: "))
    inn = int(input("Введите ИНН: "))
    counting_count = int(input("Введите расчетный счет: "))
    while len(str(counting_count)) != 20:
        print("Расчетный счет должен содержать 20 цифр")
        counting_count = int(input("Введите расчетный счет: "))
    bank_name = input("Введите название банка: ")
    bik = int(input("Введите БИК:"))
    respond_count = int(input("Введите корреспондентский счет:"))
    s = (f"ОГРНИП: {ogrn}\n ИНН: {inn}\n Р/с: {counting_count}\n Банк: {bank_name}\n БИК: {bik}\n К/с: {respond_count}")
    return s


def output():
    print(Sep)
    print("ВЫВЕСТИ ИНФОРМАЦИЮ")
    print("1 - Общая информация", "2 - Вся  информация", "0 - Назад", sep="\n")
    vyvod = int(input("Введите номер пункта меню: "))
    return vyvod

# main
print("Приложение MyProfile", "Сохраняй информацию о себе и выводи ее в других форматах", sep = "\n")
while True:
    men = menu()
    if men == 0:
        break
    elif men == 1:
        vvod = input_update()
        if vvod == 1:
            pers_inf = private()
        elif vvod == 2:
            bussines_inf = man_info()
        elif vvod == 3:
            exit
    elif men == 2:
        escape = output()
        if escape == 0:
            exit
        elif escape == 1:
            print(pers_inf)
        elif escape == 2:
            print(f"{pers_inf}\n\nИнформация о предпринимателе\n{bussines_inf}\n{Sep}")






























