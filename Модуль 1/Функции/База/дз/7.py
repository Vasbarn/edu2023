import random
def rock_paper_scissors():
    while True:
        r_p_s = input("Камень, ножницы, бумага?  ").lower()
        r = random.randint(0,2)
        answer = ["Камень", "Ножницы", "Бумага"]
        l2 = list()
        l2.append(r_p_s)
        otvet = answer[r].lower()
        print(otvet)
        if otvet == l2[0]:
            print("Ничья")
        elif (l2[0] == "камень" and otvet == "ножницы") or (l2[0] == "ножницы" and otvet == "бумага") or (l2[0] == "бумага" and otvet == "камень"):
            print("Вы выиграли")
        else:
            print("Вы проиграли")








def guess_the_number():
    flag = 0
    x1 = int(input("Задайте нижнюю границу интервала загаданных чисел: "))
    x2 = int(input("Задайте верхнюю границу интервала загаданных чисел: "))
    while flag == 0:
        guess = random.randint(x1, x2)
        numb = int(input(f"Число лежит в диапазоне от {x1} до {x2} Попробуйте его отгадать : "))
        if numb == guess:
            print("Вы угадали!")
            flag += 1
        else:
            print("Не угадали! Попробуйте еще раз")

def mainMenu():
    menu = int(input("Нажмите 1 для игры в 'Камень. Ножницы. Бумага' или нажмите 2 для игры в 'Угадай число: "))
    if menu == 1:
        rock_paper_scissors()
    elif menu == 2:
        guess_the_number()




mainMenu()