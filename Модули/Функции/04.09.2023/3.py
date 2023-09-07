def prosto(num: int) -> None:
    spisok = list()

    for i in range(2, num + 1):
        count = 0
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
            if count > 1:
                break
        else:
            spisok.append(i)
    return spisok

v = prosto(100)
print(v)