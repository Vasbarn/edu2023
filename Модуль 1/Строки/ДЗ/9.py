stroka=input("Введите текст: ")
s=''.join(stroka)
big=0
small=0
for i in s:
    if i.islower():
        small+=1
    else:
        big+=1
print("Количество строчных букв: ", small, "\n" ,"Количество заглавных букв: ", big)
