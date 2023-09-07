def count_letters(text, letter: str, num: int):
    count_let = 0
    count_num = 0
    for i in text:
        if i == letter:
            count_let += 1
        elif i == num:
            count_num += 1
    print("Количество искомых букв: ", count_let)
    print("Количество искомых цифр: ", count_num)






stroka = input("Введите текст: ").lower()
bukva = input("Введите искомую букву: ").lower()
cifra = int(input("Введите искомую цифру: "))
count_letters(stroka, bukva, cifra)

