x = 8
y = 10
move = input(f"Робот находится в точке {x, y}. Выберите направление: ")
while True:
    if move.upper() == "W":
        y += 1
        if y > 20:
            y -= 1
            print(f"Робот находится в точке {x, y}")

        print(f"Робот находится в точке {x, y}")
    elif move.upper() == "S":
        y -= 1
        if y < 0:
            y += 1
            print(f"Робот находится в точке {x, y}")
        print(f"Робот находится в точке {x, y}")
    elif move.upper() == "A":
        x -= 1
        if x < 0:
            x += 1
            print(f"Робот находится в точке {x, y}")
        print(f"Робот находится в точке {x, y} ")
    elif move.upper() == "D":
        x += 1
        if x > 15:
            x -= 1
            print(f"Робот находится в точке {x, y}")
        print(f"Робот находится в точке {x, y}")

    else:
        print("Используйте клавиши WASD")

    move = input(f"Выберите направление: ")


