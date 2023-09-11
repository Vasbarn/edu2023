from typing import Union


def new_lst(value: Union[list, int], spisok: list = None):
    if spisok is None:
        spisok = []
    if isinstance(value, int):
        spisok.append(value)
        return spisok
    for i in value:
        new_lst(i, spisok)
    return spisok


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
r = new_lst(nice_list)
print(r)