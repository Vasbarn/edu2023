import random
r = int(input('Введите число от 1 до 100: '))
a = 1
b = 101
c = 1
while True:
    comp = random.randint(a, b)
    if comp > r:
        b = comp
    elif comp < r:
        a = comp + 1
    else:
        print(f'Да, компьютер угадал с помощью {c} попыток')
        c += 1
