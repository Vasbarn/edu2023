spisok = list()
def fibon(num: int, curr_num: int = 0, follow_num: int = 1, count: int = 0) -> None:
    if num < 1:
        raise TypeError
    if count > num:
        return

    spisok.append(curr_num)

    fibon(num=num, curr_num=follow_num,follow_num=curr_num+follow_num,count=count + 1)


v = fibon(10)

print(spisok)


