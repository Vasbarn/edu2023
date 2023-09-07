import random
x = random.randint(1,99)
c = 0
while True:
    r = int(input("Число от 1 до 99: "))
    if r < x:
        print("Число меньше чем нужно. Повторите ввод.")
    elif r > x:
        print("Число больше чем нужно. Повторите ввод.")
    c += 1
    if r == x:
        print(x, "Вы угадали! Число попыток: ", c)
