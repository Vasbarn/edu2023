rows = int(input("Количество рядов: "))
seats = int(input("Количество сидений в ряду: "))
dimens = int(input("Расстояние между рядами: "))
for i in range(rows + dimens + 5):
    if i == 0:
        print("_"*(seats + 4))
    elif i == (rows + dimens + 4):
        print("_"*(seats + 4))
    else:
        ryad = f"|{'h' * (seats+2)}|"
        if i % 4 == 0:
            print(ryad)
            print(("|" + ((seats + 2)* ' ') + "|")
        else:
            print("|" + 'h' * (seats + 2) + "|")
            print(("|" + ((seats + 2)* ' ') + "|")


