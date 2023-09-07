total_card = int(input("Введите количество карт:"))
exists_list = list()
for card in range(1, total_card):
    exists_list.append(int(input("Номер изветной карты")))

for card in range(1, total_card + 1):
    if card not in exists_list:
        print("Этой карты у нас нет: {}".format(card))
        break