Sep = "----------------------------------------"
def menu() -> int:
    print(Sep)
    print("ГЛАВНОЕ МЕНЮ")
    print("1 - Ввести или обновить информацию", "2 - Вывести информацию", "0 - Завершить работу", sep="\n")
    vvod = int(input("Введите номер пункта меню: "))
    if vvod == 0:
        exit
    elif vvod == 1:
        input_update()
    elif vvod == 2:
        output()



def input_update():
    print(Sep)
    print("ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ")
    print("1 - Личная информация", "2 - Информация о предпринимателе", "0 - Назад", sep="\n")
    vvod = int(input("Введите номер пункта меню: "))
    if vvod == 0:
        menu()
    elif vvod == 1:
        private()
    elif vvod == 2:
        man_info()


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
    s = (f"Имя: {name}\n Возраст: {age}\n Телефон: {telephone}\n E-mail: {mail}\n Индекс: {index}\n Адрес: {post}")
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


# def back():
def output():
    print(Sep)
    print("ВЫВЕСТИ ИНФОРМАЦИЮ")
    print("1 - Общая информация", "2 - Вся  информация", "0 - Назад", sep="\n")
    vyvod = int(input("Введите номер пункта меню: "))
    if vyvod == 0:
        menu()
    elif vyvod == 1:
        general(private())
    elif vyvod == 2:
        all(private(),man_info(), Sep)

def general(func):
    print(func)


def all(func1, func2, sep):
    print(f"{func1}\n\nИнформация о предпринимателе\n{func2}\n{sep}")



# main
print("Приложение MyProfile", "Сохраняй информацию о себе и выводи ее в других форматах", sep = "\n")
while True:
    menu()























