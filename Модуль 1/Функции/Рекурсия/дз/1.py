def vyvod(num,i = 1):
    print(i, end=" ")
    if i != num:
        vyvod(num, i + 1)


vyvod(5)
