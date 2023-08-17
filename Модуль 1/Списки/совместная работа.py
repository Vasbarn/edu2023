# langs = ['Python', 'Java', 'JS']
# print(langs)
# # elem = langs.pop(1)
#
# print(langs.index('Java'))
# # print(elem)
# my_list = [1, 2, 3]
# your_list = [4, 5, 6]
# my_list.extend(your_list)
# print(my_list)
# # my_list == [1, 2, 3, 4, 5 ,6]
# my_list = my_list + your_list
# print(my_list)
# decode = [1, 1, 0 ,1, 0, -1]
# k = decode.count(1)
#
#
# tg = [
#     ["Торговый зал 1", "Склад 1"],
#     ["Торговый зал 2", "Склад 2"],
#     ["Торговый зал 3", "Склад 3"],
#     ["Торговый зал 4", "Склад 4"]
#     ]
#
# print(tg[0])
# print(tg[0][1])
langs = ['Python', 'Java', 'JS']
langs2 = langs
langs.append("1C")
print(langs)
print(langs2)
print()
langs2 = langs.copy()
langs.append("asd")
print(langs)
print(langs2)