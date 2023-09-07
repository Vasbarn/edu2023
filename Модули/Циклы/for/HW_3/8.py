text = input("Введите строку: ")
long = len(text)
flag = 0
for letter in range(0,len(text)):
    if text[letter] == text[long-1]:
        letter += 1
        long -= 1
    else:
        flag = -1
if flag != -1:
    print("Это палиндром")
else:
    print("Это не палиндром")
