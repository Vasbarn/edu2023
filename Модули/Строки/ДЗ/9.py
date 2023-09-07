stroka=input("Введите текст: ")

big=0
small=0
for i in stroka:
    if i.islower():
        small+=1
    elif i.isupper():
        big+=1
print("Количество строчных букв: ", small, "\n" ,"Количество заглавных букв: ", big)
