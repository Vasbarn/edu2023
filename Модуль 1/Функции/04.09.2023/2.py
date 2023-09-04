def fibon(num: int) -> None:
    if num < 1:
        raise TypeError
    curr_num = 0
    follow_num = 1
    spisok = list()
    for k in range(num+1):
        spisok.append(curr_num)
        curr_num, follow_num = follow_num, curr_num + follow_num

    return spisok


v = fibon(10)
print(v)


