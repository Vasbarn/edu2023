stroka = input("Введите слова через пробел: ").split()
# mlen = len(stroka[0])
# index = 0
# for i in range(0,len(stroka)):
#     if mlen < len(stroka[i]):
#         mlen = len(stroka[i])
#         index = i
# print(mlen, stroka[index])

for index, word in enumerate(stroka):
    if index == 0:
        maxlen = len(word)
        slovo = word
    else:
        if maxlen < len(word):
            maxlen = len(word)
            slovo = word
print(maxlen, slovo)