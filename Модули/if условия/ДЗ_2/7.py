clock = int(input("Введите время (в часах): "))
while 0 < clock < 23:
    if 14 <= clock <= 15 and clock != 10 and clock != 18:
        print("Посылку получить нельзя")
        clock = -1
    else:
        print("Посылку можно получить")
        clock = -1