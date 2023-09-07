def new_lst(*args):
    spisok = []
    for i in args:
        for j in i:
            if not isinstance(j, list):
                spisok.append(j)
            else:
                result = new_lst(j)
    spisok.append(result)
    return spisok


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
r = new_lst(nice_list)
print(r)